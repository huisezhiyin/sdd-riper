# Default Prompt Setup Lite

用于在项目级或系统级默认 prompt 中轻量注入 `sdd-riper-one-light`，让多轮对话、new chat、不同 agent 入口仍能带上基本 Harness 能力。

## 何时询问

进入 new chat、新项目会话、首次在项目中启用 light，或出现以下情况时，先检查并询问用户是否要建立/更新默认 prompt 文档：

- 项目没有 `AGENTS.md` / `CLAUDE.md` / `.github/copilot-instructions.md` / `.cursorrules` 等默认规则。
- 已有规则，但没有说明何时使用 `sdd-riper-one-light`。
- new chat 后 agent 忘记 Restate / Checkpoint / Spec / Validation。
- 用户希望团队默认启用 light。

如果用户拒绝，继续当前任务，不静默写配置。

如果系统级 prompt 不可见，不要声称已经检查系统级配置；只说明已检查可见项目文件，并询问用户是否有系统级规则需要同步。

## 脚本入口

优先用脚本做确定性检查，避免 agent 自己漏文件或误判路由：

```bash
python3 <skill-root>/scripts/default_prompt_check.py --root <project-root> --mode light
```

用户明确批准后，才允许写入：

```bash
python3 <skill-root>/scripts/default_prompt_check.py --root <project-root> --mode light --apply --target AGENTS.md
```

脚本 map 见 `script-map.md`。

## 可写位置

- Codex / OpenAI agent: `AGENTS.md`
- Claude Code: `CLAUDE.md`
- GitHub Copilot: `.github/copilot-instructions.md`
- Cursor: `.cursorrules`
- 团队系统级 prompt：由用户提供路径或管理方式后再写

## 最小内容

默认 prompt 文档只写最小路由，不复制完整 skill：

```markdown
## AI Coding Harness

- 日常中等及以上 coding 任务默认使用 `sdd-riper-one-light`。
- light 默认用户已拆好任务；agent 只做目标复述、最小 spec/micro-spec、checkpoint、validation、handoff。
- 任务明显过大、边界不清、高风险或需要 codemap/context/频繁阻塞时，建议切到 `sdd-riper-one`。
- 不要裸改：中等以上任务执行前先说明目标、边界、下一步、风险和验证方式。
- 完成必须由测试、日志、运行结果或人工确认等证据证明。
- 不提交本地记忆、trace、SQLite/Milvus、密钥或机器私有路径。
```

## 注意事项

- 不要把完整 `SKILL.md` 粘进项目 prompt。
- 不要把教学长文、模板全文、案例全文常驻。
- 默认 prompt 负责路由和底线；细节按需读 skill references。
