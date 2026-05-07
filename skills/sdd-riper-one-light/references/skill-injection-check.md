# Skill Injection Check

用于诊断当前 agent、项目规则或默认 prompt 是否实际注入了 `sdd-riper-one-light`。

## 行为信号

如果 skill 生效，通常会看到：

- 用户给任务后先复述理解。
- 中等以上任务会形成 spec、micro-spec、summary 或 handoff。
- 执行前给 checkpoint，说明目标、边界、下一步、风险、验证方式。
- 完成时用测试、日志、运行结果、人工确认等证据收口。
- 执行后回写 Change Log / Validation / Resume or Handoff。
- 长对话或 new chat 时会先做 checkpoint 自总结，再按需回读相关 spec 区块，而不是只靠聊天记忆。

## New Chat 启动检查

进入 new chat 或新项目会话时，先做一次轻量检查：

1. 优先调用 `scripts/default_prompt_check.py --root <project-root> --mode light`。
2. 检查可见的项目级 prompt 文件是否存在。
3. 检查其中是否包含 `sdd-riper-one-light` 路由。
4. 若缺失，询问用户是否要新建或补充默认 prompt 文件。
5. 用户同意前，不静默创建或修改文件。
6. 如果系统级 prompt 不可见，向用户说明只能检查可见文件，并询问是否有系统级规则需要同步。

## 项目规则检查

检查项目内是否有默认路由：

- `AGENTS.md`
- `CLAUDE.md`
- `.cursorrules`
- `.github/copilot-instructions.md`
- 其他系统级、项目级或团队级默认 prompt

重点看是否包含：

- 何时启用 `sdd-riper-one-light`
- 是否在任务过大、高风险、需要 codemap/context 或频繁阻塞时切到 `sdd-riper-one`
- 是否要求 `No Spec, No Code`
- 是否要求 checkpoint / validation
- 是否禁止提交本地记忆、运行数据、密钥

如果缺少默认路由，先询问用户是否要按 `default-prompt-setup-lite.md` 建立/更新默认 prompt 文档。

## 手动显式调用

如果不确定是否注入，可在任务开头写：

```text
请使用 sdd-riper-one-light。
先复述理解，建立或更新最小 spec，执行前给 checkpoint，我确认后再改。
```

## 常见失效表现

- 直接裸改，不复述目标。
- 没有 spec / summary / handoff。
- 没有 checkpoint 就做高影响修改。
- 只说“完成了”，没有验证证据。
- 长任务没有 Resume / Handoff。
- 新 chat 无法从本地 spec 恢复。

出现这些表现时，先回读 `SKILL.md` 和 `anti-context-decay-lite.md`，再恢复任务。

若这些失效在 new chat 中反复出现，建议建立项目级或系统级默认 prompt 文档，不要只依赖当前聊天上下文。
