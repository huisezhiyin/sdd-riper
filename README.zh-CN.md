# SDD-RIPER Light: AI Agent Harness

[English](./README.md) | [简体中文](./README.zh-CN.md)

> 让大模型成为事件推进的主体，让人类成为控盘者。
> 不再先挖好每一条水渠，而是让水先漫溢、找到河道；人类跟着水势调整位置，在关键处设闸、验收、开垦。

---

## 30 秒读懂 Harness

**Harness** 不是一套要求模型逐步照做的律令，而是把一个可验证的任务单元交给大模型自主推进；人类只维护目标、边界、权限、上下文、checkpoint 和验收证据。

它要解决的不是“怎么写一个神奇 Prompt”，而是四个工程问题：

| 问题 | Harness 的回答 |
| --- | --- |
| 任务怎么交出去 | 切成模型能独立推进的最小混沌单元 |
| 过程怎么不失控 | 人在关键节点 checkpoint，而不是逐行遥控 |
| 完成怎么判断 | 用测试、日志、截图、人工验收等证据证明 |
| 下次怎么接上 | 用最小 spec / summary / handoff 留下可恢复上下文 |

所以这里的核心很简单：

```text
人负责目标、边界、节奏、风险和验收；
模型负责探索、实现、修复和推进；
spec 是持久化真相源，不是反复塞满上下文的大 prompt。
```

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

日常任务用 `sdd-riper-one-light`：轻提示、中度留痕、checkpoint、validation、reverse sync。

复杂任务、高风险任务、新手训练、审计交接用 `sdd-riper-one`：更明确的阶段门禁、codemap / context、完整 spec、更多问询与阻塞。

陌生项目、老项目、大模块或跨仓任务，先用 [`codemap`](./skills/codemap/SKILL.md) 建代码地形索引。它的目的不是写一份给人看的架构长文，而是让 Agent 知道入口、调用链、风险点、验证入口和下一步该回读哪一小片代码。

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

## Agent 最小接入方式

如果你是在 Claude、Codex 或其他 agentic coding 环境里使用，最小但已经很好用的一套就是：

```text
<repo>/
  AGENTS.md
  skills/
    codemap/
    new-chat-ready/
    sdd-riper-one-light/
    sdd-riper-one/
```

- `AGENTS.md` 放在仓库根目录，承载工作区默认规则。
- `sdd-riper-one-light` 和 `sdd-riper-one` 放在 `skills/` 目录。
- `codemap` 作为代码地形索引 Skill，优先用于陌生代码库、老项目、大模块和跨仓任务。
- `new-chat-ready` 用于新对话交接、resume pack、可直接粘贴的续接 prompt，以及必要的项目级 Markdown 记忆同步。
- 日常默认使用 `sdd-riper-one-light`。
- 重构、审计、交接和高风险任务切到 `sdd-riper-one`。
- 系统级 / 个人级默认规则可参考 [`examples/global-agents.md`](./examples/global-agents.md)。

凡是能读取仓库内规则和本地 skill 目录的 agent 环境，基本都可以用这套结构；Codex 只是其中一种。

实际使用时，通常一句话就够：

```text
请启用 $sdd-riper-one-light。
先不要直接改代码。
先给我任务理解、本轮核心目标、最小 spec / summary、风险和验证方式。
```

## 仓库卫生

这个仓库默认面向公开、可复用的 agent workspace。

- 不要提交运行数据：`.agent-memory/`、`.expcap/`、SQLite 文件、Milvus Lite 数据、trace、episode、candidate 和 asset。
- 使用 `expcap` 时默认采用 `EXPCAP_STORAGE_PROFILE=user-cache` 和 `EXPCAP_HOME="$HOME/.expcap"`。
- 不要提交个人 home 目录等机器特定路径。
- 文档提交前要脱敏：移除私有项目名、内部链接、凭据、日志、ID 和用户数据。
- 下载副本文件如 `name (1).md` 提交前先改名；未改名时保持忽略。

## 多仓库 / 临时 Workspace 怎么用

微服务、前后端联动、多仓库临时 workspace 下，核心问题不是 chat 开在哪里，而是**上下文如何被切片、聚焦、切换和收束**。

常见有三种方式：

- **在主项目里开 chat**：如果任务主要落在一个仓库，比如 `order-service`，就在这个仓库里启动；其他仓库按需让 Agent 探索、读取接口契约或调用链，再把结论带回当前任务。
- **在父目录开 chat**：如果任务天然跨仓，比如前后端接口一起改、多个微服务协议联动，就在父 workspace 启动，让 Agent 先生成 `Project Registry`，再按项目切片阅读和执行。
- **拆成多个单仓任务**：如果各仓库改动边界清楚，只是发布或联调相关，可以拆成多个单仓任务，最后做契约对齐和回归。

推荐规则：

- 父目录可以作为入口，但不要让模型一次性吞掉所有仓库。
- 单仓可以作为入口，但跨仓信息要显式引入。
- 多仓任务先建立 `Project Registry`，记录项目路径、职责、相关性和当前 `active_project`。
- 默认 `change_scope=local`；跨项目 checkpoint 或准备跨仓改文件前，先声明 `active_project` / `active_workdir` 并等待确认。
- 只有明确需要跨仓修改时，才进入 `CROSS / 跨项目`。
- 每个相关项目都应该有自己的 CodeMap；跨项目时再补一层接口契约或链路摘要。

最小启动示例：

```text
MULTI / 多项目

当前 workspace 下有多个仓库。
请先自动发现项目，生成 Project Registry。
不要一次性读取所有代码。
先判断本次任务的主项目、相关项目、active_project 和 change_scope。
默认 local；需要跨项目修改时先 checkpoint，等我批准。
```

更完整的多项目规则见 [`skills/sdd-riper-one/references/multi-project.md`](./skills/sdd-riper-one/references/multi-project.md)。当前 `create_codemap` 可作为 SDD-RIPER 的 Pre-Research 入口；独立 [`codemap`](./skills/codemap/SKILL.md) skill 负责用固定模板统一不同模型的 CodeMap 输出口径。

---

## 需要显式流程时：标准控盘入口

[`sdd-riper-one`](./skills/sdd-riper-one/SKILL.md) 不是废弃版本。

它更重、更显式，适合这些场景：

- 团队刚开始建立 AI 编程纪律。
- 模型能力不稳定，需要更强下限。
- 复杂重构、跨项目联动、长期交接。
- 需要完整 `Research -> Plan -> Execute -> Review` 阶段审计。
- 组织还没有准备好直接把模型当事件主体来协作。

换句话说：

- **熟练用户 / 强模型日常任务**：默认用 `sdd-riper-one-light`，释放模型的探索能力。
- **新手、训练、审计、交接或低质量模型场景**：从 `sdd-riper-one` 进入，用更显式的流程获得下限。
- **高风险任务**：即使熟练用户也可以临时切回标准控盘协议。

---

## 这个仓库有什么

| 资产 | 定位 |
| --- | --- |
| [`skills/sdd-riper-one-light`](./skills/sdd-riper-one-light/) | 主推 Light Harness，日常默认入口 |
| [`skills/sdd-riper-one`](./skills/sdd-riper-one/) | 标准控盘协议，训练、审计、交接和复杂任务入口 |
| [`skills/codemap`](./skills/codemap/) | 代码地形索引 Skill，用 feature / project CodeMap 节约上下文注意力 |
| [`skills/new-chat-ready`](./skills/new-chat-ready/) | 新对话交接 Skill，生成可恢复 handoff、续接 prompt，并按需同步项目级 Markdown 记忆 |
| [`examples/global-agents.md`](./examples/global-agents.md) | 系统级 / 个人级 `AGENTS.md` 模板，包含默认 skill 路由和安全边界 |
| [`protocols/SDD-RIPER-ONE.md`](./protocols/SDD-RIPER-ONE.md) | 标准协议原文 |
| [`protocols/RIPER-DOC.md`](./protocols/RIPER-DOC.md) | 文档生成与维护协议 |
| [`protocols/RIPER-5.md`](./protocols/RIPER-5.md) | 更早期、更严格的 RIPER 参考 |
| [`docs/README.md`](./docs/README.md) | 文档阅读地图：当前主线与归档文章 |
| [`docs/手把手学会 AI Coding Harness：从任务拆分到上下文控盘.md`](./docs/手把手学会%20AI%20Coding%20Harness：从任务拆分到上下文控盘.md) | 对外主文：用两个真实开源项目讲任务拆分、上下文控盘、codemap、目标驱动执行、验收与留痕 |
| [`docs/团队落地指南.md`](./docs/团队落地指南.md) | 团队推广与治理指南 |

---

## 读法建议

如果你已经在使用强模型：

1. 先读 [`sdd-riper-one-light`](./skills/sdd-riper-one-light/README.md)。
2. 直接用最小启动模板跑一个真实任务。
3. 遇到陌生老项目或大模块，先用 [`codemap`](./skills/codemap/SKILL.md) 建代码地形索引。
4. 遇到复杂任务，再补读 [`sdd-riper-one`](./skills/sdd-riper-one/README.md)。

如果你在团队里推广：

1. 先让团队默认安装 Light Harness。
2. 给高风险任务保留标准控盘入口。
3. 用 [团队落地指南](./docs/团队落地指南.md) 统一规则：代码修改前先 checkpoint，批准后再执行。

如果你关心思想背景，先从文档地图进入，不需要把所有历史长文都读一遍：

| 文档 | 核心问题 |
| --- | --- |
| [文档阅读地图](./docs/README.md) | 哪些是当前主线，哪些是历史归档 |
| [手把手学会 AI Coding Harness](./docs/手把手学会%20AI%20Coding%20Harness：从任务拆分到上下文控盘.md) | 如何用真实项目学会切任务、控上下文、使用 codemap、引导模型、验收结果，并把 SDD-RIPER 变成默认 skill |
| [团队落地指南](./docs/团队落地指南.md) | 如何让团队从个人技巧变成组织能力 |
| [Claude Code 源码拆解](./docs/Claude%20Code%20源码拆解：从启动到多%20Agent%20扩展层.md) | 从真实 agent runtime 看 Harness 设计 |

更早期的长文已经集中放到 [`docs/archive/`](./docs/archive/)，作为历史思考和写作素材保留。

---

## 核心判断

大模型时代，真正重要的不是把 AI 管成一个更听话的代码助手。

真正重要的是：**承认模型已经成为事件推进的主体，然后为这种主体性建立控制面。**

`sdd-riper-one-light` 做的不是减少控制，而是把控制从“预设每一步”移动到“关键节点设闸”。
这就是 Harness Engineering 的意义。
