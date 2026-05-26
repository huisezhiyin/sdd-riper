# Project Markdown Sync

Use this for every `new-chat-ready` handoff. Every handoff must scan for durable knowledge that future agents or humans should not have to rediscover.

This is not a transcript archive. It is a small, reviewable sync from the current conversation, recovered logs, active spec, codemap, validation evidence, and diff into project-level Markdown. If the project exposes root-level knowledge files such as `PROJECT_KNOWLEDGE.md`, `PROJECT_MEMORY.md`, `PROJECT_SPEC.md`, or equivalents indexed by `AGENTS.md`, treat them as the preferred long-lived memory layer.

Core rule:

```text
Project MD Sync Scan is mandatory.
Project MD Sync Write is conditional.
```

Even when nothing is written, report `Synced`, `Candidates not synced`, and `Skipped` so the next chat knows the scan happened.

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
- `PROJECT_KNOWLEDGE.md`: stable project facts, decision context, operating model, and high-level knowledge that future agents should read first.
- `PROJECT_SPEC.md`: long-lived project truth when the repo uses root-level spec files instead of `mydocs/project/`.
- `PROJECT_MEMORY.md`: reusable experience and recurring pitfalls when the repo uses root-level memory files instead of `mydocs/project/`.
- `mydocs/project/PROJECT_SPEC.md`: long-lived project truth, domain model, module boundaries, invariants, architecture rules, validation entry points.
- `mydocs/project/PROJECT_MEMORY.md`: reusable experience, pitfalls, debugging paths, known traps, effective repair patterns.
- `mydocs/project/PROJECT_INDEX.md`: links to important specs, codemaps, handoffs, archives, and where to start for common tasks.
- `mydocs/codemap/*`: code terrain indexes. Do not place code navigation facts in Project Memory when they belong in a CodeMap.

If a project uses different conventions, follow the existing local structure. First inspect `AGENTS.md` for indexed project knowledge files, then check for root-level `PROJECT_*` files, then fall back to `mydocs/project/*`.

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

## Commit Boundary

Project MD Sync files may contain internal project facts, feature-level context, user preferences, or private operational knowledge. Updating a file is not the same as committing it.

- Do not stage or commit system-level knowledge, feature specs, handoffs, Project Memory, Project Spec, or user preference memory by default.
- Before committing any memory/spec/handoff/project-knowledge file, confirm that the user wants it committed and that the content is sanitized for the target repository.
- For public repositories, default to reporting candidates or keeping local artifacts uncommitted unless the user explicitly approves publication.
- If privacy risk is unclear, skip the write or leave the file untracked and report the reason.

If no reusable knowledge is found, still report the scan:

```text
Project MD Sync:
- Synced: none
- Candidates not synced: none
- Skipped:
  - No durable project-level knowledge found in this handoff.
```

## Workflow

1. Always scan the handoff, recovered logs, spec, codemap, diff, validation, and explicit user corrections.
2. Inspect project knowledge entrypoints: `AGENTS.md` indexes, root `PROJECT_KNOWLEDGE.md` / `PROJECT_MEMORY.md` / `PROJECT_SPEC.md`, and `mydocs/project/*`.
3. Collect durable candidates.
4. Filter out task-local facts that belong in Feature Spec / handoff.
5. Pick target files by content type.
6. Read existing target sections before editing.
7. Patch only the smallest relevant section; preserve existing style and headings.
8. Add source links or evidence notes when useful, but do not paste long transcripts.
9. Report what was synced, skipped, and left as candidate.

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
