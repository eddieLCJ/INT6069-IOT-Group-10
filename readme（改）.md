# 🏠 L-CASH: 基于大模型的认知型无障碍智能家居系统

> **L-CASH** (LLM-Empowered Cognitive & Adaptive Accessible Smart Home) 
> 🎓 本项目为香港教育大学 **INT6069 (Internet of Things)** 课程 2025/26 Semester 2 期末 Group Project 优秀设计方案。

![M5Stack](https://img.shields.io/badge/Hardware-M5GO_Kit-blue?logo=arduino)
![MQTT](https://img.shields.io/badge/Protocol-MQTT-green)
![Python](https://img.shields.io/badge/Backend-Python-yellow?logo=python)
![LLM](https://img.shields.io/badge/AI-LangChain_&_LLM-orange)

## 📖 目录 (Table of Contents)
- [项目简介](#-项目简介-about-the-project)
- [核心特性](#-核心特性-key-features)
- [系统架构](#-系统架构-system-architecture)
- [硬件清单](#-硬件清单-bill-of-materials)
- [团队分工](#-团队分工-team-roles)
- [快速开始](#-快速开始-getting-started)
- [课程评估优势](#-课程评估优势-assessment-highlights)

---

## 🌟 项目简介 (About The Project)
传统的智能家居系统多属于“被动响应式”（指令驱动）。L-CASH 致力于为独居老人、残障人士等需要特殊关怀的群体设计一款**具备主动感知与干预能力**的系统。

本项目利用 **M5GO 开发套件**作为分布式物理感知与执行节点，通过 **MQTT 协议**进行低延迟通信，并创新性地引入 **大语言模型 (LLM)** 作为中枢大脑，实现“多模态环境感知 -> 意图理解 -> 主动物理干预”的完整闭环。

---

## ✨ 核心特性 (Key Features)
- 🧠 **LLM 认知中枢 (Context-Aware AI):** 大模型实时订阅全屋多模态传感器数据，进行逻辑推理与主动决策，而非简单的闲聊。
- 🛡️ **无障碍与适老化 (Accessibility):** 结合 ToF 测距与手势识别，实现防跌倒监测与无接触式控制。
- ⚡ **分布式硬件协同 (Distributed IoT):** 4 个物理节点各司其职，涵盖安防入户、环境健康、物理执行与手动覆写。
- 📊 **全息数字孪生 (Digital Twin Web):** 提供实时传感器状态监控、数据可视化及大模型交互控制台。

---

## 🏗️ 系统架构 (System Architecture)

系统采用标准的物联网四层架构：
1. **感知与执行层:** 4 台 M5GO 终端配合指纹、ToF、空气质量等传感器矩阵。
2. **网络层:** 基于高并发、低延迟的 MQTT Broker 异步通信。
3. **认知决策层:** 以 LangChain 框架接入的 LLM 智能体。（架构暂定，等雪峰
4. **应用与控制层:** 响应式 Web 控制台界面。

### 📡 硬件节点分布
* **Node 1 (智能入户与安防):** RFID + 指纹识别 + 摄像头抓拍 + 舵机门锁。
* **Node 2 (环境健康卫士):** TVOC/eCO2 + 温湿度检测。
* **Node 3 (无障碍交互):** ToF (防跌倒/区域监测) + 手势识别 + 舵机(模拟窗户/风扇)。
* **Node 4 (手动覆盖中枢):** 土壤湿度监控 + 摇杆/按键 (全屋最高优先级物理控制权)。

---

## 🧰 硬件清单 (Bill of Materials)
基于 M5GO Development Kit:
- M5GO Base (x4)
- RFID Unit, Fingerprint Unit, M5Camera Unit
- TVOC/eCO2 Unit, ENV Sensor, Light Unit
- ToF Unit, Gesture Unit
- 360° Servo Kit (x2)
- Earth Moisture Unit, Joystick Unit, Color Unit

---

## 👥 团队分工 (Team Roles)
- **👨‍💻 硬件工程师 A & B (@YourGitHub_A, @YourGitHub_B):** 负责 M5GO 固件开发 (UIFlow/Arduino C++)，传感器驱动封装与 MQTT 报文发布/订阅逻辑。
- **🧠 AI 算法工程师 (@YourGitHub_C):** 负责 Python 后端架构，LangChain Prompt 工程，以及传感器多模态数据的语义解析与 LLM 决策流。
- **🌐 全栈开发工程师 (@YourGitHub_D):** 负责 MQTT Broker 部署，数据库设计，以及前端 Dashboard 实时数据可视化与交互界面开发。

---

## 🚀 快速开始 (Getting Started)

### 1. 硬件端部署 (Hardware)
1. 使用 M5Burner 为 4 台 M5GO 烧录相应的 UIFlow/MicroPython 固件。
2. 修改 `hw_nodes/` 目录下的配置文件，填入您的 Wi-Fi 账号密码及 MQTT Broker 地址。
3. 连接各 Unit 模块，通电运行。

### 2. 后端与 AI 部署 (Backend & LLM)
1. 进入后端目录：`cd backend`
2. 安装依赖：`pip install -r requirements.txt`
3. 配置环境变量 `.env`，填入大模型 API Key（如 OpenAI / 文心一言）及 MQTT 配置。
4. 启动服务：`python app.py`

### 3. 前端控制台部署 (Frontend Dashboard)
1. 进入前端目录：`cd frontend`
2. 安装依赖：`npm install`
3. 启动开发服务器：`npm run dev`

---

## 🏆 课程评估优势 (Assessment Highlights)
* **Authentic Problems:** 直接响应老龄化社会的无障碍家居痛点，具强烈社会价值。
* **Systems Integration:** 完美串联端、边、云、网、智，展现企业级 IoT 架构。
* **Originality:** 将 LLM for IoT（大模型驱动物联网）这一学术界前沿热点落地为真实原型。

---
*📝 本项目为香港教育大学 INT6069 课程作业，未经授权请勿用于商业用途。*
