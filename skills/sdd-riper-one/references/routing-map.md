# Routing Map

`SKILL.md` 是运行内核，本文件是按需读取地图。默认不要通读 `references/`。

## 场景路由

| 场景 | 先读 | 按需再读 | 可调用脚本 |
|---|---|---|---|
| new chat / 新项目启动 | `skill-injection-check.md` | `default-prompt-setup.md` | `scripts/default_prompt_check.py --root <project> --mode one` |
| 模式选择 | `mode-selection.md` | `minimum-chaos-unit.md` | 无 |
| 最终目标不清 / 任务太大 | `minimum-chaos-unit.md` | `commands.md` | 可按需生成 codemap/context |
| 需求材料杂乱 | `commands.md` | `spec-template.md` | 无 |
| 陌生代码库 / 跨模块 | `commands.md` | `workflow-quickref.md` | 无 |
| 模型提出不同路线 | `water-flow.md` | `spec-template.md` | 无 |
| 长对话 / new chat 恢复 | `anti-context-decay.md` | `spec-template.md` | 无 |
| 多项目 | `multi-project.md` | `commands.md` | 无 |
| 归档沉淀 | `archive-template.md` | `script-map.md` | `scripts/archive_builder.py ...` |
| 默认 prompt 写入 | `default-prompt-setup.md` | `script-map.md` | `scripts/default_prompt_check.py --apply`，必须先获用户批准 |

## One 步骤树

```text
new chat check
  -> route exists: continue task
  -> route missing: ask user whether to create/update prompt file

pre-research
  -> clarify final goal
  -> generate/read codemap if code terrain is unclear
  -> build/read context bundle if requirement is scattered
  -> assess minimum chaos unit

RIPER
  -> Research
  -> optional Innovate
  -> Plan
  -> Plan Approved
  -> Execute
  -> Review
  -> Archive / Handoff
```

## 不做什么

- 不把完整 skill、spec 模板、长理论文章复制到默认 prompt。
- 不用脚本替代目标判断、任务拆分和风险取舍。
- 不在任务单元清楚后继续过度阻塞。
- 不把 spec 当作每轮 prompt 包；checkpoint 先自总结，必要时惰性回读 spec 原文。
