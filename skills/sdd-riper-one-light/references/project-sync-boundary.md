# Project Sync Boundary

本文件是按需读取的项目知识沉淀边界说明。默认不要常驻加载；只有项目知识落点不清、任务产生跨任务可复用事实，或用户要求沉淀项目知识时再读取。

## Principle

Code is cheap, context is expensive.

SDD 优化的是上下文路由、落盘、恢复和审查能力，不是把项目知识治理规则继续塞进 active skill prompt。

人和项目定义知识拓扑；SDD 只负责识别候选、必要时请求确认，并按已声明规则同步。

## Priority

1. 用户明确指令
2. 项目 `AGENTS.md`
3. 项目已有约定
4. SDD 默认建议

## Common Targets

这些是默认建议，不是强制裁判。项目规则或用户指令优先。

### AGENTS.md

适合放 agent 面向的项目工作规则：

- skill 路由
- 工作流习惯
- 验证期望
- 安全边界
- 进入项目时先读哪些文件或目录
- 长期知识入口索引

### PROJECT_KNOWLEDGE.md

适合放稳定项目知识：

- 仓库拓扑
- mirror / downstream 关系
- 稳定项目事实
- 历史决策
- 反复踩坑
- 可复用验证或同步命令

### PROJECT_MEMORY.md

适合放演进型团队或项目记忆：

- lessons learned
- 反复出现的运维或协作注意事项
- 私有或内部上下文
- 可能变化、不适合作为公开文档的经验

### PROJECT_SPEC.md

适合放长期项目真相：

- 产品或架构约束
- 长期决策
- 会指导未来 Feature Spec 的项目级不变量

### Feature Spec

适合放任务局部上下文：

- 当前目标
- 范围和非目标
- 本任务决策
- plan 和 checklist
- validation evidence
- change log
- open risks
- 临时执行状态

## Trigger Points

只有这些场景才读取本文件：

- 用户问项目知识应该落到哪里
- 任务产生稳定、可复用、跨任务会再次影响判断的事实
- 用户反复纠正暴露出长期规则
- Review 发现可复用验证命令或反复踩坑
- new chat / handoff / resume 需要恢复项目知识入口
- 项目级文件和 Feature Spec 边界可能混淆

## Project Sync Candidate

SDD 发现可复用项目知识时，默认不要静默写入。先提出候选：

- fact / rule
- source evidence
- why reusable
- suggested target file
- scope
- privacy / commit boundary

## Sync Flow

1. 检查 `AGENTS.md` 是否声明知识入口和同步策略。
2. 如果项目已定义目标文件，按定义执行。
3. 如果不清楚，提出 Project Sync Candidate。
4. 除非项目规则明确允许，否则同步前等待用户确认。
5. 任务局部执行流水留在 Feature Spec，不写入项目级长期文件。
6. 不默认 stage 或 commit project memory、spec、handoff、私有知识或用户偏好记忆。

## Non-Goals

SDD 不应该：

- 变成通用项目知识管理 skill
- 不经用户或项目规则就裁判所有知识分类
- 每轮加载本 reference
- 把大段项目记忆复制进 active context
- 把项目知识文件当作 prompt payload
- 把临时任务日志写入项目级长期文件
