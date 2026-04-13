from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit
import servo
# 核心：使用官方 M5mqtt 库
from m5mqtt import M5mqtt

# --- 1. 硬件初始化 ---
setScreenColor(0xc45353)
finger_1 = unit.get(unit.FINGER, unit.PORTC)
servo_0 = servo.Servo(26) # Port B
is_working = False

try:
    tof_0 = unit.get(unit.TOF, unit.PORTA)
except:
    tof_0 = None

# --- 2. 你的原始 UI 元素 (完全不动) ---
finger = M5TextBox(18, 91, "finger", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
user = M5TextBox(18, 65, "User", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label0 = M5TextBox(0, 22, "Smart takeout cabinet", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
circle0 = M5Circle(275, 126, 15, 0xffffff, 0xFFFFFF)
circle1 = M5Circle(230, 142, 15, 0xffffff, 0xFFFFFF)
circle2 = M5Circle(216, 184, 15, 0xf7f5f5, 0xFFFFFF)
circle3 = M5Circle(275, 190, 35, 0x19a4a1, 0x19a4a1)
label = M5TextBox(0, 0, "Welcome", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
rectangle0 = M5Rect(18, 179, 35, 35, 0x33a72e, 0xc45353)
rectangle1 = M5Rect(58, 179, 35, 35, 0xd5c276, 0xc45353)
rectangle2 = M5Rect(99, 178, 35, 35, 0x6734a9, 0xc45353)
rectangle3 = M5Rect(140, 178, 35, 35, 0xd6285f, 0xc45353)
debug_tof = M5TextBox(275, 10, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)

# 初始化：360度舵机停止
servo_0.write_angle(90)

# --- 3. 核心动作函数 ---
def servo_run_cycle(direction='open'):
    if direction == 'open':
        servo_0.write_angle(70) 
        wait(1.0)
    else:
        servo_0.write_angle(110) 
        wait(1.0)
    servo_0.write_angle(90)

def open_door_sequence(name, mode='Local'):
    global is_working
    if is_working: return
    is_working = True
    
    # 向中控反馈：开门中
    try: mqtt_client.publish('city/status/a', '已解锁')
    except: pass
    
    rgb.setColorAll(0xffffff)
    user.setText(name)
    finger.setText(mode + ' Unlocked!')
    rgb.setColorAll(0x33ff33)
    wait(1) 
    
    servo_run_cycle('open')
    wait(2)
    user.setText('Status: Open!')
    rgb.setColorAll(0xff9900)
    wait(4) 
    
    servo_run_cycle('close')
    user.setText('Status: Close!')
    rgb.setColorAll(0xffffff)
    wait(1)
    
    user.setText('User')
    finger.setText('Finger')
    rgb.setColorAll(0x000000)
    
    try: mqtt_client.publish('city/status/a', '正常关闭')
    except: pass
    is_working = False

# --- 4. MQTT 逻辑 ---
mqtt_client = M5mqtt("Device_A_M5Go", "broker.emqx.io", 1883, "", "", 300)

def web_control_callback(topic_data):
    # 收到中控发来的字符串指令
    print("MQTT Received: " + str(topic_data))
    if topic_data == 'UNLOCK':
        open_door_sequence("Web Admin", mode='Web')
    elif topic_data == 'LOCK':
        servo_0.write_angle(90)

# 订阅必须在 start 之后或紧随其后
mqtt_client.subscribe("city/device_A/cmd", web_control_callback)

# --- 5. 指纹回调 ---
def finger_1_cb(user_id, access):
    if access == 1:
        name = 'Jasper' if user_id == 1 else 'Alen'
        open_door_sequence(name, mode='Finger')

finger_1.readFingerCb(callback=finger_1_cb)
finger_1.getUnknownCb(lambda: [rgb.setColorAll(0xff0000), finger.setText('Unauthorized!'), wait(1), rgb.setColorAll(0x000000)])

# --- 6. 启动服务 ---
try:
    mqtt_client.start()
    label.setText("Welcome")
except:
    label.setText("Offline")

# --- 7. 按钮控制 ---
btnA.wasPressed(lambda: [finger_1.removeAllUser(), user.setText('Cleared')])
btnB.wasPressed(lambda: [user.setText('Add User 1...'), finger_1.addUser(1, 1)])
btnC.wasPressed(lambda: [user.setText('Add User 2...'), finger_1.addUser(2, 1)])

# --- 8. 主循环 ---
last_report_time = 0
while True:
    if tof_0:
        try:
            dist_val = tof_0.distance
            debug_tof.setText(str(dist_val))
            if not is_working:
                if dist_val < 300:
                    label.setText('Warning!')
                    rgb.setColorAll(0xff0000)
                else:
                    label.setText('Welcome')
                    rgb.setColorAll(0x000000)
        except:
            pass
    
    # 每 5 秒强制上报一次状态，确保网页端同步
    if time.ticks_ms() - last_report_time > 5000:
        try:
            current_status = "正常关闭" if not is_working else "开门中"
            mqtt_client.publish('city/status/a', current_status)
        except:
            pass
        last_report_time = time.ticks_ms()

    wait_ms(100)