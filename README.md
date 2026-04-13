# AIoT 智慧城市系统
**基于 M5Stack + ESP32-S3 | MQTT 分布式架构 | 飞书自然语言交互**

[![MQTT](https://img.shields.io/badge/Protocol-MQTT-blue)](https://mqtt.org/)
[![Python](https://img.shields.io/badge/Backend-Python%20Flask-yellow)](https://flask.palletsprojects.com/)
[![ESP32-S3](https://img.shields.io/badge/AI%20Terminal-ESP32--S3-purple)](https://www.espressif.com/en/products/socs/esp32-s3)
[![M5Stack](https://img.shields.io/badge/Device-M5Go%20Kit-orange)](https://m5stack.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 📋 项目简介
本项目是一套**基于IoT设计的分布式AIoT智慧城市系统**，采用分层解耦架构设计，以 **Website 智慧管控平台为全系统唯一核心中枢**，实现「自然语言交互-智能决策-集中管控-硬件执行-状态反馈」的完整业务闭环。

系统支持**双平行入口**：管理员可视化管控平台 + 普通用户飞书自然语言交互，基于标准MQTT协议实现硬件终端与上层系统的完全解耦，从架构根源解决多入口并发竞态问题，零基础可快速落地，同时具备工业级IoT系统的严谨性与可扩展性。

### 核心特性
- ✅ **统一中枢管控**：Website平台为全系统唯一指令入口，所有操作统一收口、规则统一校验
- ✅ **AI自然语言交互**：基于ESP32-S3部署MiniClaw智能体，飞书端纯自然语言即可控制设备
- ✅ **双入口完全解耦**：Website管控与飞书交互互不影响，单入口故障不影响系统整体运行
- ✅ **完整业务闭环**：智能外卖柜锁控 + 消防应急全局联动，覆盖智慧城市核心场景
- ✅ **并发安全防护**：内置优先级仲裁、忙碌互斥锁、幂等性设计，彻底解决多入口指令冲突
- ✅ **全链路可追溯**：所有操作全程留痕，审计日志完整可查，适配毕设验收与问题排查

---

## 🏗️ 系统整体架构
<img width="2940" height="816" alt="image" src="https://github.com/user-attachments/assets/a841c27b-1cd3-4fae-902d-0fd2bd82514e" />


### 分层核心职责
| 架构层级 | 核心定位 | 不可突破权责红线 |
|----------|----------|------------------|
| 用户入口层 | 系统双平行用户入口，服务不同角色 | 仅做指令输入与结果展示，不做任何决策、不存储系统规则 |
| 智能决策层 | 自然语言翻译官+AI决策大脑 | 仅与Website通信，**绝对不直接连接硬件下发指令** |
| 中枢管控层 | 全系统唯一核心大脑、唯一真相来源、唯一硬件指令入口 | 全系统唯一有权限给硬件下发指令的模块，所有操作必须经过本层校验 |
| 消息通信总线层 | 系统通信中枢、解耦核心 | 仅做标准MQTT消息透传，不修改任何指令、不做任何逻辑判断 |
| 边缘硬件执行层 | 物理世界执行终端 | 仅做指令执行与状态上报，不做任何决策逻辑 |

---

## 📦 核心模块详解
### 1. Website 智慧中控平台
**全系统唯一中枢，统一前端可视化UI + Flask后端核心引擎**
- 核心功能：
  - 可视化仪表盘：实时展示所有终端设备运行状态
  - 手动管控：按钮式控制外卖柜开关、消防应急触发/解除
  - 规则引擎：权限校验、指令优先级仲裁、忙碌互斥锁、应急状态拦截
  - 全局状态机：全系统唯一状态真相来源，同步所有设备实时状态
  - 审计日志：全链路操作留痕，支持历史记录查询与导出
- 技术栈：Python Flask、HTML/CSS/JavaScript、paho-mqtt

### 2. MiniClaw 智能体（ESP32-S3）
**系统自然语言交互入口，边缘端部署纯离线AI推理**
- 核心硬件：ESP32-S3-WROOM-1 开发板
- 核心功能：
  - 飞书WebSocket长连接：实时接收用户自然语言指令、返回执行结果
  - 自然语言意图解析：离线完成用户指令识别，转换为系统标准指令
  - 决策预校验：执行前从Website拉取全局状态，提前拦截非法操作
  - 指令提交：将标准指令提交给Website中枢执行
- 技术栈：MiniClaw固件、ESP-IDF、飞书开放平台API、MQTT客户端

### 3. 智能外卖柜子系统（M5Go）
**物理执行终端，实现外卖柜智能锁控与安全监测**
- 核心硬件：M5Go主控、GroveHub扩展板、指纹识别模块、TOF测距模块、360°舵机
- 核心功能：
  - 本地指纹解锁：支持双用户指纹录入、识别、权限管理
  - 远程指令执行：接收Website下发的开关锁、应急锁定指令
  - 安全监测：TOF测距异常预警，<300mm触发声光报警
  - 状态实时上报：事件触发+定时上报设备状态，保障中枢同步
- 技术栈：MicroPython、UIFlow、M5Stack硬件驱动

### 4. 消防应急子系统（M5Go）
**系统安全预警核心，实现火情监测与全局应急联动**
- 核心硬件：M5Go主控、GroveHub扩展板、ENV温湿度传感器、板载RGB灯/扬声器
- 核心功能：
  - 环境监测：温湿度实时采集，3次采样平均值滤波防误判
  - 火情自动判定：≥40℃触发火警，≤35℃解除预警，防临界值反复触发
  - 本地声光报警：火警触发后红色RGB爆闪+间断蜂鸣报警
  - 全局应急广播：MQTT推送全局应急指令，触发全系统联动
- 技术栈：MicroPython、UIFlow、M5Stack硬件驱动

---

## 📡 通信协议规范
### MQTT 主题规范
| 主题 | 发布方 | 订阅方 | 消息内容 | 核心用途 |
|------|--------|--------|----------|----------|
| `city/device_A/cmd` | Website中枢 | 外卖柜终端 | `UNLOCK`/`LOCK`/`EMERGENCY_FIRE` | 外卖柜控制指令下发 |
| `city/status/a` | 外卖柜终端 | Website中枢 | `正常关闭`/`已解锁`/`开门中` | 外卖柜状态上报 |
| `city/status/b` | 消防终端 | Website中枢 | `正常`/`火警触发` | 消防系统状态上报 |
| `city/all/cmd` | Website中枢 | 全终端 | `EMERGENCY_FIRE`/`EMERGENCY_STOP` | 全局应急广播 |

### 指令优先级规则
| 优先级 | 指令类型 | 执行规则 |
|--------|----------|----------|
| 0（最高） | 应急指令 | 强制锁定执行，清空所有待执行普通指令 |
| 1 | 关锁指令 | 优先级高于开锁指令 |
| 2 | 开锁指令 | 非应急、非忙碌状态下可执行 |

---

## 🚀 快速开始
### 前置环境准备
1. 硬件准备：
   - M5Go主控 ×2（外卖柜+消防）
   - ESP32-S3开发板 ×1（MiniClaw）
   - 配套传感器、执行器模块
   - 2.4GHz WiFi（所有设备接入同一局域网）
2. 软件准备：
   - Python 3.8+
   - M5Burner固件烧录工具
   - 飞书开放平台企业自建机器人
   - 可选：Docker（本地部署EMQX MQTT Broker）

### 步骤1：部署MQTT消息总线
- 方案A（快速上手）：使用免费公共EMQX Broker `broker.emqx.io:1883`
- 方案B（私有部署）：本地Docker一键部署私有Broker
  ```bash
  docker run -d --name emqx -p 1883:1883 emqx/emqx:latest
  ```

### 步骤2：烧录边缘硬件终端程序
1. **消防应急子系统**：
   - 按文档完成硬件接线，确认模块连接正常
   - 烧录配套MicroPython代码，修改WiFi名称、密码、MQTT Broker地址
   - 开机测试温湿度采集、火警触发、MQTT广播功能
2. **智能外卖柜子系统**：
   - 完成硬件接线，录入测试指纹
   - 烧录配套MicroPython代码，修改WiFi与MQTT配置
   - 测试指纹解锁、TOF预警、远程指令响应功能

### 步骤3：启动Website智慧管控平台
1. 克隆仓库到本地，安装Python依赖
   ```bash
   git clone <你的仓库地址>
   cd website-control-center
   pip install -r requirements.txt
   ```
2. 修改`app.py`中的MQTT配置（如需私有部署），启动后端服务
   ```bash
   python app.py
   ```
3. 浏览器访问 `http://localhost:5000`，确认Web面板正常加载、设备状态同步正常

### 步骤4：启动MiniClaw智能体
1. ESP32-S3烧录MiniClaw固件，配置WiFi、飞书机器人密钥、MQTT地址、Website接口地址
2. 开机确认飞书WebSocket连接正常、MQTT客户端在线、Website接口访问正常
3. 飞书发送`你好`，确认终端正常回复，完成部署

### 步骤5：全系统联调
1. 按顺序启动：Website中枢 → 外卖柜终端 → 消防终端 → MiniClaw智能体
2. Web面板点击「打开外卖柜」，确认柜门正常开启、状态同步正常
3. 飞书发送「打开外卖柜」，确认全流程执行正常、飞书收到回执
4. 飞书发送「触发火警」，确认全系统应急联动正常、外卖柜锁定、声光报警正常
5. 飞书发送「解除火警」，确认全系统恢复正常状态

---

## 🎬 标准演示流程（毕设答辩专用）
1. **开机上线**：依次启动所有模块，Web面板/飞书确认所有设备在线，展示系统整体架构
2. **本地功能演示**：指纹解锁外卖柜，展示本地控制能力；手捂ENV传感器触发火警，展示本地报警与联动能力
3. **Web管控演示**：Web面板点击开关锁、触发/解除火警，展示管理员可视化管控能力
4. **AI自然语言交互演示**：飞书发送自然语言指令，展示「语音转指令-智能决策-硬件执行-结果回执」的完整AIoT闭环
5. **应急联动演示**：触发火警后，展示外卖柜自动锁定、消防报警、中枢告警的全系统联动闭环
6. **恢复演示**：解除火警，所有设备恢复常规状态，演示完成

---

## ✅ 项目验收清单
| 模块 | 验收项 | 完成状态 |
|------|--------|----------|
| Website管控平台 | Web面板正常加载，设备状态实时同步 | ☐ |
| Website管控平台 | 按钮指令下发正常，设备响应无延迟 | ☐ |
| MiniClaw智能体 | 飞书长连接稳定，自然语言指令解析准确 | ☐ |
| MiniClaw智能体 | 指令提交正常，飞书回执准确及时 | ☐ |
| 外卖柜子系统 | 指纹解锁正常，TOF预警功能正常 | ☐ |
| 外卖柜子系统 | 远程指令响应正常，状态上报准确 | ☐ |
| 消防应急系统 | 温湿度采集正常，火警触发准确 | ☐ |
| 消防应急系统 | 全局应急广播正常，声光报警正常 | ☐ |
| 全系统联动 | 火警触发后全设备联动正常，解除后恢复正常 | ☐ |
| 并发安全 | 多入口同时下发指令，无冲突、无重复执行 | ☐ |
| 故障隔离 | 单模块故障不影响其他模块正常运行 | ☐ |

---

## ❓ 常见问题 FAQ
1. **MQTT连接失败怎么办？**
   - 检查所有设备是否接入同一2.4GHz WiFi，确认WiFi无AP隔离
   - 确认MQTT Broker地址、端口正确，无防火墙/网络拦截
   - 检查所有设备的MQTT Client ID是否唯一，禁止重复ID接入

2. **外卖柜舵机不动作怎么办？**
   - 检查舵机接线引脚、供电是否正常，确认初始角度配置正确
   - 检查设备是否处于应急锁定状态，应急期间拒绝开锁指令
   - 查看Web面板设备状态，确认设备在线、MQTT连接正常

3. **MiniClaw飞书无回复怎么办？**
   - 检查ESP32-S3 WiFi连接是否正常，确认飞书机器人权限、密钥配置正确
   - 确认Website服务正常运行，接口地址配置无误
   - 检查MQTT客户端是否正常连接，主题订阅成功

4. **传感器I2C报错怎么办？**
   - 检查GroveHub扩展板是否插紧，模块接线无反接、虚接
   - 重启设备重新识别模块，确认I2C地址无冲突

---

## 🤝 贡献指南
本项目为高校课程毕业设计项目，欢迎提交Issue与PR优化：
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

---

## 📄 许可证
本项目基于 [MIT 许可证](sslocal://flow/file_open?url=LICENSE&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=) 开源，可自由使用、修改、分发，仅需保留原作者版权声明。

---

## 📁 仓库目录结构
```
aiot-smart-city-control-system/
├── README.md                           # 项目说明文档（本文件）
├── website-control-center/             # Website智慧管控平台
│   ├── app.py                          # Flask后端主程序
│   ├── requirements.txt                # Python依赖
│   └── templates/
│       └── index.html                  # Web可视化面板
├── miniclaw-esp32-terminal/            # MiniClaw智能体
│   ├── firmware/                       # ESP32-S3固件
│   └── 配置指南.md                      # 部署配置说明
├── takeaway-cabinet-device/            # 智能外卖柜终端
│   └── takeaway-control.py             # M5Go主程序
├── fire-emergency-device/              # 消防应急终端
│   └── emergency-control.py            # M5Go主程序
└── docs/                               # 项目文档
    ├── 系统架构图.png
    ├── 硬件接线指南.md
    └── 毕设答辩PPT模板.pptx
```
