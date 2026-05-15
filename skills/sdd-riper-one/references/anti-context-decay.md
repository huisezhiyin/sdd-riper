# Anti Context Decay

重型 one 要重度留痕，但不能把所有历史常驻上下文。目标是不节约有效 token，但节约上下文注意力。

## 持久化分层

- Spec：任务真相源，记录目标、边界、阶段、决策、计划、验证、偏差、handoff。
- Recap Checkpoint：比 spec 更轻的热摘要，记录当前目标、进度、关键决策、下一步和验证/风险；用于防止当前 loop 腐烂，不替代 spec。
- Codemap：代码地形索引，按需回读，不常驻全量。
- Context bundle：需求输入的清洗结果，按需回读，不常驻全量。
- Archive：任务完成后的经验沉淀，用于复用和汇报。

## Checkpoint 热摘要

不要每轮把 spec 摘要或完整 spec 塞回上下文。到 checkpoint、执行前、阶段收尾、偏差暴露、离开后返回、用户问“现在到哪了”或 new chat 恢复时，先让模型自总结：

- phase
- approval status
- spec path
- Final Goal
- Current Task Unit
- Done / Key Decisions
- In / Out
- active checklist / next action
- open questions
- current risks

这组摘要是当前轮的工作记忆，不是新的真相源；如果它和 spec 冲突，以 spec 为准。长任务暂停、切阶段或交接前，把最新 recap 回写到 spec 的 `Checkpoint Summary` 或 `Resume / Handoff`。

## 惰性回读触发

先自总结，再按需回读 spec 相关区块：

- 切阶段前。
- Plan / Execute / Review 前。
- 用户纠正目标或范围。
- 新 chat 继续旧任务。
- 长对话出现遗忘、摘要冲突或行为漂移。
- 高风险动作前。

优先回读相关区块，不默认整份重载。回读完整 spec 仅用于：

- 阶段切换有争议。
- checkpoint 摘要与 spec 冲突，且相关区块不足以澄清。
- Review 需要跨目标、计划、执行日志、验收约束做全链路核对。
- 准备 handoff / archive。

回读 skill/reference：

- 忘记 No Spec / Plan Approved / Review 门禁。
- 模式选择、任务拆分、水流路线、注入诊断不清楚。
- 需要建立默认 prompt 文档，让 new chat 默认带入 skill 路由。
- new chat 启动时先检查可见项目/系统提示词入口；缺少 skill 路由时询问是否新建或补充默认 prompt 文档。

## New Chat 恢复块

暂停或交接前，在 spec 写：

```text
Resume Anchor:
- Final Goal:
- Current Task Unit:
- Current Phase:
- Approval Status:
- Done:
- Not Done:
- Next One Action:
- Validation State:
- Remaining Risks:
```
