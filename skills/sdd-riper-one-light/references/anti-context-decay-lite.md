# Anti Context Decay Lite

Light 的目标不是节约 token，而是节约上下文注意力。不要把长协议、长模板、长历史常驻进模型上下文；用 spec 和按需回读对抗长对话腐烂。

## Recap Checkpoint / 热摘要

不要每轮把 spec 摘要或完整 spec 塞回上下文。到执行前 checkpoint、偏差暴露、阶段收尾、暂停交接、离开后返回、用户问“现在到哪了”或 new chat 恢复时，先让模型生成一段短 recap。

`Recap Checkpoint` 是介于聊天流和 spec 之间的轻量持久化上下文：比普通总结更结构化，比 spec 更短。它的目标是让当前 loop 不腐烂，而不是记录全部过程。

最小形态可以是一行：

```text
recap: <当前目标>；已完成 <进度/证据>；关键决策 <决策>；下一步 <动作>；风险/验证 <状态>。
```

需要更清楚时，用这些最小锚点：

- 当前最终目标 / 本轮核心目标
- 当前 spec / micro-spec 路径
- 已完成进度和关键决策
- 当前 In / Out
- 当前 checkpoint 或下一步动作
- 当前 validation 状态
- 剩余风险和下一轮入口

这组摘要用于当前轮聚焦；它不是新的真相源，也不需要机械复读。若 recap 与 spec 冲突，以 spec 为准，并把冲突标出来。

## Recap 落盘规则

- 单轮小任务：recap 可以只留在回复里。
- 多步任务：把最新 recap 写进 micro-spec / spec 的 `Checkpoint Summary` 或 `Resume / Handoff`。
- 暂停、new chat、交接：先用 recap 收口，再调用 `$new-chat-ready` 生成可续接 prompt。
- 验证失败或目标变化：先更新 recap，再决定是否回读 spec 或调整任务边界。

## 何时回读 spec

出现以下情况时，先 checkpoint 自总结；如果仍有不确定、冲突或需要证据，再回读当前相关 spec 区块：

- 新 chat 继续旧任务。
- 长对话后目标、范围、验证方式开始漂移。
- 用户反馈“你忘了前面说过的目标/边界”。
- 执行前需要确认最新 checkpoint、批准状态或 Done Contract。
- 验证失败后需要决定继续、调整方向或回炉。

优先回读相关区块，不默认整份重载。完整 spec 只用于严重漂移、交接恢复、归档或多处约束相互影响的 Review。

## 何时回读 skill

出现以下情况时，回读 `SKILL.md` 或本 reference：

- 忘记 Restate / Checkpoint / Validation / Reverse Sync。
- 用户质疑当前行为是否符合 light。
- 任务从 light 升级到 deep，或建议切到 `sdd-riper-one`。
- 新 chat 里需要恢复 light 的默认工作方式。

## 何时回读 reference

- spec 字段不清楚：读 `spec-lite-template.md`。
- 模式选择不清楚：读 `mode-selection-lite.md`。
- 深规划、debug、review、多项目：读 `modules.md`。
- 怀疑 skill 没有注入：读 `skill-injection-check.md`。
- 需要建立默认 prompt 文档：读 `default-prompt-setup-lite.md`。
- new chat 启动时先检查可见项目/系统提示词入口；缺少 skill 路由时询问是否新建或补充默认 prompt 文档。

## 恢复输出

恢复时不要长篇复述协议，只输出：

```text
当前目标：
当前 spec：
当前边界：
当前进度：
下一步：
验证/风险：
```
