# Paste-Ready New Chat Prompt Template

Use this as the final section of a handoff. Keep it compact enough to paste directly into a fresh chat.

```text
默认用中文交流。

请接着这个任务继续，不要从零开始。

Workspace:
<absolute workspace path>

Active instructions to read first:
- <AGENTS.md or equivalent>
- <active spec / handoff / codemap path>
- <other essential source path>

Current goal:
<one-sentence goal>

Current state:
- Confirmed: <key confirmed facts>
- Inferred: <key inferences to re-check>
- Unknown: <open gaps>

Files and dirty state:
- <path>: <state and why it matters>

Validation so far:
- <command/evidence>: <result and coverage>

Constraints:
- <approval, safety, privacy, non-goals, files not to touch>

Next action:
1. <first concrete action>
2. <second concrete action>
3. <validation/checkpoint>

Important: preserve existing user changes, do not revert unrelated work, and update the handoff/spec after making progress.
```
