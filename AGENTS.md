# AGENTS.md

This repository is designed to be used with coding agents. The goal of this file is to make the project easy for an agent to enter, safe to edit, and easy for a human to review.

本文件是脱敏后的公开版项目地形说明。它不是业务私有规则，也不绑定某台机器、某个账号或某个模型。

## Project Knowledge

Before synchronizing README, skills, `AGENTS.md`, or mirror copies, read [`PROJECT_KNOWLEDGE.md`](./PROJECT_KNOWLEDGE.md). It records the sanitized repository network, mirror boundaries, downstream Aone skill repositories, and the update checklist.

## Default Workflow

For everyday coding-agent work, prefer the light workflow first:

- Use `sdd-riper-one-light` for normal coding, documentation, bugfix, refactor, and agentic coding tasks.
- Use `sdd-riper-one` when the task is high-risk, multi-file, cross-module, audit-heavy, or needs explicit handoff.
- For tiny questions or trivial edits, a full protocol is not required.

Core loop:

```text
read context -> restate goal and risk -> checkpoint -> execute -> validate -> reverse sync
```

## Task Package

Do not start from only “implement this” or “fix this”. Before substantial edits, package the task with:

```text
Goal: what should be completed.
Context: what files, docs, logs, specs, or tests should be read first.
Boundary: what may be changed and what should not be touched.
Validation: what evidence proves the task is done.
Recovery: what should be documented or remembered after completion.
```

For small tasks, this can be a few lines. For risky tasks, turn it into a micro spec.

## Before Editing

Before changing code, provide a short checkpoint:

```text
1. Files to change
2. Why these files
3. Minimal implementation plan
4. Explicit non-goals
5. Validation command or evidence
```

If the task is documentation-only and low risk, edits can proceed directly after reading the relevant context.

## Validation

Do not summarize a task as done without evidence.

After edits, report:

```text
1. What changed
2. What validation ran
3. Validation result
4. What target behavior is covered
5. What risk remains uncovered
6. Whether README, AGENTS, skill docs, specs, or examples need updates
```

Use the smallest meaningful validation command first. Broaden validation when the change touches shared behavior or cross-module contracts.

## Reverse Sync

If a task reveals durable knowledge, do not leave it only in chat history.

Consider updating:

- `README.md` or `README.zh-CN.md` for public user-facing behavior.
- `AGENTS.md` for project-level routing, validation expectations, safety rules, and indexed long-lived knowledge entrypoints.
- `skills/*/README.md` or `skills/*/SKILL.md` for agent workflow behavior.
- `skills/*/references/` for reusable protocol details.
- `skills/*/examples/` for sanitized examples.
- Root-level project knowledge files such as `PROJECT_KNOWLEDGE.md`, `PROJECT_SPEC.md`, or `PROJECT_MEMORY.md` when a project uses them.
- `mydocs/project/PROJECT_SPEC.md`, `mydocs/project/PROJECT_MEMORY.md`, or `mydocs/project/PROJECT_INDEX.md` for stable project truth, reusable experience, and durable indexes.
- Feature specs or checklists when the change introduces a repeatable decision or risk.

The goal is to turn useful one-time agent work into reusable project terrain.

When a conversation reveals stable, reusable, cross-task knowledge, record it as a Project Sync Candidate instead of leaving it only in chat. If the fact is task-local, keep it in the active feature spec or handoff. If it is project-level memory, sync it to the project knowledge entrypoint after confirmation, with source evidence and scope.

System-level knowledge, feature specs, handoffs, Project Memory, Project Spec, and user preference memory may contain private or internal information. Do not stage or commit them by default. Only commit them when the user explicitly asks, the target repository is appropriate, and the content has been sanitized for that repository.

## Skill Map

- `skills/sdd-riper-one-light/`
  - Default lightweight harness for strong coding agents; low-friction implementation of the shared SDD / Code is cheap control primitives.
  - Best for daily coding, fast iteration, checkpoint-based execution, and reverse sync.
- `skills/sdd-riper-one/`
  - Heavy implementation of the same core controls: restate, spec truth, checkpoint, approval, validation, reverse sync, handoff, and end-to-end closure.
  - Best for complex, high-risk, cross-module, audit, training, handoff-heavy work, or tasks that need denser artifacts.
- `skills/new-chat-ready/`
  - Cross-cutting handoff layer for fresh chats, resume packs, paste-ready continuation prompts, and project-level Markdown memory sync.
  - Best when context is long, a task pauses, another agent/session must continue without losing state, or durable knowledge should be synchronized.

## Safety And Hygiene

- Do not commit local runtime data, memory stores, vector databases, credentials, or traces.
- Do not commit `.agent-memory/`, `.expcap/`, local SQLite files, Milvus Lite data, `.env`, or machine-specific paths.
- Keep examples sanitized: preserve the problem shape and reasoning, remove private project names, internal URLs, secrets, logs, IDs, and user data.
- Prefer small, reviewable edits over broad rewrites unless the task explicitly calls for a rewrite.
- Do not revert unrelated user changes.

## Writing Style

For public docs:

- Prefer concrete actions over slogans.
- Show the smallest usable workflow before the full theory.
- When introducing a concept like checkpoint, spec, codemap, or reverse sync, include a short example.
- Keep Chinese docs natural and readable; avoid making them sound like generated policy text.
