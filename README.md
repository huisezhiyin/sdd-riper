# SDD-RIPER Light: AI Agent Harness

> 让大模型成为事件推进的主体，让人类成为控盘者。
> 不再先挖好每一条水渠，而是让水先漫溢、找到河道；人类跟着水势调整位置，在关键处设闸、验收、开垦。

---

## 30 秒读懂

**SDD-RIPER** 不是传统意义上的重型 SDD。

传统 SDD 往往把 Spec 当成模型的操作系统：先写完整蓝图，再要求模型按图施工。
这里的 SDD 更轻，也更贴近大模型时代：**Spec 首先是给人看的最小真相源**，用于记录目标、边界、决策、验证和可恢复上下文。

这个仓库的主推入口是 [`sdd-riper-one-light`](./skills/sdd-riper-one-light/SKILL.md)。

它不是“简化版”，而是面向强模型的日常 **AI Agent Harness**：

- 让模型自己分解、探索、试错和推进。
- 让人类控制方向、边界、节奏和验收。
- 用最小 Spec、Checkpoint、Approval、Validation、Reverse Sync 把非确定性模型纳入可观察、可回退、可接手的轨道。

一句话：

> **AI 是事件主体，Human 是控盘者，Harness 是控制面。**

---

## 思维转变

### 从挖水渠到跟着河道开垦

非大模型时代，人类更像是在挖水渠：先设计路径，再把水引到自己的田地里。

大模型时代，水本身有了流动能力。更好的方式不是提前挖死每一条渠，而是让水先漫溢、探索、自己找到河道。人类要做的是跟着水势调整自己的方向和位置，在关键处设闸、筑堤、验收，并沿着已经形成的河道开垦田地。

这就是 Light Harness 和传统重流程的区别：

| 范式 | 人的角色 | 模型的角色 | 控制方式 |
| --- | --- | --- | --- |
| 传统软件工程 | 预设路径的人 | 工具 | 流程、规范、代码审查 |
| 传统重 SDD | 写蓝图的人 | 按图施工者 | 大 Spec、阶段门禁 |
| SDD-RIPER Light | 跟水势调整位置的控盘者 | 探索河道的主体 | Checkpoint、证据、回写 |

### 从助手到事件主体

强模型不再只是“帮我补代码”的助手。它会提出方案、尝试路径、暴露风险、推动任务向前流动。

这更像骑手和马的关系。马不是被动工具；在赛道上，马的速度、力量和判断才是主力。骑手不替马迈腿，骑手负责选赛道、控节奏、看风险、给信号、判输赢。

`sdd-riper-one-light` 承认这种主体性：让模型成为主力，让人类成为控盘者。Harness 不是把马绑在旧流程里，而是让人和模型在同一条赛道上协作，并且始终可观察、可设闸、可验收、可复用。

---

## 默认入口：sdd-riper-one-light

日常 coding / agentic coding，默认使用：

[`skills/sdd-riper-one-light/SKILL.md`](./skills/sdd-riper-one-light/SKILL.md)

它保留的硬门禁很少，但都很关键：

- **Restate First**：先复述任务理解，避免一开始就跑偏。
- **Core Goal as Loop Anchor**：每一轮都有当前核心目标。
- **No Spec, No Code**：先有最小真相源，再改代码。
- **No Approval, No Execute**：执行前必须有 checkpoint 和批准。
- **Done by Evidence**：完成不是模型自称完成，而是由测试、日志、人工验证等证据证明。
- **Reverse Sync**：把已经验证的结论回写，留下下一轮可恢复的锚点。

最小启动模板：

```text
请使用 sdd-riper-one-light 处理这个任务。
先不要直接改代码。

请先给我：
- 你对任务的理解
- 本轮核心目标
- 最小 spec / summary
- Done Contract：什么算完成、由什么证明
- 下一步动作
- 风险
- 验证方式

我批准后再执行。
```

---

## 旧时代也能用：标准控盘入口

[`sdd-riper-one`](./skills/sdd-riper-one/SKILL.md) 不是废弃版本。

它更重、更显式，适合这些场景：

- 团队刚开始建立 AI 编程纪律。
- 模型能力不稳定，需要更强下限。
- 复杂重构、跨项目联动、长期交接。
- 需要完整 `Research -> Plan -> Execute -> Review` 阶段审计。
- 组织还没有准备好直接把模型当事件主体来协作。

换句话说：

- **新时代的人**：默认用 `sdd-riper-one-light`，释放模型的探索能力。
- **旧时代的人**：可以从 `sdd-riper-one` 进入，用更显式的流程获得安全感。
- **高风险任务**：即使在新时代，也可以临时切回标准控盘协议。

---

## 这个仓库有什么

| 资产 | 定位 |
| --- | --- |
| [`skills/sdd-riper-one-light`](./skills/sdd-riper-one-light/) | 主推 Light Harness，日常默认入口 |
| [`skills/sdd-riper-one`](./skills/sdd-riper-one/) | 标准控盘协议，训练、审计、交接和复杂任务入口 |
| [`protocols/SDD-RIPER-ONE.md`](./protocols/SDD-RIPER-ONE.md) | 标准协议原文 |
| [`protocols/RIPER-DOC.md`](./protocols/RIPER-DOC.md) | 文档生成与维护协议 |
| [`protocols/RIPER-5.md`](./protocols/RIPER-5.md) | 更早期、更严格的 RIPER 参考 |
| [`docs/团队落地指南.md`](./docs/团队落地指南.md) | 团队推广与治理指南 |
| [`docs/如何快速从零开始落地大模型编程 -- 手把手教程.md`](./docs/如何快速从零开始落地大模型编程%20--%20手把手教程.md) | 从零上手教程 |

---

## 读法建议

如果你已经在使用强模型：

1. 先读 [`sdd-riper-one-light`](./skills/sdd-riper-one-light/README.md)。
2. 直接用最小启动模板跑一个真实任务。
3. 遇到复杂任务，再补读 [`sdd-riper-one`](./skills/sdd-riper-one/README.md)。

如果你在团队里推广：

1. 先让团队默认安装 Light Harness。
2. 给高风险任务保留标准控盘入口。
3. 用 [团队落地指南](./docs/团队落地指南.md) 统一规则：代码修改前先 checkpoint，批准后再执行。

如果你关心思想背景：

| 文档 | 核心问题 |
| --- | --- |
| [从传统编程转向大模型编程](./docs/从传统编程转向大模型编程.md) | 为什么人的身份要迁移 |
| [AI 原生研发范式](./docs/AI%20原生研发范式：从"代码中心"到"文档驱动"的演进.md) | 为什么 Spec 首先是给人看的工程资产 |
| [团队落地指南](./docs/团队落地指南.md) | 如何让团队从个人技巧变成组织能力 |

---

## 核心判断

大模型时代，真正重要的不是把 AI 管成一个更听话的代码助手。

真正重要的是：**承认模型已经成为事件推进的主体，然后为这种主体性建立控制面。**

`sdd-riper-one-light` 做的不是减少控制，而是把控制从“预设每一步”移动到“关键节点设闸”。
这就是 Harness Engineering 的意义。
