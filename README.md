# SDD-RIPER Light: Control Plane for Coding Agents

[English](./README.md) | [简体中文](./README.zh-CN.md)

> Code is cheap. Context, control, and evidence are not.
>
> Let the model move the work forward. Let the human own goals, boundaries, permissions, checkpoints, evidence, and acceptance.

Strong coding agents no longer stop at suggestions. They can read a repository, change multiple files, run tools, validate results, and move an engineering task forward. Once the model can act, the bottleneck shifts from producing code to keeping the work aligned, observable, recoverable, and provable.

SDD-RIPER is a small, repo-native harness for that control problem. It is not a magic prompt and it is not heavyweight spec-driven development. It gives strong agents a durable working surface without turning every task into process theater.

| Human Owns | Agent Owns | Project Preserves |
| --- | --- | --- |
| Goals, boundaries, permissions, checkpoints, acceptance | Exploration, implementation, iteration, tool use | Specs, context indexes, validation evidence, recovery state, reusable knowledge |

Start here: [use the light skill](./skills/sdd-riper-one-light/README.md) · [understand the thesis](./docs/code-is-cheap.md) · [open the docs map](./docs/README.md)

The default entry is [`sdd-riper-one-light`](./skills/sdd-riper-one-light/SKILL.md). Use the heavier [`sdd-riper-one`](./skills/sdd-riper-one/SKILL.md) when the task needs stricter gates, denser artifacts, or training/audit-ready traces.

The repository is organized around four complementary skills:

- `sdd-riper-one-light` and `sdd-riper-one` control execution, checkpoints, validation, and reverse sync.
- `codemap` turns unfamiliar code into an agent-facing context index.
- `new-chat-ready` preserves recovery context for new chats, handoffs, and long pauses.

## Quick Start

Use this prompt for ordinary coding or documentation work:

```text
Use sdd-riper-one-light for this task.
Do not change files yet.

First give me:
- your understanding of the task
- the core goal for this loop
- a minimal spec / summary
- Done Contract: what counts as done, and what proves it
- next actions
- risks
- validation method

Wait for my approval before execution.
```

For unfamiliar code, first ask for a CodeMap:

```text
Use codemap.
Create a feature-level or project-level code terrain index before planning changes.
Focus on entry points, call chains, risk points, validation entry points, and the smallest code slice to read next.
```

For a fresh-chat handoff:

```text
Use new-chat-ready.
Create a concise resume pack.
First check whether this agent can create a Codex thread directly. If it can, create the new conversation and send the compact continuation prompt there; otherwise give me a paste-ready fallback prompt.
Also scan and tidy reusable project knowledge so future chats stay small, but do not commit memory/spec/handoff files unless I explicitly approve.
```

## Which Skill To Use

These four skills share the same context principle: keep active context small, persist durable state outside the chat, and load only the slice needed for the next decision.

| Skill | Use When | Output |
| --- | --- | --- |
| [`sdd-riper-one-light`](./skills/sdd-riper-one-light/) | Daily coding, docs, bugfixes, ordinary refactors, strong-model work | Same core controls with low-friction checkpoints, minimal spec, validation, reverse sync |
| [`sdd-riper-one`](./skills/sdd-riper-one/) | High-risk work, multi-file refactors, audit, training, complex handoff | Same core controls with explicit RIPER gates, fuller spec, denser artifacts, stronger blocking |
| [`codemap`](./skills/codemap/) | Unfamiliar codebases, legacy systems, large modules, cross-repo tasks | Agent-facing code terrain index |
| [`new-chat-ready`](./skills/new-chat-ready/) | New chat, resume pack, handoff, context compression, recovered sessions | Compact handoff, optional direct Codex thread creation, next-chat prompt, project-memory sync scan |

## Minimal Agent Setup

For Codex, Claude Code, and other agentic coding environments, the smallest useful repo layout is:

```text
<repo>/
  AGENTS.md
  skills/
    codemap/
    new-chat-ready/
    sdd-riper-one-light/
    sdd-riper-one/
```

Recommended defaults:

- Put repo-specific rules in `AGENTS.md`.
- Put personal or team-wide defaults in a system-level `AGENTS.md`; use [`examples/global-agents.md`](./examples/global-agents.md) as the template.
- Use `sdd-riper-one-light` by default.
- Add `codemap` before planning changes in unfamiliar or large code.
- Use `new-chat-ready` before long pauses, context resets, or handoffs.
- Switch to `sdd-riper-one` for high-risk or audit-heavy work.

## Core Workflow

```text
read context -> restate goal and risk -> checkpoint -> execute -> validate -> reverse sync
```

The harness keeps a few hard rules:

- **Restate First**: restate the task before planning or changing files.
- **No Spec, No Code**: create or update a minimal source of truth before implementation.
- **No Approval, No Execute**: wait for explicit approval before code changes or high-impact actions.
- **Done by Evidence**: completion must be proven by tests, logs, screenshots, manual checks, or equivalent evidence.
- **Reverse Sync**: write verified conclusions back into the spec, handoff, docs, or project memory when appropriate.

## Spec And Memory Boundaries

There are three different layers. Do not mix them.

| Layer | Purpose | Typical Location |
| --- | --- | --- |
| Feature spec / handoff | Current task truth, decisions, progress, validation, resume state | `mydocs/specs/*`, `mydocs/handoff/*`, or project conventions |
| Project knowledge / memory | Stable facts, repeated pitfalls, reusable validation commands, project-specific rules | `PROJECT_KNOWLEDGE.md`, `PROJECT_SPEC.md`, `PROJECT_MEMORY.md`, `mydocs/project/*`, or files indexed by `AGENTS.md` |
| System-level defaults | Personal or team-wide agent routing and safety boundaries | system `AGENTS.md`, [`examples/global-agents.md`](./examples/global-agents.md) |

Important privacy rule:

- The project or human defines the knowledge topology. SDD detects `Project Sync Candidate`s and routes them according to `AGENTS.md` or explicit user instruction.
- Agents may proactively detect reusable knowledge and propose a `Project Sync Candidate`.
- Agents must not stage or commit system-level knowledge, feature specs, handoffs, project memory, or user preference memory by default.
- Commit those files only when the user explicitly asks, the target repository is appropriate, and the content has been sanitized for that repository.

## Repository Hygiene

This repository is public and reusable. Keep it clean:

- Do not commit runtime data: `.agent-memory/`, `.expcap/`, SQLite files, Milvus Lite data, traces, episodes, candidates, assets, or local cache directories.
- Do not commit `.env`, credentials, tokens, API keys, private logs, personal paths, or user data.
- Do not edit `.gitignore` just to force local artifacts into the repo.
- Sanitize examples before committing: preserve the problem shape and reasoning, remove private names, URLs, IDs, logs, secrets, and user data.
- For `expcap`, prefer user-cache storage such as `EXPCAP_STORAGE_PROFILE=user-cache` and `EXPCAP_HOME="$HOME/.expcap"`.

## Multi-Repo Work

For frontend/backend or microservice work, do not let the model ingest every repository at once.

Start with a project registry:

```text
MULTI / multi-project

This workspace contains multiple repositories.
First discover projects and create a Project Registry.
Do not read all code at once.
Identify the main project, related projects, active_project, and change_scope.
Default to local. Before cross-project edits, stop at a checkpoint and wait for approval.
```

See [`skills/sdd-riper-one/references/multi-project.md`](./skills/sdd-riper-one/references/multi-project.md) for the fuller protocol.

## Repository Map

| Path | What It Is |
| --- | --- |
| [`AGENTS.md`](./AGENTS.md) | Project-level agent rules for this repository |
| [`examples/global-agents.md`](./examples/global-agents.md) | System-level / personal `AGENTS.md` template |
| [`skills/sdd-riper-one-light`](./skills/sdd-riper-one-light/) | Default daily harness |
| [`skills/sdd-riper-one`](./skills/sdd-riper-one/) | Strict control protocol |
| [`skills/codemap`](./skills/codemap/) | Code terrain indexing skill |
| [`skills/new-chat-ready`](./skills/new-chat-ready/) | New-chat handoff and project-memory sync skill |
| [`docs/README.md`](./docs/README.md) | Docs map and reading path |
| [`protocols/`](./protocols/) | Older protocol references |

## Reading Path

If you want the shortest useful path:

1. Read [`skills/sdd-riper-one-light/README.md`](./skills/sdd-riper-one-light/README.md).
2. Try one real task with the quick-start prompt.
3. Use [`codemap`](./skills/codemap/SKILL.md) on unfamiliar code.
4. Read [`skills/sdd-riper-one/README.md`](./skills/sdd-riper-one/README.md) when you need stricter gates.
5. Use [`docs/README.md`](./docs/README.md) only when you want the long-form articles.

The long-form reading path contains three documents with distinct roles. See the [docs map](./docs/README.md) for the maintained index.

| Document | Core Question |
| --- | --- |
| [Code is cheap. Don't write any.](./docs/code-is-cheap.md) | Why AI coding shifts engineering value from producing code to controlling goals, context, checkpoints, validation, and risk |
| [Hands-on AI Coding Harness](./docs/ai-coding-harness-guide.md) | How to slice tasks, control context, use codemap, validate output, and leave recoverable state |
| [General-purpose agents are a trap](./docs/general-purpose-agents-are-a-trap.md) | Why capability-specific agents, explicit flows, business APIs, and necessary hardcode often solve real user problems more reliably than vague universality |

## Core Claim

The important move is not to make AI a more obedient coding assistant.

The important move is to accept that the model can now move the event forward, then build a control plane around that agency.

That is the purpose of SDD-RIPER Light.
