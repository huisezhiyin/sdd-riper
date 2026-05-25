# Project Markdown Sync

Use this when a handoff reveals durable knowledge that future agents or humans should not have to rediscover.

This is not a transcript archive. It is a small, reviewable sync from the current conversation, recovered logs, active spec, codemap, validation evidence, and diff into project-level Markdown.

## What Belongs Here

Sync only reusable knowledge:

- project-specific agent instructions or repeated user corrections;
- setup, build, test, debug, and validation commands that are stable;
- stable domain concepts, business invariants, module boundaries, and architecture decisions;
- recurring pitfalls, known failure modes, and verified fixes;
- reusable patch patterns or migration rules;
- links to active project/feature specs, codemaps, and handoffs that future agents should read first.

Do not sync:

- one-off task execution logs;
- temporary dirty state;
- unverified assumptions;
- raw chat transcripts;
- secrets, tokens, `.env`, credentials, or private personal context;
- details that belong only in the active Feature Spec or handoff.

## Target Files

- `AGENTS.md`: agent routing, repo-specific boundaries, required workflows, repeated corrections, validation expectations, safety rules.
- `README.md`: human-facing setup, usage, build/test commands, project overview, stable operational workflows.
- `mydocs/project/PROJECT_SPEC.md`: long-lived project truth, domain model, module boundaries, invariants, architecture rules, validation entry points.
- `mydocs/project/PROJECT_MEMORY.md`: reusable experience, pitfalls, debugging paths, known traps, effective repair patterns.
- `mydocs/project/PROJECT_INDEX.md`: links to important specs, codemaps, handoffs, archives, and where to start for common tasks.
- `mydocs/codemap/*`: code terrain indexes. Do not place code navigation facts in Project Memory when they belong in a CodeMap.

If a project uses different conventions, follow the existing local structure.

## Decision Rules

Before writing, classify each candidate:

```text
Candidate:
- Knowledge:
- Source evidence:
- Target file:
- Why reusable:
- Confidence: confirmed / inferred / unknown
- Action: write / propose / skip
```

Write directly only when:

- the user explicitly asked to update project docs; or
- the current approved task includes reverse sync / documentation updates; and
- the target file and section are clear.

Otherwise propose candidates and ask before editing.

## Workflow

1. Collect durable candidates from the handoff, recovered logs, spec, codemap, diff, validation, and explicit user corrections.
2. Filter out task-local facts that belong in Feature Spec / handoff.
3. Pick target files by content type.
4. Read existing target sections before editing.
5. Patch only the smallest relevant section; preserve existing style and headings.
6. Add source links or evidence notes when useful, but do not paste long transcripts.
7. Report what was synced, skipped, and left as candidate.

## Output Shape

```text
Project MD Sync:
- Synced:
  - <target file>: <what changed>
- Candidates not synced:
  - <candidate>: <why not>
- Skipped:
  - <item>: <reason>
- Next project docs to read:
  - <path>
```
