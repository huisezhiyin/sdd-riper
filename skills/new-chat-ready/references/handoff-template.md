# New Chat Handoff: <task>

Keep this document concise. Default target: under about 120 lines. Link to specs, codemaps, commits, logs, and validation output instead of copying long details. If a section has no useful continuity value, write `None` or merge it into a shorter section.

- Created: <YYYY-MM-DD HH:mm timezone>
- Workspace: `<absolute path>`
- Active Skill / Workflow: `<skill or workflow>`
- Recovery Sources: `<current chat | local logs | mixed>` with source paths if recovered
- New Chat Capability Check: `<available | unavailable | skipped for safety>` with tool names or reason
- Git Protection: `<clean anchor | local snapshot | local + remote snapshot | skipped | failed>`
- Snapshot Ref: `<original branch -> snapshot branch @ commit SHA>`
- Remote Protection: `<not requested | skipped | failed | remote/ref>`
- Remaining Dirty State: `<clean | explicitly excluded paths and reason>`
- Delivery Mode: `<created Codex thread | paste-ready prompt | inline-only>` with thread id/link if created
- Current Goal: <one sentence>
- Status: `<not-started | in-progress | blocked | validating | complete>`
- Confidence: `<high | medium | low>` with reason

## 1. Sources

List only sources the next agent should trust or read first.

| Source | Role | Status |
| --- | --- | --- |
| `<path or chat artifact>` | <why it matters> | `<confirmed | stale | unknown>` |

## 2. Current State

Keep this to the shortest facts needed for the next action.

### Confirmed

- <fact grounded in files, commands, or explicit user decisions>

### Inferred

- <reasonable inference that still needs re-checking>

### Unknown

- <gap that should not be silently assumed>

## 3. Decisions And Constraints

- Decision: <what was decided>
  Evidence: <file, command, or user statement>
- Constraint: <boundary, non-goal, approval rule, privacy rule, or repo hygiene rule>

## 4. Files And Changes

| Path | State | Notes |
| --- | --- | --- |
| `<path>` | `<changed | read | generated | user-dirty | untouched>` | <what the next agent must know> |

List only files that affect continuation, validation, or safety. Do not inventory the entire repo.

## 5. Validation

| Command / Evidence | Result | Coverage |
| --- | --- | --- |
| `<command or manual evidence>` | `<pass | fail | not run>` | <what behavior or document state it proves> |

## 6. Open Risks

- <risk, missing validation, unresolved question, or possible conflict>

## 7. Next Action

1. <smallest useful next step>
2. <second step if needed>
3. <validation or checkpoint step>

## 8. Project MD Sync

| Candidate | Target | Status | Evidence |
| --- | --- | --- | --- |
| `<durable knowledge>` | `<AGENTS.md / README.md / PROJECT_KNOWLEDGE.md / PROJECT_SPEC.md / PROJECT_MEMORY.md / PROJECT_INDEX.md>` | `<synced | proposed | skipped>` | `<source>` |

Use this section to keep future prompts short: stable knowledge belongs in project docs or as explicit sync candidates, not repeatedly pasted into every handoff.

## 9. Paste-Ready New Chat Prompt

Paste the compact final prompt here, or link to the generated prompt section/file if it is stored separately. If a Codex thread was created automatically, record the thread id/link and the exact prompt sent.
