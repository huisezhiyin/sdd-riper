# sdd-riper-one-light

面向 `GPT-5.4` 等强模型和熟练用户的轻量 SDD / RIPER coding skill，也是日常 AI Agent Harness。

它是同一套 SDD / Code is cheap 控制原语的低摩擦实现，不是残缺版。它默认用户已经把任务拆得基本可执行，模型能力也足够强，因此不承担重度教学、重度拆分和频繁阻塞。它代表强模型时代的低干扰工作方式：承认模型已经从“助手”变成事件推进的主体，允许它自己分解、探索和执行；人类通过最终目标、Checkpoint、Approval、Validation 与 Reverse Sync 控制边界和节奏。

如果说 `sdd-riper-one` 是同一套核心原语的重型 Harness 教练和控盘器，`sdd-riper-one-light` 就是熟练用户的无感安全带：模型负责速度、探索和推进，人类负责方向、风险、节奏和验收。两者差异主要是门禁强度、流程显式度和产物密度，不是核心能力是否存在。

它把重点从“强制 phase 展开”切到“强制 checkpoint 校准”：

- `Spec is Truth`
- `No Spec, No Code`
- `No Approval, No Execute`
- `Restate First`
- `Core Goal as Loop Anchor`
- `Done by Evidence`
- `Reverse Sync`
- 默认中文但不强制、短汇报、按需加载深模块

## 工作方式优先

这个 skill 更适合被理解成一种**轻量但有硬门禁的工作方式**，而不是一句 prompt 技巧。

它默认不教用户怎么完整拆任务，只在明显失控时提醒升级。真正要保留的是下面这些习惯：

- 先复述理解，再进入计划
- 先明确阶段性核心目标，并把它当成当前 loop 的唯一锚点
- 先形成 `micro-spec` 或最小 spec，再进入执行
- 先写清什么算完成、由什么证明
- 先讲清 `目标`、`范围`、`约束`、`验证方式`
- 获批后再执行
- 执行后回写结论，并留下可恢复锚点
- 测试、日志或手动验证暴露偏差后，先重述当前核心目标和剩余差距，再决定下一轮

如果先把这些习惯建立起来，`sdd-riper-one-light` 才会发挥出“短协议 + 强控制 + 低打扰”的优势。

## 适用场景

适用于高输入、高频、多轮的 coding / agentic coding 任务，尤其适合：

- 大上下文、多文件、长链路任务
- 强模型已能自行分解任务，spec 只做持久化真相源和按需索引，不作为每轮 prompt 包
- 用户已经把任务拆到基本可执行，不需要 skill 主动训练任务拆分
- 更希望通过先复述任务理解、在 checkpoint 点自总结核心目标和进度来维持注意力
- 需要把 `review -> 提测 -> 手测 -> 日志回喂 -> 下一轮目标` 串成一个小闭环
- 希望减少重型协议常驻 token 开销，同时保留硬门禁

## 核心特点

- `checkpoint-driven`：强制保留校准点，不强制保留整套 phase 文本
- 双门禁：必须先有最小 spec，且必须先获批准再执行
- 自分解优先：默认由模型自行拆解任务与补足局部计划
- 无感安全带：默认相信用户拆分，只做轻量 sanity check
- `Restate First`：用户给任务后，先用模型自己的话复述理解
- `Core Goal as Loop Anchor`：阶段性核心目标在关键节点必须被重新对齐，防止长链路漂移
- `Done by Evidence`：完成由验证结果和外部反馈证明，而不是由模型自行宣布
- 轻量 spec：用最小文档承载目标、边界、进度、计划与结论
- `Resume Ready`：长任务暂停前保留最小恢复锚点，支持跨轮继续
- 按需模块：`Deep Planning` / `Debug` / `Review` / `Multi-project`

## 最小工作流

1. 先复述模型自己的任务理解
2. 轻量判断任务是否明显过大、越界或高风险；没有明显问题就继续
3. 明确本轮阶段性核心目标，并写入最小 spec
4. 建立或更新最小 spec，并落盘
5. 写清 `Done Contract`：什么算完成、由什么证明
6. 输出简短 checkpoint：区分任务理解、核心目标、当前进度
7. 在测试、日志或人工反馈后，先重述核心目标是否已完成、还差什么
8. 等待用户明确批准
9. 执行修改
10. 回写 spec 中的 `Change Log / Validation / Resume or Handoff`，并写明下一轮目标或收尾结论

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
- 如果需要主动拆分最小混沌单元、生成完整 codemap/context、频繁阻塞或训练用户，切到 `sdd-riper-one`
- checkpoint 时先自总结当前目标、进度、风险和验证状态；仍不确定时只回读相关 spec 区块，不整份重载
- 长对话或 new chat 恢复时，按需读取 `references/anti-context-decay-lite.md`
- 进入 new chat 或新项目会话时，先检查可见的项目/系统提示词入口是否包含 skill 路由；缺失时询问是否新建或补充 `AGENTS.md`、`CLAUDE.md` 等默认 prompt 文档；写法见 `references/default-prompt-setup-lite.md`
- 默认 prompt 检查优先调用 `scripts/default_prompt_check.py`，脚本入口见 `references/script-map.md`
- 不确定该读哪份 reference 时，先看 `references/routing-map.md`
- 关键不是展开阶段，而是把阶段性核心目标当成 loop 锚点，在关键节点自总结、必要时惰性回读、用证据判定完成并同步进度

## 说明

这个仓库是 light 版实现，强调：

- 少文本
- 强校准
- 必要门禁
- 高可控
- 更适配强模型的自分解与自回顾能力
- 渐进式披露：`SKILL.md` 放运行内核，模板、模式选择、上下文防腐烂和注入诊断放在 `references/`
- 默认注入只写最小路由和底线，不复制完整 skill，避免污染长期上下文

README 负责说明默认工作方式；真正的协议约束以 `SKILL.md` 为准。

## 脱敏示例

仓库内提供了 3 份脱敏后的真实案例，分别对应：

- `standard spec`：[examples/specs/spec-standard-security-status-race.md](examples/specs/spec-standard-security-status-race.md)
- `light spec`：[examples/specs/spec-light-runtime-compat.md](examples/specs/spec-light-runtime-compat.md)
- `feature codemap`：[examples/codemap/codemap-feature-content-control.md](examples/codemap/codemap-feature-content-control.md)

这些示例保留了真实任务中的问题形态、分析结构和闭环方式，但移除了内部项目、类名、路径与日志标识。
