# 🤖 MiniClaw 智能体：ESP32‑S3 飞书交互实现综述
**适用于 GitHub README，简洁、专业、零基础可看懂**

---

## 1. 项目概述
MiniClaw 是一款**纯嵌入式轻量级 AI 智能体框架**，可直接跑在 **ESP32‑S3** 芯片上，**不需要 Linux、不需要树莓派、不需要服务器**，超低功耗（约 0.5W）7×24 小时稳定运行。

本项目实现：
**ESP32‑S3 ←→ 飞书机器人 ←→ 大模型（DeepSeek）**
完整的**自然语言对话 + 指令理解 + 硬件控制**闭环。

---

## 2. 核心能力（一句话总结）
- 在 **ESP32‑S3** 上运行完整 AI Agent（ReAct 逻辑）
- 通过 **飞书** 收发消息，**内网也能用**（WebSocket 长连接）
- 对接 **DeepSeek** 大模型做意图理解
- 支持**语音/文字指令 → AI 解析 → 控制硬件**
- 可直接接入你的智慧城市 IoT 系统

---

## 3. 整体架构
```
飞书客户端
      ↓↑（WebSocket 长连接）
ESP32‑S3（MiniClaw 智能体）
      ↓↑（HTTP / MQTT）
Website 中控大脑 / 硬件设备（外卖柜、消防）
```

---

## 4. 技术实现流程
### 4.1 硬件
- 主控：**ESP32‑S3**（双核 240MHz / 8MB PSRAM）
- 供电：USB 5V
- 网络：WiFi 802.11b/g/n（2.4G）

### 4.2 软件栈
- 框架：**MiniClaw（C 语言 / FreeRTOS）**
- 通信：**飞书 WebSocket 长连接**
- 大模型：**DeepSeek API**
- 编译环境：**ESP-IDF 5.5+**

### 4.3 飞书交互流程
1. 用户在飞书发消息
2. 飞书通过 **WebSocket 长连接**推送给 ESP32‑S3
3. MiniClaw 接收消息 → 送给 DeepSeek 理解意图
4. AI 决策 → 生成指令（如“打开外卖柜”）
5. 通过 **HTTP/MQTT** 发给中控或硬件
6. 执行结果返回 → 飞书回复用户

---

## 5. 飞书接入关键配置
### 5.1 飞书开放平台步骤
1. 创建**企业自建应用**
2. 添加**机器人能力**
3. 开通权限：
   - `im.message:read`
   - `im.message:send_as_bot`
   - `im.message.receive_v1`
4. 事件订阅使用 **长连接（WebSocket）**
5. 获取：
   - AppID
   - AppSecret

### 5.2 MiniClaw 配置
修改 `mimi_secrets.h`：
```
FEISHU_APP_ID
FEISHU_APP_SECRET
```

修改 `mimi_config.h`：
```
#define MIMI_FEISHU_ENABLED 1
```

---

## 6. 与你们 IoT 系统的对接方式
**完全兼容你们现有架构：**
- MiniClaw **不直接控制硬件**
- 只通过 **HTTP** 访问 Website 中控
- 或通过 **MQTT** 发布指令
- 所有指令统一由中控下发 → 安全、无冲突

---

## 7. 本项目优势（适合写进 GitHub）
- ✅ **超轻量**：仅 ESP32‑S3 即可跑完整 AI 智能体
- ✅ **国内友好**：飞书 + DeepSeek，无需代理
- ✅ **内网可用**：WebSocket 长连接，不用公网 IP
- ✅ **低功耗**：0.5W，可长期在线
- ✅ **稳定可靠**：C 语言裸机运行，不崩溃
- ✅ **高度兼容**：可直接接入 MQTT 物联网系统

---

## 8. 一句话总结（可直接放项目首页）
> MiniClaw 让 ESP32‑S3 成为一个能飞书对话、AI 思考、控制硬件的嵌入式智能体，无需服务器、无需 Linux，开箱即用，完美适配 AIoT 毕业设计与物联网项目。

搭建可参考：https://mp.weixin.qq.com/s/oFV4537SysFUv1vESNXoSg?scene=1
---

如果你愿意，我可以**再帮你压缩成 3 行超短版本**，直接放在 GitHub 项目顶栏展示。当前文件内容过长，豆包只阅读了前 91%。
