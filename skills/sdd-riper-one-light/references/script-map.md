# Script Map

`sdd-riper-one-light` 的脚本只处理可重复、容易遗漏的确定性检查。不要让脚本替代 agent 的代码理解和工程判断。

| 场景 | 脚本 | 允许直接调用 | 输入 | 输出 |
|---|---|---|---|---|
| new chat 默认 prompt 检查 | `scripts/default_prompt_check.py --root <project> --mode light` | 是 | 项目根目录 | Markdown/JSON 报告，包含是否缺少 skill 路由、建议目标文件、最小补充片段 |
| 用户批准后写入默认 prompt | `scripts/default_prompt_check.py --root <project> --mode light --apply --target AGENTS.md` | 是，但必须先获用户批准 | 项目根目录、目标文件 | 创建或追加最小 `AI Coding Harness` 段落 |

约束：

- 不检查不可见的系统级 prompt；脚本会提醒需要询问用户。
- 不复制完整 skill。
- 不覆盖现有文件，只创建或追加最小段落。
- 如果已有等价路由，默认不写入。
