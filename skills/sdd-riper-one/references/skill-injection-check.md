# Skill Injection Check

用于检查当前 agent、项目规则或默认 prompt 是否实际注入 `sdd-riper-one`。

## 应有行为

如果 one 生效，通常会看到：

- 不会在 spec 落盘前进入实现。
- 会显式维护 phase、approval status、spec path。
- 会澄清最终目标，并评估当前任务单元是否足够小。
- 复杂或陌生代码会使用/生成 codemap。
- 多源需求会整理 context bundle。
- Plan 前有文件、签名、原子 checklist。
- 没有精确 `Plan Approved` 不进入 Execute。
- Execute 后有 Review / Validation / Plan-Execution Diff。
- 任务结束后建议 handoff 或 archive。

## New Chat 启动检查

进入 new chat 或新项目会话时，先做一次轻量检查：

1. 优先调用 `scripts/default_prompt_check.py --root <project-root> --mode one`。
2. 检查可见的项目级 prompt 文件是否存在。
3. 检查其中是否包含 `sdd-riper-one` / `sdd-riper-one-light` 路由。
4. 若缺失，询问用户是否要新建或补充默认 prompt 文件。
5. 用户同意前，不静默创建或修改文件。
6. 如果系统级 prompt 不可见，向用户说明只能检查可见文件，并询问是否有系统级规则需要同步。

## 项目规则检查

检查：

- `AGENTS.md`
- `CLAUDE.md`
- `.cursorrules`
- `.github/copilot-instructions.md`
- agent 默认 system/project prompt
- skill host 的安装和默认启用配置

重点确认：

- 是否默认路由 `sdd-riper-one` 或 `sdd-riper-one-light`。
- 哪些任务触发 one，哪些任务触发 light。
- 项目规则是否覆盖或削弱 `No Spec, No Code`、`Plan Approved`、`Spec is Truth`。
- 是否禁止提交本地记忆、trace、SQLite、Milvus、密钥等运行数据。

如果没有默认路由，先询问用户是否要按 `default-prompt-setup.md` 建立/更新默认 prompt 文档。

## 手动显式调用

```text
请启用 sdd-riper-one。
先澄清最终目标，生成或引用 codemap/context，拆分最小混沌单元，落盘 spec。
未到 Plan Approved 前不要执行代码修改。
```

## 失效表现

- 直接进入代码。
- 没有 spec path。
- 没有 phase / approval status。
- 没有最终目标和任务单元评估。
- 不问用户就跨 Scope。
- 没有 Plan Approved 就执行。
- 完成后没有 Review / Validation / Handoff。

出现这些表现时，回读 `SKILL.md`、`mode-selection.md` 和 `anti-context-decay.md`。

若这些失效在 new chat 中反复出现，建议建立项目级或系统级默认 prompt 文档；只写最小路由和底线，不复制完整 skill。
