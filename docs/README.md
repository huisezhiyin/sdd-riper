# 文档阅读地图

这个目录只保留三篇定位互补的长文。历史稿不再放在工作树里；如需追溯，可以从 Git 历史恢复。

## 三篇文章

| 文档 | 适合谁 | 回答什么问题 |
| --- | --- | --- |
| [Code is cheap. Don't write any.](./code-is-cheap.md) | 入门读者、工程师、宣讲场 | 为什么代码廉价后，控制面必须上移到目标、上下文、checkpoint、证据和风险 |
| [一套可复制的 AI Coding Harness 工作法](./ai-coding-harness-guide.md) | 准备把方法用于真实任务的人 | 怎样切任务、准备上下文、设置边界、推进、验收和交接 |
| [为什么通用 Agent 是饮鸩止渴](./general-purpose-agents-are-a-trap.md) | Agent 产品与平台建设者 | 为什么具体能力、显式 Flow、业务接口和必要的 hardcode 往往更可靠 |

## 最短阅读路径

如果你只想开始使用：

1. 先读 [`sdd-riper-one-light` 快速说明](../skills/sdd-riper-one-light/README.md)；
2. 用快速模板跑一个真实任务；
3. 遇到问题时再读 Harness 实战指南。

如果你想理解方法论：

1. 读 `Code is cheap`；
2. 读 Harness 实战指南；
3. 做 Agent 产品或业务自动化时，再读通用 Agent 观点文。

## 一句话主线

```text
人负责目标、边界、checkpoint、验收和沉淀；
模型负责探索、实现和推进；
spec 保存持久化事实，活跃上下文只读取下一步需要的最小切片。
```

日常任务使用 `sdd-riper-one-light`。陌生代码、大模块和跨仓任务先用 `codemap`。高风险、训练和审计场景切到 `sdd-riper-one`。长暂停、交接和上下文重置使用 `new-chat-ready`。

## 维护原则

- 长文固定为“核心判断、实践工作法、延伸观点”三个位置。
- 新思想优先合并进现有文章；只有出现新的、无法合并的问题域时才新增长文。
- 不在公开文章中保留缺少来源的效率数字、特定模型推荐或已经不存在的命令。
- 历史稿由 Git 保存，不在仓库里维护第二套 archive。
- 文章里的 Skill 名称、链接和行为必须与当前仓库一致。
