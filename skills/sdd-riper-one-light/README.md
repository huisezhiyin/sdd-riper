# sdd-riper-one-light

面向 `GPT-5.4` 等强模型的轻量 SDD / RIPER coding skill，也是本仓库主推的日常 AI Agent Harness。

它不是把原版弱化，也不是只给熟练用户的“进阶版”。它代表大模型时代的默认工作方式：承认模型已经从“助手”变成事件推进的主体，允许它自己分解、探索和执行；人类通过 Checkpoint、Approval、Validation 与 Reverse Sync 控制边界和节奏。

如果说强模型是赛道上的主力，`sdd-riper-one-light` 就是让骑手和马协同工作的 Harness：模型负责速度、探索和推进，人类负责方向、风险、节奏和验收。

它把重点从“强制 phase 展开”切到“强制 checkpoint 校准”：

- `Spec is Truth`
- `No Spec, No Code`
- `No Approval, No Execute`
- `Restate First`
- `Core Goal as Loop Anchor`
- `Done by Evidence`
- `Reverse Sync`
- 默认中文、短汇报、按需加载深模块

## 工作方式优先

这个 skill 更适合被理解成一种**轻量但有硬门禁的工作方式**，而不是一句 prompt 技巧。

真正要让团队先记住的不是某条调用咒语，而是下面这些习惯：

- 先复述理解，再进入计划
- 先明确阶段性核心目标，并把它当成当前 loop 的唯一锚点
- 先形成 `micro-spec` 或最小 spec，再进入执行
- 先写清什么算完成、由什么证明
- 先讲清 `目标`、`范围`、`约束`、`验证方式`
- 获批后再执行
- 执行后回写结论，并留下可恢复锚点
- 测试、日志或手动验证暴露偏差后，先重述当前核心目标和剩余差距，再决定下一轮

如果先把这些习惯建立起来，`sdd-riper-one-light` 才会发挥出“短协议 + 强控制”的优势。

## 适用场景

适用于高输入、高频、多轮的 coding / agentic coding 任务，尤其适合：

- 大上下文、多文件、长链路任务
- 强模型已能自行分解任务，不需要反复喂整份 spec
- 更希望通过先复述任务理解、再反复强调核心目标、持续总结进度来维持注意力
- 需要把 `review -> 提测 -> 手测 -> 日志回喂 -> 下一轮目标` 串成一个小闭环
- 希望减少重型协议常驻 token 开销，同时保留硬门禁

## 核心特点

- `checkpoint-driven`：强制保留校准点，不强制保留整套 phase 文本
- 双门禁：必须先有最小 spec，且必须先获批准再执行
- 自分解优先：默认由模型自行拆解任务与补足局部计划
- `Restate First`：用户给任务后，先用模型自己的话复述理解
- `Core Goal as Loop Anchor`：阶段性核心目标在关键节点必须被重新对齐，防止长链路漂移
- `Done by Evidence`：完成由验证结果和外部反馈证明，而不是由模型自行宣布
- 轻量 spec：用最小文档承载目标、边界、进度、计划与结论
- `Resume Ready`：长任务暂停前保留最小恢复锚点，支持跨轮继续
- 按需模块：`Deep Planning` / `Debug` / `Review` / `Multi-project`

## 最小工作流

1. 先复述模型自己的任务理解
2. 明确本轮阶段性核心目标，并写入最小 spec
3. 建立或更新最小 spec，并落盘
4. 写清 `Done Contract`：什么算完成、由什么证明
5. 输出简短 checkpoint：区分任务理解、核心目标、当前进度
6. 在测试、日志或人工反馈后，先重述核心目标是否已完成、还差什么
7. 等待用户明确批准
8. 执行修改
9. 回写 spec 中的 `Change Log / Validation / Resume or Handoff`，并写明下一轮目标或收尾结论

## 推荐的最小启动方式

默认不要让使用者先背 prompt，而是让他们按下面这套方式给任务：

- 先说 `目标`
- 再说 `范围`
- 再说 `约束`
- 再说 `验证方式`

然后要求 skill：

- 先复述理解
- 先明确阶段性核心目标
- 先输出 `micro-spec / summary`
- 先写 `Done Contract`
- 先给 checkpoint
- 在拿到日志或测试反馈后，先重新判断核心目标是否完成
- 批准后再执行

如果一定要给一个最小模板，可以给这种级别：

```text
请使用 sdd-riper-one-light 先收敛任务，不要直接改代码。
先给我：
- 你对任务的理解
- 本轮阶段性核心目标
- micro-spec / summary
- Done Contract
- 下一步动作
- 风险
- 验证方式
我批准后再执行。
```

## 使用提示

- 小任务：使用 `micro-spec + micro-summary`
- 中任务：走 `standard`
- 复杂任务：升级到 `deep`，必要时加载按需模块
- 每轮只回读当前相关 spec 区块，不整份重载
- 关键不是展开阶段，而是把阶段性核心目标当成 loop 锚点，在关键节点复述理解、强调目标、用证据判定完成并同步进度

## 说明

这个仓库是 light 版实现，强调：

- 少文本
- 强校准
- 强门禁
- 高可控
- 更适配强模型的自分解与自回顾能力

README 负责说明默认工作方式；真正的协议约束以 `SKILL.md` 为准。

## 虚构示例

仓库内提供了 3 份虚构/合成示例，分别对应：

- `standard spec`：[examples/specs/spec-standard-security-status-race.md](examples/specs/spec-standard-security-status-race.md)
- `light spec`：[examples/specs/spec-light-runtime-compat.md](examples/specs/spec-light-runtime-compat.md)
- `feature codemap`：[examples/codemap/codemap-feature-content-control.md](examples/codemap/codemap-feature-content-control.md)

这些示例用于模拟常见任务中的问题形态、分析结构和闭环方式，不对应任何具体组织、业务系统或在用项目。
