# SDD-RIPER Light：Coding Agent 的控制面

[English](./README.md) | [简体中文](./README.zh-CN.md)

> Code is cheap. 真正昂贵的是上下文、控制和证据。
>
> 让模型负责推进事件，让人类负责目标、边界、权限、checkpoint、证据和验收。

强大的 Coding Agent 已经不再停留在给建议。它可以读取仓库、跨文件修改、调用工具、验证结果，并独立推动一个工程任务向前。当模型开始真正行动，瓶颈就从“能不能生成代码”转向了“任务是否始终对齐、过程是否可观察、结果是否可证明、失败后是否能恢复”。

SDD-RIPER 是为这个控制问题准备的一组轻量、项目原生的 Harness。它不是神奇 Prompt，也不是传统重型 SDD；它为强模型提供持久化工作面，同时避免把每个任务都变成流程表演。

| 人负责 | Agent 负责 | 项目沉淀 |
| --- | --- | --- |
| 目标、边界、权限、checkpoint、验收 | 探索、实现、迭代、工具调用 | spec、上下文索引、验证证据、恢复状态、可复用知识 |

从这里开始：[直接使用 Light Skill](./skills/sdd-riper-one-light/README.md) · [理解背后的判断](./docs/code-is-cheap.md) · [打开文档地图](./docs/README.md)

默认入口是 [`sdd-riper-one-light`](./skills/sdd-riper-one-light/SKILL.md)。当任务需要更强门禁、更高产物密度，或需要训练 / 审计级留痕时，再切到 [`sdd-riper-one`](./skills/sdd-riper-one/SKILL.md)。

本仓围绕四个互补 skill 组织：

- `sdd-riper-one-light` 和 `sdd-riper-one` 负责执行控盘、checkpoint、validation 和 reverse sync。
- `codemap` 把陌生代码整理成面向 agent 的上下文索引。
- `new-chat-ready` 为新对话、交接和长暂停保留可恢复上下文。

## 快速开始

日常 coding 或文档任务可以这样开：

```text
请使用 sdd-riper-one-light 处理这个任务。
先不要直接改文件。

请先给我：
- 你对任务的理解
- 本轮核心目标
- 最小 spec / summary
- Done Contract：什么算完成，由什么证明
- 下一步动作
- 风险
- 验证方式

我批准后再执行。
```

遇到陌生代码时，先建 CodeMap：

```text
请使用 codemap。
先创建 feature 级或 project 级代码地形索引，再进入计划。
重点关注入口、调用链、风险点、验证入口，以及下一步最小回读代码片段。
```

需要新对话交接时：

```text
请使用 new-chat-ready。
生成精简 resume pack。
先确认当前 agent 是否能直接创建 Codex 新对话。能创建就直接创建新对话并把精简续接 prompt 发过去；不能创建时再给我可直接粘贴的 fallback prompt。
同时扫描并整理可复用项目知识，避免未来新对话越来越臃肿；但不要默认提交 memory/spec/handoff 文件，除非我明确批准。
```

## Skill 怎么选

这四个 skill 共享同一个上下文原则：活跃上下文保持小，持久状态落到聊天外，需要决策时只按需读取最小切片。

| Skill | 适用场景 | 产物 |
| --- | --- | --- |
| [`sdd-riper-one-light`](./skills/sdd-riper-one-light/) | 日常 coding、文档、bugfix、普通重构、强模型协作 | 同一核心控制原语的低摩擦实现：最小 spec、checkpoint、validation、reverse sync |
| [`sdd-riper-one`](./skills/sdd-riper-one/) | 高风险、多文件重构、审计、训练、复杂交接 | 同一核心控制原语的重型实现：显式 RIPER 门禁、更完整 spec、更高产物密度、更强阻塞 |
| [`codemap`](./skills/codemap/) | 陌生代码库、遗留系统、大模块、跨仓任务 | 面向 agent 的代码地形索引 |
| [`new-chat-ready`](./skills/new-chat-ready/) | 新对话、resume pack、handoff、上下文压缩、恢复旧会话 | 精简 handoff、可选直接创建 Codex 新对话、续接 prompt、项目记忆同步扫描 |

## Agent 最小接入方式

对 Codex、Claude Code 或其他 agentic coding 环境，最小可用结构是：

```text
<repo>/
  AGENTS.md
  skills/
    codemap/
    new-chat-ready/
    sdd-riper-one-light/
    sdd-riper-one/
```

推荐默认规则：

- 项目级规则放在根目录 `AGENTS.md`。
- 个人或团队系统级默认规则放在系统 `AGENTS.md`，可参考 [`examples/global-agents.md`](./examples/global-agents.md)。
- 日常默认使用 `sdd-riper-one-light`。
- 陌生或大型代码改动前先用 `codemap`。
- 长暂停、上下文重置或交接前用 `new-chat-ready`。
- 高风险、审计、训练或需要更高产物密度的场景切到 `sdd-riper-one`。

## 核心工作流

```text
读上下文 -> 复述目标和风险 -> checkpoint -> 执行 -> 验证 -> 反向同步
```

Harness 保留少数硬规则：

- **Restate First**：计划或改文件前先复述任务。
- **No Spec, No Code**：实现前先形成或更新最小真相源。
- **No Approval, No Execute**：代码修改或高影响动作前等明确批准。
- **Done by Evidence**：完成必须由测试、日志、截图、人工验收或等价证据证明。
- **Reverse Sync**：把已验证结论按需回写到 spec、handoff、文档或项目记忆。

## Spec 与记忆边界

有三层东西，不要混写。

| 层级 | 用途 | 常见位置 |
| --- | --- | --- |
| Feature spec / handoff | 当前任务真相、决策、进度、验证、恢复状态 | `mydocs/specs/*`、`mydocs/handoff/*` 或项目约定 |
| Project knowledge / memory | 稳定事实、反复踩坑、可复用验证命令、项目级规则 | `PROJECT_KNOWLEDGE.md`、`PROJECT_SPEC.md`、`PROJECT_MEMORY.md`、`mydocs/project/*` 或 `AGENTS.md` 索引的文件 |
| 系统级默认规则 | 个人或团队通用 agent 路由和安全边界 | 系统 `AGENTS.md`、[`examples/global-agents.md`](./examples/global-agents.md) |

隐私边界：

- 知识拓扑由项目或人定义；SDD 只负责识别 `Project Sync Candidate`，并按 `AGENTS.md` 或用户明确指令分流。
- Agent 可以主动发现可复用知识，并提出 `Project Sync Candidate`。
- Agent 默认不得暂存或提交系统级知识、feature spec、handoff、项目记忆或用户偏好记忆。
- 只有用户明确要求提交，目标仓库合适，并且内容已按目标仓库脱敏确认后，才可以提交这些文件。

## 仓库卫生

这个仓库是公开、可复用的 agent workspace，提交前要保持干净：

- 不提交运行数据：`.agent-memory/`、`.expcap/`、SQLite、Milvus Lite、trace、episode、candidate、asset、本地缓存目录。
- 不提交 `.env`、凭据、token、API key、私有日志、个人路径或用户数据。
- 不为了强行提交本地运行产物而改 `.gitignore`。
- 示例提交前必须脱敏：保留问题形态和推理过程，移除私有名称、URL、ID、日志、密钥和用户数据。
- 使用 `expcap` 时优先放在用户缓存，例如 `EXPCAP_STORAGE_PROFILE=user-cache` 和 `EXPCAP_HOME="$HOME/.expcap"`。

## 多仓库任务

前后端联动或微服务任务里，不要让模型一次性吞掉所有仓库。

先建立 Project Registry：

```text
MULTI / 多项目

当前 workspace 下有多个仓库。
请先发现项目，生成 Project Registry。
不要一次性读取所有代码。
先判断主项目、相关项目、active_project 和 change_scope。
默认 local；需要跨项目修改时先 checkpoint，等我批准。
```

完整规则见 [`skills/sdd-riper-one/references/multi-project.md`](./skills/sdd-riper-one/references/multi-project.md)。

## 仓库地图

| 路径 | 作用 |
| --- | --- |
| [`AGENTS.md`](./AGENTS.md) | 本仓项目级 agent 规则 |
| [`examples/global-agents.md`](./examples/global-agents.md) | 系统级 / 个人级 `AGENTS.md` 模板 |
| [`skills/sdd-riper-one-light`](./skills/sdd-riper-one-light/) | 日常默认 Harness |
| [`skills/sdd-riper-one`](./skills/sdd-riper-one/) | 严格控盘协议 |
| [`skills/codemap`](./skills/codemap/) | 代码地形索引 skill |
| [`skills/new-chat-ready`](./skills/new-chat-ready/) | 新对话交接与项目记忆同步 skill |
| [`docs/README.md`](./docs/README.md) | 文档地图与阅读路径 |
| [`protocols/`](./protocols/) | 早期协议参考 |

## 阅读路径

最短可用路径：

1. 读 [`skills/sdd-riper-one-light/README.md`](./skills/sdd-riper-one-light/README.md)。
2. 用快速开始模板跑一个真实任务。
3. 陌生代码先用 [`codemap`](./skills/codemap/SKILL.md)。
4. 需要强门禁时读 [`skills/sdd-riper-one/README.md`](./skills/sdd-riper-one/README.md)。
5. 需要长文再看 [`docs/README.md`](./docs/README.md)。

当前长文只保留三个定位互补的入口。维护中的完整索引见[文档地图](./docs/README.md)。

| 文档 | 核心问题 |
| --- | --- |
| [Code is cheap. Don't write any.](./docs/code-is-cheap.md) | 为什么代码变廉价后，工程价值会转向目标、上下文、checkpoint、验收与风险控制 |
| [手把手学会 AI Coding Harness](./docs/ai-coding-harness-guide.md) | 如何切任务、控上下文、用 codemap、验收输出、留下可恢复状态 |
| [为什么通用 Agent 是饮鸩止渴](./docs/general-purpose-agents-are-a-trap.md) | 为什么具体能力、显式 Flow、业务接口和必要的 hardcode 往往比模糊的通用能力更可靠 |

## 核心判断

真正重要的不是把 AI 管成更听话的代码助手。

真正重要的是：承认模型已经可以推进事件，然后为这种主体性建立控制面。

这就是 SDD-RIPER Light 的目的。
