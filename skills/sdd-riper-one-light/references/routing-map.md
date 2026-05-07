# Routing Map

`SKILL.md` 是运行内核，本文件是按需读取地图。默认不要通读 `references/`。

## 场景路由

| 场景 | 先读 | 按需再读 | 可调用脚本 |
|---|---|---|---|
| new chat / 新项目启动 | `skill-injection-check.md` | `default-prompt-setup-lite.md` | `scripts/default_prompt_check.py --root <project> --mode light` |
| 日常已拆好任务 | `spec-lite-template.md` | `conventions.md` | 无 |
| 任务明显过大/高风险 | `mode-selection-lite.md` | `modules.md` | 无 |
| 长对话 / new chat 恢复 | `anti-context-decay-lite.md` | `spec-lite-template.md` | 无 |
| deep/debug/review/multi-project | `modules.md` | `mode-selection-lite.md` | 无 |
| 默认 prompt 写入 | `default-prompt-setup-lite.md` | `script-map.md` | `scripts/default_prompt_check.py --apply`，必须先获用户批准 |

## Light 步骤树

```text
new chat check
  -> route exists: continue task
  -> route missing: ask user whether to create/update prompt file

task intake
  -> restate goal
  -> light sanity check
  -> minimal spec / micro-spec
  -> checkpoint
  -> approved execute
  -> validation
  -> reverse sync / handoff
```

## 不做什么

- 不主动重度拆分任务。
- 不频繁讲解理论。
- 不把完整模板、案例或 skill 复制到默认 prompt。
- 不用脚本替代工程判断。
