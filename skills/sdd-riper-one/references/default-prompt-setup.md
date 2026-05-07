# Default Prompt Setup

用于在项目级或系统级默认 prompt 中注入 `sdd-riper-one` / `sdd-riper-one-light` 的路由，让多轮对话和 new chat 后仍能保持 Harness 能力。

## 启动前询问

进入 new chat、新项目会话、首次在项目中启用 one，或发现默认规则缺失时，先检查可见 prompt 文件并询问用户：

```text
是否要为这个项目建立或更新默认 prompt 文档？
可选位置：AGENTS.md（OpenAI/Codex）、CLAUDE.md（Claude Code）、.github/copilot-instructions.md、.cursorrules。
我会只写最小路由和边界，不复制完整 skill。
```

未经用户同意，不要静默创建或修改这些文件。

如果系统级 prompt 不可见，不要声称已经检查系统级配置；只说明已检查可见项目文件，并询问用户是否有系统级规则需要同步。

## 脚本入口

优先用脚本做确定性检查，避免 agent 自己漏文件或误判路由：

```bash
python3 <skill-root>/scripts/default_prompt_check.py --root <project-root> --mode one
```

用户明确批准后，才允许写入：

```bash
python3 <skill-root>/scripts/default_prompt_check.py --root <project-root> --mode one --apply --target AGENTS.md
```

脚本 map 见 `script-map.md`。

## 可写位置

- Codex / OpenAI agent: `AGENTS.md`
- Claude Code: `CLAUDE.md`
- GitHub Copilot: `.github/copilot-instructions.md`
- Cursor: `.cursorrules`
- 系统级 prompt：需要用户明确给出路径、平台或管理方式

## 推荐最小路由

```markdown
## AI Coding Harness

- 复杂、高风险、陌生代码库、需求不清、需要交接/审计的任务，使用 `sdd-riper-one`。
- 日常已拆好的中低风险任务，使用 `sdd-riper-one-light`。
- `sdd-riper-one` 负责澄清最终目标、生成/引用 codemap/context、拆分最小混沌单元、维护完整 spec、阶段门禁和重度留痕。
- `sdd-riper-one-light` 负责目标复述、最小 spec/micro-spec、checkpoint、validation、进度汇报和中度留痕。
- 中等以上任务不要裸改；执行前必须有目标、边界、风险、验证方式和 checkpoint。
- 高风险或不可逆操作必须先暂停并等待用户确认。
- 完成必须由测试、日志、运行结果或人工确认等证据证明。
- 不提交本地记忆、trace、SQLite/Milvus、密钥或机器私有路径。
```

## 不要写入默认 prompt 的内容

- 完整 `SKILL.md`
- 完整 spec 模板
- 长篇理论文章
- 大量案例
- 机器私有路径、密钥、trace、记忆数据库

这些内容放在 skill references 或项目 docs 中按需读取。

## 已存在文档时

如果目标文件已存在：

1. 先读取现有内容。
2. 判断是否已有等价路由。
3. 只追加或更新最小必要段落。
4. 不覆盖用户原有项目规则。
5. 如存在冲突，先列出冲突并等待用户选择。
