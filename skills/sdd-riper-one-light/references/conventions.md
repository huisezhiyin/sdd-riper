# Conventions Reference

仅在需要落盘 spec / codemap 时查看。
本文件不是常驻协议，不应在每轮任务中重复注入。

## 时间前缀

- 统一使用：`YYYY-MM-DD_hh-mm_`

## 目录约定

- `micro-spec`：`mydocs/micro_specs/`
- `feature spec / standard spec`：`mydocs/specs/`
- `project spec / project memory`：`mydocs/project/`
- `codemap`：`mydocs/codemap/`

## 文件命名

- `micro-spec`：`mydocs/micro_specs/YYYY-MM-DD_hh-mm_<TaskName>.md`
- `feature spec / standard spec`：`mydocs/specs/YYYY-MM-DD_hh-mm_<TaskName>.md`
- `project spec`：`mydocs/project/PROJECT_SPEC.md`
- `project memory`：`mydocs/project/PROJECT_MEMORY.md`
- `codemap`：`mydocs/codemap/YYYY-MM-DD_hh-mm_<ProjectOrFeature>.md`

## Spec 分层边界

- `Feature Spec`：当前任务真相源，记录本次目标、边界、Done Contract、recap checkpoint、计划、改动、验证、剩余风险和 handoff。
- `Project Spec`：项目长期真相源，记录稳定业务概念、模块边界、架构约定、核心链路、测试/构建入口和跨任务会复用的事实。
- `Project Memory`：项目经验层，记录常见坑点、已验证排查路径、经验模式和后续 agent 进入项目时应知道的注意事项。

硬边界：

- Feature Spec 不承载项目长期记忆。
- Project Spec 不承载任务执行流水。
- Codemap 不承载任务决策，只做代码地形索引。
- Archive 不替代当前真相源，只做完成后的沉淀视图。

## Project Spec 同步规则

从 Feature Spec 反向同步到 Project Spec / Project Memory 前，必须满足至少一条：

- 该事实稳定存在于代码、配置、测试或业务规则中。
- 后续多个任务会再次依赖它。
- 它能减少未来 agent 的重复探索或误判。
- 它是已验证的坑点、约定、入口或测试方法。

不得同步：

- 本次临时命令、一次性执行流水、未验证假设、短期 workaround。
- 只对当前任务有效的计划、进度、approval、dirty state。

## 何时优先用 `micro-spec`

- 小范围代码修改
- 单文件或少量文件改动
- 需求相对明确
- 不需要显式方案权衡

## 何时升级为正式 spec

- 架构设计或大范围重构
- 跨模块 / 跨项目任务
- 复杂迁移
- 需求模糊，需要方案权衡
- 需要显式评审与回写

## TaskName 建议

- 用简短英文、拼音或稳定短语
- 聚焦任务目标，不写长句
- 一个文件名只表达一个主要任务

## 使用原则

- spec 是真相源，不是聊天记录转储
- 先判断当前写入属于 Feature Spec 还是 Project Spec，不能混写
- codemap 是索引，不是源码拷贝
- 默认优先 `micro-spec`
