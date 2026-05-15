---
name: sdd-riper-one
description: 将 SDD-RIPER 方法论落地为严格可执行流程的重型 Harness 技能。用于辅助用户澄清最终目标、生成 codemap/context、拆分最小混沌单元、维护完整 spec、执行 RIPER 阶段门禁、阻塞高风险动作和沉淀可 new chat 恢复的本地任务轨迹。
---

# SDD-RIPER-ONE Skill

## 全局行为与安全底线 (Global Safeguards)

- **高危操作阻断**：永远不要静默或提议执行 `git clean`（包含任何参数，特别是 `-fdx`），防止用户未提交的工作区数据不可逆丢失。
- **研发纪律**：
  - `No Spec, No Code`：未形成并持久化 Spec 前，不进入代码实现。
  - `No Approval, No Execute`：未得到执行许可前，禁止进行环境修改或高风险变更。
  - `Spec is Truth`：任何聊天决议或最新改动必须回源到 Spec，Spec 是唯一真相源。

## 核心定位

- 这是重型 Harness 教练 / 控盘器 / 本地任务黑盒，不是 `sdd-riper-one-light` 的简单完整版。
- 默认用于用户、模型或任务还不能稳定切出最小混沌单元的场景：新手、实习生、低质量模型、复杂需求、高风险修改、长链路推进、审计或交接任务。
- 它要做更多事：澄清最终目标、生成 codemap/context、辅助拆分任务单元、频繁 checkpoint、显式阻塞、记录决策与进度、检查路线是否偏离最终目标。
- 自动化按风险释放：目标和任务单元不清时降低自动化、增加问询和阻塞；一旦最小混沌单元清楚，可在批准范围内自动推进该单元。
- `New Chat Startup Check`：进入 new chat 或新项目会话时，先检查可见的项目/系统提示词入口是否存在、是否包含 `sdd-riper-one` / `sdd-riper-one-light` 路由；缺失时询问用户是否要新建或补充 `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`、`.cursorrules` 等默认文档；未获同意不得静默写入。
- 先读一次：`references/sdd-riper-one-protocol.md`
- 总纲：`Pre-Research -> RIPER`，全程遵循 SDD 并持续维护 Spec
- 三条底线：`No Spec, No Code`、`Spec is Truth`、`Reverse Sync`
- `create_codemap` / `build_context_bundle` 是 Pre-Research 输入准备；`sdd_bootstrap` 是 RIPER 启动命令（进入 Research 第一步，同时完成 Pre-Research 收口）
- RIPER 主流程：`Research -> (Innovate, 可选) -> Plan -> Execute -> Review`
- 不要在每轮对话里重载整份 Skill / Spec；spec 是可回查的真相源，不是反复塞入上下文的 prompt 包。教学、诊断、模板和长规则放在 references 按需加载。
- 默认 prompt 文档只写最小路由、边界、禁止项和恢复规则；不要把完整 Skill 复制进项目 prompt，避免把长期上下文变成噪音。
- **Spec 受众分层与上下文保护**：Spec 的第一受众是人类（持久化的任务上下文与组织记忆），第二受众才是模型。协议对模型的核心价值是四件事：**注意力聚焦**（让模型在当前阶段只关注该关注的）、**信息索引**（需要时按路径回读，而非全量常驻）、**防止上下文腐烂**（用落盘的 Spec 对抗长对话中的遗忘与漂移）、**辅助 Review**（提供 Spec vs 代码的交叉验证基准）。协议绝不应导致上下文被塞满挤爆——RIPER 管流程，Spec 管记录，模型按需取用。
- **Spec 分层边界**：默认活跃 spec 是 `Feature Spec`，只记录本次任务；`Project Spec` / `Project Memory` 只记录稳定、可复用、跨任务会影响判断的项目事实。禁止把任务流水写进 Project Spec，也禁止把项目长期记忆塞进 Feature Spec。

## Harness 教练职责

- 与用户讨论最终目标是否清晰，必要时先收敛目标而不是直接拆实现。
- 评估当前输入是否能形成最小混沌单元；不能时，先拆分、补 codemap/context 或提出阻塞问题。
- 将每个任务单元写清：目标、边界、上下文、验证证据、失败回炉方式、用户选择。
- 在 spec 中持续记录目标、进度、决策、路线偏差、验证、剩余风险和 handoff，支持随时 new chat 恢复。
- 在关键 checkpoint 提醒最终目标和当前任务单元，检查当前路线是否偏离目标。
- 给用户更强选择权：方案分叉、风险接受、NO-GO 后继续、范围变化，都要显式记录用户决策。

## 推荐流程（直接执行）

- 标准流（中大型任务）：
  - `create_codemap -> build_context_bundle -> sdd_bootstrap -> Research -> (Innovate, 可选) -> Plan -> Execute -> Review`
- 快速流（小任务/需求模糊）：
  - `sdd_bootstrap -> （按需补）create_codemap/build_context_bundle -> Research -> Plan -> Execute -> Review`
- 门禁：
  - 首版 spec 落盘前，不进入实现
  - 未完成最终目标澄清和最小混沌单元评估前，不进入 Plan
  - 未收到精确字样 `Plan Approved`，禁止进入 `Execute`
  - `Review` 不通过，回到 `Research/Plan` 修正

## 上下文装配规则

- `SDD` 是完整持久化上下文与记忆层：必须完整落盘、持续维护，但不作为每轮常驻输入
- `RIPER` 是审批驱动状态机：checkpoint 时必须让当前 `phase`、批准状态与下一步动作清晰可见
- 裁剪目标是减少重复重放，不是减少约束或弱化门禁

### Checkpoint 热摘要（惰性更新）

在 checkpoint、执行前、阶段收尾、偏差暴露或 new chat 恢复时，先让模型用当前上下文自总结：

- 当前 `phase`
- 当前 `approval status`
- 当前 `spec path`
- 当前 `Goal`
- 当前 `Done / Key Decisions`
- 当前 `In Scope / Out of Scope`
- 当前活跃 `Checklist`
- 当前 `Open Questions`
- 当前风险与 `Next Action`

热摘要只用于当前轮聚焦，不替代 spec；与 spec 冲突时，永远以 spec 为准。它是比完整 spec 更轻的 recap checkpoint，用来防止当前 loop 上下文腐烂；除 checkpoint/恢复/高风险节点外，不机械重复这组字段。

### 温上下文（切阶段或高风险动作前加载）

- `Research -> Plan`：`Research Findings`、关键事实、方案结论
- `Plan -> Execute`：`File Changes`、`Signatures`、原子 `Checklist`
- `Execute -> Review`：`Validation`、实际改动摘要、偏差说明
- 执行 `review_spec` / `review_execute` 时，回读对应评审区块

### 冷上下文（默认不带，命中再加载）

- 全量 `Change Log`
- 历史 `Research` 细节
- 完整 `codemap`
- 完整 `context bundle`
- `MULTI` / `DEBUG` / `ARCHIVE` 的完整扩展规则
- 长示例、长模板、长 quick reference

### 硬门禁（不可因裁剪而削弱）

- 没有 spec，不进入代码实现
- spec 未记录最终目标、当前任务单元、边界和验证方式，不进入 Plan
- spec 必须声明层级：`Feature Spec` / `Project Spec`。普通开发任务默认只能维护 Feature Spec；Project Spec 更新必须来自已确认的 Project Sync Candidate。
- `phase` 与 `approval status` 必须是显式状态，不允许根据语气、倾向或不完整表述推断
- 没有精确字样 `Plan Approved`，不进入 `Execute`
- phase 切换前，先做 checkpoint 自总结；若摘要缺字段、不确定、与 spec 可能冲突，或下一阶段依赖具体条款，再回读对应 spec 区块
- `Review` 时必须基于 plan 与 validation，而不是只看聊天摘要
- 发现冲突、字段缺失、摘要过期或记忆不确定时，优先回读相关原文区块；只有恢复、交接、归档、严重冲突或多处不确定时才全量回读

### 回读触发规则

- **默认**：不反复喂完整 spec；保留 `spec path`，让模型在 checkpoint 点先自总结当前状态
- **切阶段时**：先 checkpoint 自总结，再按依赖回读目标阶段对应的 spec 区块（Research Findings / File Changes / Validation 等）
- **执行 review 时**：`review_spec` 回读 Plan 区块，`review_execute` 回读 Plan + Validation + Review 区块
- **触发全量回读**：恢复/handoff/archive、阶段切换有争议、摘要与 spec 冲突、长对话出现明显遗忘且相关区块不足、高风险改动涉及多处约束
- **禁止**：不能把 spec 当作每轮 prompt 包反复注入，不能用热摘要替代必要的 spec 原文，不能根据模糊语气推断 `Plan Approved`

### Skill / Reference 回读触发

- 模式选择不清：读 `references/mode-selection.md`
- 不确定当前场景该读什么或该调用哪个脚本：读 `references/routing-map.md`
- 不会拆任务或目标不清：读 `references/minimum-chaos-unit.md`
- 模型提出不同路线，需要判断是否顺水接受：读 `references/water-flow.md`
- 长对话、新 chat、上下文腐烂、忘记 skill 行为：读 `references/anti-context-decay.md`
- 怀疑 agent / 项目规则 / 默认 prompt 没有注入本 skill：读 `references/skill-injection-check.md`
- 需要建立项目级/系统级默认 prompt 文档：读 `references/default-prompt-setup.md`
- 需要确定脚本入口或参数：读 `references/script-map.md`

## 按需能力入口

- 多项目：触发 `MULTI / 多项目 / CROSS / SWITCH` 时读 `references/multi-project.md`。
- 原生命令：触发 `create_codemap / build_context_bundle / sdd_bootstrap / review_spec / review_execute / archive` 时读 `references/commands.md`。
- Debug：触发 `DEBUG / 排查 / 日志分析 / 验证功能` 时读 `references/sdd-riper-one-protocol.md` 的 Debug 段或 `references/usage-examples.md` 的 Debug 示例。
- New Chat Ready：触发 `new chat / 换对话 / handoff / resume_pack / 续接 prompt / 上下文压缩` 时调用 `$new-chat-ready`，并同步当前 spec 的 `Resume / Handoff` 区块。
- 触发词、命名规则、阶段 DoD：需要时读 `references/workflow-quickref.md`。
- 归档脚本：需要执行 archive 时读 `references/script-map.md` 和 `references/archive-template.md`。

## 阶段约束（最小集合）

- 在 checkpoint 点先自总结当前目标、阶段、批准状态、下一步与风险；再决定是否同步或回读 spec
- 默认不在每轮对话中重载整份 spec；只在需要时回读当前阶段区块、活跃 checklist、`Open Questions`、最近一次 `Change Log / Validation`
- 仅在恢复/handoff/archive、严重冲突、跨阶段依赖复杂或明显遗忘且相关区块不足时，全量回读 spec
- `codemap` / `context bundle` 按需读取，不作为每轮固定输入
- `Innovate` 可选：复杂任务建议 2-3 方案；小任务可跳过但要写原因
- `Plan` 必须可执行：文件路径 + 签名 + 原子 checklist
- `Plan` 后建议执行 `review_spec`；其 `NO-GO` 为建议项，不是强制门禁
- `Review` 必须按三轴评审并回写结论：`Review Matrix`、`Overall Verdict`、`Plan-Execution Diff`
- 任务闭环后建议执行 `archive`，沉淀 human/llm 双视角知识

## 参考

- `references/routing-map.md`（先看这个，决定读什么/调什么）
- `references/sdd-riper-one-protocol.md`
- `references/spec-template.md`
- `references/workflow-quickref.md`
- `references/usage-examples.md`
- `references/archive-template.md`
- `references/multi-project.md`（多项目协作详细规则）
- `references/commands.md`（原生命令动作详细参数）
- `references/script-map.md`（可调用脚本入口）
- `$new-chat-ready`（跨对话交接包与续接 prompt）
