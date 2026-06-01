# Global AGENTS Example

这是一份系统级 / 个人级 `AGENTS.md` 示例，可作为 Codex、Claude Code 或其他 agentic coding 环境的默认规则参考。

建议用途：

- 放到个人全局配置入口，例如 `~/.codex/AGENTS.md`。
- 或作为团队默认 prompt 的最小模板。
- 项目级 `AGENTS.md` 可以在此基础上补充业务边界、验证入口和项目知识入口。

```markdown
# Global AGENTS

默认用中文交流；用户、项目或目标文档明确使用其他语言时，跟随更具体的语言要求。

## Skill 路由

- `codemap`：进入陌生代码库、遗留系统、大模块、跨仓任务，或用户要求 `create_codemap` / `MAP` / 项目总图 / 功能地形图时使用；产物面向 agent，不写成人类架构长文。
- `sdd-riper-one-light`：中等及以上代码任务使用；简单问答、低风险文案、单点机械修改可跳过。
- `sdd-riper-one`：高风险、多文件、跨模块、审计、训练、复杂交接或需要显式阶段门禁时使用。
- `new-chat-ready`：用户表达要 new chat、换对话、handoff、resume pack、上下文压缩、无缝续接时使用；自动整理当前状态、可落盘交接文档，并生成新对话可直接粘贴的 prompt。

## 默认边界

- 主 Codex 会话始终是 owner / decider / implementer / verifier。
- 项目可以同时拥有 feature 级 spec/handoff 和 project 级知识入口（如根目录 `PROJECT_KNOWLEDGE.md`、`PROJECT_MEMORY.md`、`PROJECT_SPEC.md`，或项目 `AGENTS.md` 指向的等价文件）。进入项目、new chat 恢复、debug 或跨任务决策时，优先检查项目 `AGENTS.md` 是否索引了这类 project 级文件；不要只在 `docs/features/` 或单次 handoff 里找长期规则。
- 不要把 `.agent-memory/`、本地 SQLite、Milvus Lite db、trace / episode / candidate / asset 运行数据提交到业务仓库。
- 不要提交 `.env`、API key、token 或其他本地凭据。
- 不主动改动 `.gitignore`，包括主动恢复 `.gitignore`；提交和暂存文件时忠实遵守仓库现有 `.gitignore`。

## 最小记忆能力

- 对话中如果感知到稳定、可复用、跨任务会再次影响判断的系统级经验、项目信息或用户偏好，不要只留在聊天里。
- 优先沉淀到项目已有长期知识入口：根目录 `PROJECT_KNOWLEDGE.md`、`PROJECT_MEMORY.md`、`PROJECT_SPEC.md`，或项目 `AGENTS.md` 明确索引的等价文件。
- 若知识属于当前任务过程，先写入 feature spec / handoff；若属于项目长期规则或反复踩坑，再作为 Project Sync Candidate，经确认后同步到 Project Spec / Project Memory / AGENTS。
- 记录时保持最小、可审查、可溯源：写清事实、来源、适用边界和验证证据；不要写入密钥、私人信息、未验证猜测或整段聊天记录。
- 系统级知识、用户偏好、feature spec、handoff、Project Memory 都可能包含隐私或内部信息；默认只提出候选和建议落点，不主动提交到业务仓库。只有用户明确要求提交，或项目规则明确允许且内容已确认脱敏时，才可以暂存/提交。
- 触发 new chat、handoff、resume pack、上下文压缩或任务收尾时，必须扫描是否有可沉淀知识；没有也要说明“无可同步长期知识”。

详细流程以对应 skill 的 `SKILL.md` 为准，避免把长策略常驻进默认 prompt。
```
