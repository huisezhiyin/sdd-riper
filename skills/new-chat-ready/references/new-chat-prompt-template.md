# Paste-Ready New Chat Prompt Template

Use this as the final section of a handoff, or as the message sent into a newly created Codex thread. The agent should first check whether it can create/send to a Codex thread directly; this template is the thread payload when direct creation is available, and a paste-ready fallback only when direct creation is unavailable, unsafe, or explicitly not wanted.

Compression rules:

- Aim for 20-40 lines; stay under about 60 lines unless safety requires more.
- Prefer paths and commands over narrative history.
- Include only sources the next agent should read first.
- Do not duplicate long details already stored in the handoff/spec/project docs.
- If a Codex thread was created automatically, this prompt should still be portable for manual paste.
- Do not generate a manual-only prompt until the capability check has ruled out direct creation.

```text
默认用中文交流；用户、项目或目标文档明确使用其他语言时，跟随更具体的语言要求。

请接着这个任务继续，不要从零开始。

Workspace:
<absolute workspace path>

Active instructions to read first:
- <AGENTS.md or equivalent>
- <project knowledge/spec/memory only if directly relevant>
- <active spec/handoff/codemap path>

Recovered context sources:
- <current chat or local log/session path, if recovery was used>

Current goal:
<one-sentence goal>

Current state:
- Confirmed: <key confirmed facts>
- Inferred: <key inferences to re-check>
- Unknown: <open gaps>

Files and dirty state:
- <path>: <state and why it matters>

Git protection:
- <snapshot branch>@<commit SHA>; <remote status>; <remaining excluded dirty paths>

Validation so far:
- <command/evidence>: <result and coverage>

Constraints:
- <approval, safety, privacy, non-goals, files not to touch>

Project memory:
- <synced/proposed/skipped project docs, one line>

Next action:
1. <first concrete action>
2. <second concrete action>
3. <validation/checkpoint>

Important: continue in the protected local snapshot branch, preserve existing user changes, do not create/delete worktrees or branches unless explicitly requested, and update the handoff/spec after making progress.
```
