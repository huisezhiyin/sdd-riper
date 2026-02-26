# ⚡️ SDD-RIPER: AI-Native Development Protocol

> **The Constitution for Human-AI Collaboration.**
> 像指挥军团一样指挥 AI，而不是像保姆一样修补代码。

---

## 📖 30秒读懂 SDD-RIPER

**SDD (Spec-Driven Development)** 是一套为大模型编程量身定制的研发协议。它将程序员的角色从“代码产出者”重定义为**“意图定义者”**。

### 核心公式

> **Spec (Truth) + AI (Execute) = Software 2.0**

### ⚡️ 为什么你需要它？

| 🚫 痛点 (Without SDD) | ✅ SDD 解法 |
| --- | --- |
| **上下文腐烂**：AI 聊着聊着就忘了前文约束，破坏旧逻辑。 | **Spec 锚点**：强制 AI 每次行动前读取 Protocol，状态永久“满血”。 |
| **审查瘫痪**：AI 秒生成 500 行代码，人类根本 Review 不过在这里。 | **RIPER Loop**：先审 Plan 再写 Code。**审逻辑代替审代码**。 |
| **不可维护**：全是 AI 生成的陌生代码，两周后不敢动。 | **文档即源码**：代码是消耗品，Spec 才是资产。修 Bug 先修文档。 |

---

## 🔄 The RIPER Loop (标准作业流)

我们强制 AI 遵循以下五步状态机，拒绝“一发入魂”的幻觉代码：

```mermaid
graph LR
    R[🔍 Research<br>调研/事实锁定] --> I[💡 Innovate<br>方案设计]
    I --> P[📝 Plan<br>原子级规划]
    P -->|Human Sign-off| E[🚀 Execute<br>按图施工]
    E --> V[👀 Review<br>反向验收]
    V -->|Fix Spec| P

```

1. **Research**: 拒绝瞎猜，先查代码库现状。
2. **Innovate**: 审讯式设计，寻找最优解。
3. **Plan**: **核心环节**。输出详细步骤，人类批准后才准动手。
4. **Execute**: 无脑执行，不仅是 Coder，更是 Builder。
5. **Review**: AI 自查 + 生成验收报告。

---

## 📂 协议资产清单

| 协议文件 | 适用场景 | 对应模型建议 |
| --- | --- | --- |
| [`SDD-RIPER-ONE.md`](./protocols/SDD-RIPER-ONE.md)  | **标准版**：主力协议，包含完整闭环。 | Claude 3.5 / GPT-4o / Qwen 2.5 |
| [`RIPER-DOC.md`](./protocols/RIPER-DOC.md)  | **文档专家**：专门用于生成 README/API 文档。 | DeepSeek V3 / Gemini Pro |
| [`RIPER-5.md`](./protocols/RIPER-5.md) | **严格版**：上一代状态机，适合复杂逻辑重构。 | o1 / o3-mini |

---

## 📚 深度阅读 (Deep Dive)

* 🧠 **思维转型**: [从传统编程转向大模型编程](./docs/从传统编程转向大模型编程.md)  - 如何从工匠变为建筑师。
* 📜 **理论体系**: [AI 原生研发范式](./docs/AI%20原生研发范式：从“代码中心”到“文档驱动”的演进.md)  - 为什么 Spec 是新时代的源代码。
