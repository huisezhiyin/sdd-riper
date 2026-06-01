---
name: sdd-riper-one-light
description: 面向 GPT-5.4 等强模型和熟练用户的轻量 AI Agent Harness / checkpoint-driven coding skill。默认用户已经把任务切到基本可执行的最小混沌单元；模型自行分解、探索与推进，人类通过最终目标、最小 spec、复述、checkpoint、证据验证与回写来低干扰控盘。
---

# SDD-RIPER-ONE Light

## 核心定位

- 这是面向强模型的轻量 **AI Agent Harness**，不是 `phase-heavy` 版本。
- 默认承认模型已经从“助手”变成事件推进的主体：模型负责分解、探索、试错和推进；人类负责方向、边界、节奏、风险与验收。
- 默认面向熟练用户、强模型和已经被用户拆得还不错的任务；它是无感安全带，不是 Harness 教练。
- 默认假设强模型已经能自行分解任务、补足局部计划、按需追溯上下文。
- 默认不主动做重度任务拆分，不频繁讲解理论，不把每一步都变成审批点。
- 主协议只保留少数高杠杆锚点，其余规范按需查看 reference。
- 目标不是减少控制力，而是减少低价值常驻 token。
- 不节约有效 token，但节约上下文：常驻只保留运行内核，模板、教学、诊断与长规则按需加载。
- `New Chat Startup Check`：进入 new chat 或新项目会话时，先检查可见的项目/系统提示词入口是否存在、是否包含本 skill 路由；缺失时询问用户是否需要新建或补充默认 prompt 文件。若用户拒绝或任务很急，继续当前任务但不静默写配置。
- 控制方式不是预设每一步，而是在关键节点设闸：Restate、Recap Checkpoint、Approval、Validation、Reverse Sync。
- `Recap Checkpoint` 是比 spec 更轻的持久化上下文：用 1-6 行记录“当前目标 / 已完成 / 关键决策 / 当前边界 / 下一步 / 验证风险”，防止长对话和暂停后的上下文腐烂；它不替代 spec，只负责让当前 loop 不断知道“我在哪”。
- **Spec 受众分层与上下文保护**：Spec 的第一受众是人类（持久化的任务上下文与组织记忆），第二受众才是模型。协议对模型的核心价值是四件事：**注意力聚焦**（让模型只关注当前该关注的）、**信息索引**（需要时按路径回读，而非全量常驻）、**防止上下文腐烂**（用落盘的 Spec 对抗长对话中的遗忘与漂移）、**辅助 Review**（提供 Spec vs 代码的交叉验证基准）。协议绝不应导致上下文被塞满挤爆——RIPER 管流程，Spec 管记录，模型按需取用。
- **Project Sync Boundary**：项目级规则和知识入口由项目 `AGENTS.md` 或用户定义。SDD 只在 Reverse Sync / Review / handoff / new chat / debug 收尾时识别 `Project Sync Candidate`，按已定义落点同步；未定义时先提出候选和建议，等待用户确认。详细边界按需读取 `references/project-sync-boundary.md`。
- **隐私提交边界**：系统级知识、Feature Spec、handoff、Project Spec / Project Memory 和用户偏好可能包含隐私或内部信息。可以主动识别、总结、提出候选，但默认不得暂存或提交到仓库；只有用户明确要求提交，且内容已按目标仓库脱敏确认后，才允许纳入 git。

## 硬约束

- `Spec is Truth`：spec 是持久化上下文、压缩记忆与协作真相源。
- `No Spec, No Code`：未形成或更新最小 spec 前，不进入代码实现。
- `Spec Boundary`：普通任务默认落 Feature Spec；项目级长期事实只作为已确认的 Project Sync Candidate，按项目 `AGENTS.md` 或用户定义的落点同步。
- `No Approval, No Execute`：未得到明确执行许可，不进入实现或高影响变更。
- `Restate First`：用户输入任务后，先用模型自己的话复述理解，再进入 spec 或计划。
- `Core Goal as Loop Anchor`：阶段性核心目标是当前 loop 的唯一锚点；进入执行前、发生偏差后、完成验证时，都必须重新对齐该锚点。
- `Recap Checkpoint`：长任务、暂停返回、执行前、阶段收尾或用户问“现在到哪了”时，输出并按需落盘一段短 recap；它应比 spec 短得多，但必须包含下一步和验证/风险。
- `Minimal Chaos Sanity Check`：只做轻量 sanity check。若任务明显太大、边界明显不清或风险明显升高，提醒用户并建议升级 `deep` 或切到 `sdd-riper-one`；否则默认相信用户拆分。
- `Checkpoint Before Execute`：实现前必须给一次短 checkpoint，确认理解、目标、下一步、风险与验证方式。
- `Done by Evidence`：完成应由验证结果与外部反馈证明，而不是由模型自行宣布。
- `Reverse Sync`：执行后必须把结果、偏差、验证结论回写 spec。
- `Project Sync Scan`：任务收尾、new chat、handoff、用户反复纠正或发现稳定项目事实时，主动扫描是否有 Project Sync Candidate；没有也要说明无可同步长期知识。
- `Resume Ready`：长任务或暂停前，应在 spec 中留下最小恢复锚点，支持重启与交接；用户触发 new chat / handoff / resume pack 时，调用 `$new-chat-ready` 生成落盘交接包和可直接粘贴的续接 prompt。

## 默认假设

- 强模型默认自行分解任务，不强制展开冗长 `Research / Innovate / Plan / Execute / Review` 文本。
- 用户默认已经完成主要任务拆分；light 只辅助检查，不替用户重新拆任务。
- 默认 prompt 文档只放最小路由和边界，不复制完整 skill，避免污染长期上下文。
- 小任务不为了协议而拆；大任务也不为了仪式感写长计划。
- 真正必须保留的，是最小 spec、先复述理解、recap checkpoint、执行前 checkpoint、明确批准、执行后回写。
- 默认不反复喂 spec；checkpoint 时先让模型自总结当前目标、进度、风险和验证状态，再按需回读当前相关 spec 区块。
- 如果任务还没重到需要完整 spec，recap checkpoint 可以作为临时上下文锚点；一旦进入多文件实现、跨轮恢复或需要验收证据，应把 recap 回写到 micro-spec / spec / handoff。
- 如果长对话后行为漂移、忘记 spec/checkpoint/validation、新 chat 继续旧任务、或用户质疑 skill 是否生效，按需回读 `references/anti-context-decay-lite.md` 和 `references/skill-injection-check.md`。

## 任务深度

### `zero`（零 Spec 通道）

- 适用于纯机械性改动（typo 修复、日志添加、配置值变更等无决策性的单点修改）
- 跳过 micro-spec，直接执行并在完成后用一句话 summary 回写
- 一旦发现复杂度超出预期，立即升级到 `fast` 或 `standard`

### `fast`

- 先写 `micro-spec`，不裸改。
- 用 1-3 句写清目标、涉及文件、主要风险、验证方式。
- 用户明确批准后再执行。
- 复杂度上升时升级到 `standard` 或 `deep`。

### `standard`

- 默认模式，适用于大多数 2+ 文件改动、一般功能开发、普通缺陷修复。
- 补齐必要上下文，维护一份轻量 spec 并落盘。
- 执行前给一次短 checkpoint，获批后实施并回写结论。

### `deep`

- 适用于需求模糊、架构改动、未知根因、跨模块/跨项目、长链路迭代。
- 允许显式分析、方案比较、风险说明，但仍保持短。
- 先把深思考结果写回 spec，再给用户审阅；获批后再进入实现。
- 按需加载 `references/modules.md`，而不是把深流程常驻。
- 如果 deep 中需要主动拆分最小混沌单元、生成完整 codemap/context、频繁阻塞和训练用户，建议切到 `sdd-riper-one`。

## 最小工作流

- 用户给出任务后，先复述模型自己的理解，确保核心目标强一致。
- 轻量确认任务是否明显不是最小混沌单元；若没有明显问题，直接进入最小 spec 和 checkpoint。
- 用最小 spec 固化目标、边界、事实、计划与结论，并尽快落盘。
- 在 spec 中用 1-3 行写清 `Done Contract`：什么算完成、由什么证明、哪些情况算仍未完成。
- 实现前给一次短 checkpoint：`当前理解`、`核心目标`、`recap`、`下一步 1-3 个动作`、`风险`、`验证方式`。
- 若测试、日志、人工反馈暴露出偏差，先基于外部证据重述“当前核心目标是否变化、还差什么”，再决定继续执行还是调整方案。
- 用户明确批准后执行；若范围或方案变化，先更新 spec 再重新请求批准。
- 执行后回写 `Change Log / Validation / Resume or Handoff`，并说明“当前核心目标是否已由证据证明完成；若未完成，下一轮核心目标是什么”。
- 收尾时做一次 Project Sync Boundary 检查：本次过程留在 Feature Spec；稳定、可复用、跨任务会再次影响判断的事实列为 Project Sync Candidate，并按项目已定义落点或用户确认同步。

## 何时暂停

遇到以下情况，先暂停并说明原因：

- 需求存在会改变实现方向的关键歧义。
- 需要破坏性、高风险、不可逆操作。
- 任务明显不是最小混沌单元，且继续执行会导致大范围漂移。
- 模型提出的路径明显越过用户给定边界。
- 连续验证失败后仍沿同一路径推进，缺少回炉判断。
- 涉及架构级改动、公共接口变更、数据模型变更、迁移策略变更。
- 涉及跨项目修改，而用户未明确允许或范围未清楚。
- 发现现有 spec 明显错误、过期或与代码现实冲突。
- 尚未形成最小 spec 或尚未得到明确执行许可。

## 按需模块

- `references/spec-lite-template.md`：最小 spec 模板。
- `references/routing-map.md`：场景到 reference/script 的文档地图；不确定读什么时先看它。
- `references/mode-selection-lite.md`：light/one 选择、升级/降级条件。
- `references/anti-context-decay-lite.md`：长对话、新 chat、skill 遗忘时的回读和恢复规则。
- `references/project-sync-boundary.md`：项目知识沉淀、Project Sync Candidate、AGENTS / PROJECT_KNOWLEDGE / PROJECT_MEMORY / PROJECT_SPEC / Feature Spec 分流不清时读取。
- `references/skill-injection-check.md`：检查 agent / 项目规则 / 默认 prompt 是否实际注入本 skill。
- `references/default-prompt-setup-lite.md`：建立项目级/系统级默认 prompt 文档的最小写法。
- `references/script-map.md`：可直接调用的脚本入口，包含默认 prompt 检查/写入脚本。
- `references/modules.md`：`Deep Planning` / `Debug` / `Review` / `Multi-project`。
- `references/conventions.md`：落盘目录、命名规则、`micro-spec` 与正式 spec 的分流规则。
- `$new-chat-ready`：跨对话交接能力；触发 new chat / 换对话 / handoff / resume pack / 上下文压缩时使用，light 只维护 spec 锚点，不内嵌交接模板。

## 输出风格

- 默认中文，但不强制；用户、项目或目标文档明确使用其他语言时，跟随更具体的语言要求。
- 默认短输出，不复述完整协议。
- 优先给“当前理解 + 核心目标 + recap checkpoint + 下一步 + 必要风险”；只有不确定或需要证据时才补相关 spec 锚点。
- 不强制打印阶段状态机。
- 核心目标采用“事件触发式复述”：阶段开始、执行前 checkpoint、偏差暴露后、阶段收尾时必须重对齐；其他轮次不机械复读。
- 需要长链路推进时，优先给最小 `Done Contract` 与 `Resume/Handoff`，而不是扩写长计划。
- 小任务用 `micro-spec + micro-summary`；复杂任务再按需展开。
