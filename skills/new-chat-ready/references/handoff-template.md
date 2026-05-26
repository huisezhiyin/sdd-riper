# New Chat Handoff: <task>

- Created: <YYYY-MM-DD HH:mm timezone>
- Workspace: `<absolute path>`
- Active Skill / Workflow: `<skill or workflow>`
- Recovery Sources: `<current chat | local logs | mixed>` with source paths if recovered
- Current Goal: <one sentence>
- Status: `<not-started | in-progress | blocked | validating | complete>`
- Confidence: `<high | medium | low>` with reason

## 1. Sources

List only sources the next agent should trust or read first.

| Source | Role | Status |
| --- | --- | --- |
| `<path or chat artifact>` | <why it matters> | `<confirmed | stale | unknown>` |

## 2. Current State

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

## 9. Paste-Ready New Chat Prompt

Paste the final prompt here, or link to the generated prompt section/file if it is stored separately.
