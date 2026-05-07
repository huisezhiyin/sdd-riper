# Script Map

`sdd-riper-one` 的脚本用于确定性检查和重度留痕辅助。脚本负责稳定文件读写和结构化输出，agent 负责目标、边界、风险和用户决策。

| 场景 | 脚本 | 允许直接调用 | 输入 | 输出 |
|---|---|---|---|---|
| new chat 默认 prompt 检查 | `scripts/default_prompt_check.py --root <project> --mode one` | 是 | 项目根目录 | Markdown/JSON 报告，包含 one/light 路由是否缺失、建议目标文件、最小补充片段 |
| 用户批准后写入默认 prompt | `scripts/default_prompt_check.py --root <project> --mode one --apply --target AGENTS.md` | 是，但必须先获用户批准 | 项目根目录、目标文件 | 创建或追加最小 `AI Coding Harness` 段落 |
| 归档沉淀 | `scripts/archive_builder.py --targets <paths> --kind <kind> --audience <audience> --mode <mode> --topic <topic>` | 是 | spec/codemap/context 路径 | human/llm 归档文档 |

约束：

- 不检查不可见的系统级 prompt；脚本会提醒需要询问用户。
- 不复制完整 skill、spec 模板或长理论文章。
- 不覆盖现有文件，只创建或追加最小段落。
- 如果已有等价路由，默认不写入。
- `--apply` 只能在用户明确批准后使用。
