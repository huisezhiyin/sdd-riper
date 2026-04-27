# SDD-RIPER Light: AI Agent Harness

[English](./README.md) | [简体中文](./README.zh-CN.md)

> Let the model become the actor that moves the event forward, while the human owns direction, boundaries, evidence, and acceptance.
> Stop digging every canal in advance. Let the water spread, find its riverbed, then farm beside the river it discovers.

---

## In 30 Seconds

**SDD-RIPER** is not traditional heavyweight spec-driven development.

Traditional SDD often treats the spec as an operating system for the model: write a complete blueprint first, then ask the model to follow it. SDD-RIPER keeps the useful part, but changes the center of gravity: **the spec is a minimal source of truth for humans first**. It records goals, boundaries, decisions, validation, and recovery context.

The default entry point of this repository is [`sdd-riper-one-light`](./skills/sdd-riper-one-light/SKILL.md).

It is not a weaker version. It is a daily **AI Agent Harness** for strong coding models:

- Let the model decompose, explore, fail, recover, and push the work forward.
- Let the human control direction, scope, pace, risk, and acceptance.
- Use a minimal spec, checkpoints, approval, validation, and reverse sync to make a non-deterministic model observable, recoverable, and handoff-ready.

In one sentence:

> **AI is the event actor. Human owns the control plane. Harness is how the two cooperate.**

---

## The Mindset Shift

### From Digging Canals to Farming Beside the River

Before large language models, software work looked more like canal engineering: humans designed the path, then moved water into their own fields.

In the model era, the water can move. A stronger approach is not to pre-dig every path. Let the water spread first, explore, and find the riverbed. The human then adjusts position, sets gates, builds levees, validates outcomes, and farms along the river that actually forms.

That is the difference between a light harness and a heavy process:

| Paradigm | Human role | Model role | Control method |
| --- | --- | --- | --- |
| Traditional software engineering | Person who predefines the path | Tool | Process, standards, code review |
| Heavy SDD | Person who writes the blueprint | Builder following the plan | Large spec, phase gates |
| SDD-RIPER Light | Operator who moves with the flow | Actor exploring the route | Checkpoints, evidence, reverse sync |

### From Assistant to Event Actor

A strong model is no longer just an assistant that fills in code. It proposes paths, tries approaches, exposes risks, and moves the task forward.

The relationship is closer to a rider and a racehorse. The horse is not a passive tool. On the track, its speed, force, and local judgment are the main engine. The rider does not move the horse's legs. The rider chooses the track, controls pace, watches risk, gives signals, and judges the finish.

`sdd-riper-one-light` accepts that agency. It lets the model be the main force while keeping the human in control. A harness does not bind the model back into an old workflow. It makes the collaboration observable, gated, verifiable, and reusable.

---

## Default Entry: sdd-riper-one-light

For everyday coding and agentic coding, start here:

[`skills/sdd-riper-one-light/SKILL.md`](./skills/sdd-riper-one-light/SKILL.md)

It keeps only a few hard constraints, but they matter:

- **Restate First**: restate the task before planning or changing code.
- **Core Goal as Loop Anchor**: every loop has a current core goal.
- **No Spec, No Code**: create or update the minimal source of truth before implementation.
- **No Approval, No Execute**: give a checkpoint and receive approval before code changes.
- **Done by Evidence**: completion is proven by tests, logs, manual checks, or external feedback, not by the model saying it is done.
- **Reverse Sync**: write verified results back into the spec so the next loop can resume.

Minimal start template:

```text
Use sdd-riper-one-light for this task.
Do not change code yet.

First give me:
- Your understanding of the task
- The core goal for this loop
- A minimal spec / summary
- Done Contract: what counts as done, and what proves it
- Next actions
- Risks
- Validation method

Wait for my approval before execution.
```

## Minimal Agent Setup

For most agentic coding environments, the smallest setup that already works well is:

```text
<repo>/
  AGENTS.md
  skills/
    sdd-riper-one-light/
    sdd-riper-one/
```

- Put `AGENTS.md` at the repository root for workspace-level defaults.
- Put `sdd-riper-one-light` and `sdd-riper-one` under `skills/`.
- Use `sdd-riper-one-light` as the default daily entry.
- Switch to `sdd-riper-one` for refactors, audit, handoff, and higher-risk work.

This structure works well in Codex App, Claude Code, and many other agent setups that can read repository instructions plus local skill folders.

In practice, this is usually enough:

```text
Please enable $sdd-riper-one-light.
Do not change code yet.
First give me your understanding, the core goal, a minimal spec / summary, risks, and validation method.
```

## Repository Hygiene

This repository is meant to be safe as a public, reusable agent workspace.

- Keep generated runtime data out of the repo: `.agent-memory/`, `.expcap/`, SQLite files, Milvus Lite data, traces, episodes, candidates, and assets.
- Prefer `EXPCAP_STORAGE_PROFILE=user-cache` with `EXPCAP_HOME="$HOME/.expcap"` when using `expcap`.
- Do not commit machine-specific paths such as personal home directories.
- Sanitize docs before committing: remove private project names, internal URLs, credentials, logs, IDs, and user data.
- Rename downloaded duplicate files such as `name (1).md` before committing, or leave them ignored.

## Multi-Repository / Temporary Workspace Usage

For microservices, frontend/backend work, or temporary workspaces with several repositories, the core question is not where the chat starts. The real question is **how context is sliced, focused, switched, and closed**.

There are three common modes:

- **Start in the main repository**: if the task mainly belongs to one repo, such as `order-service`, start there. Let the agent inspect other repos only when it needs contracts, call chains, or related context, then bring back a concise summary.
- **Start at the parent workspace**: if the task is naturally cross-repo, such as frontend/backend API changes or multiple service contracts, start at the parent workspace. The agent should first build a `Project Registry`, then read and act project by project.
- **Split into multiple single-repo tasks**: if each repo has a clear local change and only release/integration ties them together, run separate repo tasks and do contract alignment at the end.

Recommended rules:

- The parent directory can be the entry point, but the model should not ingest every repository at once.
- A single repo can be the entry point, but cross-repo context must be introduced explicitly.
- Multi-repo work should start with a `Project Registry`: path, role, relevance, current `active_project`, and scope.
- Default to `change_scope=local` for each loop.
- Enter `CROSS / cross-project` only when cross-repo edits are explicitly needed.
- Each relevant project should have its own CodeMap; cross-project work should add an interface contract or flow summary.

Minimal start example:

```text
MULTI / multi-project

This workspace contains multiple repositories.
First auto-discover projects and create a Project Registry.
Do not read all code at once.
Identify the main project, related projects, active_project, and change_scope.
Default to local. Before cross-project edits, stop at a checkpoint and wait for approval.
```

See [`skills/sdd-riper-one/references/multi-project.md`](./skills/sdd-riper-one/references/multi-project.md) for the fuller multi-project rules. Today `create_codemap` can generate CodeMaps inside `sdd-riper-one`; in the future it also makes sense to split a dedicated `codemap` skill with fixed templates to reduce model-to-model variation.

---

## The Standard Entry Still Matters

[`sdd-riper-one`](./skills/sdd-riper-one/SKILL.md) is not obsolete.

It is heavier and more explicit, which makes it useful when:

- A team is just building AI coding discipline.
- The model is unstable and needs a stronger floor.
- The task involves complex refactoring, cross-project coordination, or long handoff chains.
- You need auditable `Research -> Plan -> Execute -> Review` gates.
- The organization is not ready to treat the model as an event actor yet.

In practice:

- **New-era users** default to `sdd-riper-one-light` to release the model's exploration ability.
- **Old-era users** can start with `sdd-riper-one` for a more explicit workflow.
- **High-risk tasks** can temporarily switch back to the standard control protocol.

---

## What Is in This Repository

| Asset | Role |
| --- | --- |
| [`skills/sdd-riper-one-light`](./skills/sdd-riper-one-light/) | Main Light Harness; the default daily entry |
| [`skills/sdd-riper-one`](./skills/sdd-riper-one/) | Standard control protocol for training, audit, handoff, and complex tasks |
| [`protocols/SDD-RIPER-ONE.md`](./protocols/SDD-RIPER-ONE.md) | Standard protocol text |
| [`protocols/RIPER-DOC.md`](./protocols/RIPER-DOC.md) | Document generation and maintenance protocol |
| [`protocols/RIPER-5.md`](./protocols/RIPER-5.md) | Earlier and stricter RIPER reference |
| [`docs/团队落地指南.md`](./docs/团队落地指南.md) | Team adoption and governance guide |
| [`docs/如何快速从零开始落地大模型编程 -- 手把手教程.md`](./docs/如何快速从零开始落地大模型编程%20--%20手把手教程.md) | Step-by-step onboarding guide |

---

## How to Read

If you already use strong coding models:

1. Read [`sdd-riper-one-light`](./skills/sdd-riper-one-light/README.md).
2. Run one real task with the minimal start template.
3. For complex work, read [`sdd-riper-one`](./skills/sdd-riper-one/README.md).

If you are adopting this in a team:

1. Make Light Harness the default entry.
2. Keep the standard control protocol for high-risk work.
3. Use the [team adoption guide](./docs/团队落地指南.md) to align on checkpoints, approval, and evidence.

If you care about the underlying thinking:

| Document | Core question |
| --- | --- |
| [From traditional programming to model-era programming](./docs/从传统编程转向大模型编程.md) | Why the human role must change |
| [AI-native engineering paradigm](./docs/AI%20原生研发范式：从%22代码中心%22到%22文档驱动%22的演进.md) | Why spec is an engineering asset for humans first |
| [Harness Engineering from toy to productivity](./docs/从玩具到生产力：用真实项目讲透%20AI%20Agent%20的%20Harness%20Engineering.md) | How to turn agent experiments into production workflows |
| [Handing engineering tasks to agents](./docs/把工程任务交给%20Agent：大模型时代程序员的身份与能力往哪迁移.md) | What engineers should own when agents execute more work |
| [Claude Code source walkthrough](./docs/Claude%20Code%20源码拆解：从启动到多%20Agent%20扩展层.md) | What a real agent runtime can teach about harness design |
| [Team adoption guide](./docs/团队落地指南.md) | How a personal technique becomes organizational capability |

---

## Core Claim

In the model era, the important move is not to make AI a more obedient coding assistant.

The important move is to **accept that the model has become an event actor, then build a control plane for that agency**.

`sdd-riper-one-light` does not reduce control. It moves control from "predefine every step" to "gate the critical moments."

That is the point of Harness Engineering.
