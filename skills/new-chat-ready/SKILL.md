---
name: new-chat-ready
description: Prepare seamless new-chat handoff packs when a user wants to start a fresh chat, continue elsewhere, pause a long task, recover from context decay, recover a lost conversation from local Codex or Claude Code logs, preserve reusable project knowledge in Markdown, or hand work to another agent. Generates a durable handoff document, optional project-level Markdown updates such as AGENTS.md/README.md/PROJECT_SPEC.md/PROJECT_MEMORY.md, and a paste-ready next-chat prompt grounded in current task state, local conversation records, source files, specs, codemaps, validation evidence, open risks, and constraints.
---

# New Chat Ready

## Core Position

This skill turns an active or recoverable past conversation into an execution handoff, optionally starts the next Codex conversation when the runtime supports it, and preserves durable project knowledge without bloating the next context window.

It is not a generic chat summary. It should preserve only the next agent's operating context: the current goal, latest recap checkpoint, workspace, decisions, files, validation evidence, risks, constraints, and the exact next action.

Use it as a cross-cutting handoff layer with SDD-RIPER, CodeMap, expcap, ordinary coding tasks, local conversation recovery, and project-level Markdown sync. SDD skills may route to this skill, but the handoff, recovery, and project sync format lives here.

Project-level sync is part of the core job, not an optional afterthought. Every new-chat handoff should reduce future context load by moving stable project and task knowledge into the right long-lived files, while keeping transient state in the handoff/spec. When a project exposes long-lived knowledge files such as root `PROJECT_KNOWLEDGE.md`, `PROJECT_MEMORY.md`, `PROJECT_SPEC.md`, or equivalents indexed from `AGENTS.md`, prefer those files for stable project truth and reusable memory. Use `AGENTS.md` for routing, boundaries, validation expectations, and safety rules.

## Trigger

Use this skill when the user asks for or implies:

- `new chat`, `fresh chat`, `换对话`, `开新会话`, `另开一轮`
- `handoff`, `resume pack`, `交接`, `接着做`, `无缝续接`
- `上下文快满`, `压缩上下文`, `总结给下个 chat`
- `对话丢了`, `恢复对话`, `找回上次对话`, `从 Codex/Claude 日志恢复`
- `沉淀到项目文档`, `更新 AGENTS/README`, `避免反复踩坑`, `把经验写进项目 memory`
- a durable pause point for a long or risky task

If the user only asks whether this capability is a good idea, answer the design question first. Create a handoff only after the user asks to do it, or when a running task clearly needs a pause/resume artifact.

For detailed trigger boundaries, read `references/trigger-policy.md`.

## Delivery Mode

Prefer the lowest-friction continuation path that the current runtime actually supports:

1. **Direct Codex continuation**: if the environment exposes thread tools such as `create_thread` and `send_message_to_thread`, create the new conversation yourself after the handoff/prompt is ready. Send the compact next-chat prompt into that thread so the user does not need to paste it manually. In Codex, discover these tools with `tool_search` before use when they are not already loaded.
2. **Paste-ready fallback**: if thread tools are unavailable, blocked, or inappropriate for privacy/workspace reasons, output a compact prompt the user can paste manually.
3. **Inline-only fallback**: if writing files is not appropriate, provide an inline handoff and compact prompt, and state that no file or new conversation was created.

Never invent tool availability. If direct creation succeeds, still provide the created thread identifier or link required by the host UI and keep the final visible summary short.

## Workflow

1. Identify the active task, workspace, intended next-chat scope, and whether direct Codex thread creation is available.
2. Gather only evidence needed for continuity:
   - project instructions such as `AGENTS.md`;
   - the latest recap checkpoint if one exists;
   - current spec, handoff, context bundle, or codemap if already active;
   - `git status` and touched files when in a repo;
   - validation commands and results already run;
   - unresolved decisions, blockers, and explicit user constraints.
3. If the active conversation is unavailable, stale, or incomplete, enter `Recovery Mode`:
   - read `references/recovery-from-local-logs.md`;
   - translate the user's natural-language recovery request into search anchors;
   - search local Codex / Claude Code logs and show a short candidate list first;
   - wait for the user to choose candidate session(s) before reading deeply, unless there is exactly one obvious high-confidence match;
   - extract only continuity facts needed for the handoff, not the full transcript.
4. Run a `Context Diet` before writing:
   - keep only facts that affect the next action, validation, safety, or project memory;
   - replace long history with links to source files, specs, codemaps, commits, logs, or commands;
   - separate stable project knowledge from task-local state;
   - delete duplicate explanations between handoff and next-chat prompt.
5. Choose where to persist:
   - If an SDD spec is active, update its `Resume / Handoff` area and optionally create a separate handoff file.
   - Otherwise write `mydocs/handoff/YYYY-MM-DD_hh-mm_<task>_new-chat.md` when the user wants a durable artifact and the workspace is writable.
   - If there is no suitable workspace, output the handoff inline.
6. Start from a short recap checkpoint, then write the handoff using `references/handoff-template.md`.
7. Always run `Project MD Sync Scan` before finishing a handoff:
   - read `references/project-md-sync.md` to classify reusable project knowledge from this conversation, recovered logs, spec, codemap, validation, and diff;
   - first inspect `AGENTS.md` and existing root project knowledge files (`PROJECT_KNOWLEDGE.md`, `PROJECT_MEMORY.md`, `PROJECT_SPEC.md`) to find the local source of truth;
   - treat stable system-level experience, repeated user corrections, durable project facts, reusable debugging/validation knowledge, and knowledge that would otherwise be repeatedly pasted into new chats as sync candidates;
   - prefer small scoped edits or candidate notes over dumping task history into project docs;
   - report `Synced`, `Candidates not synced`, and `Skipped` even when no files are updated;
   - propose `Project MD Sync Candidates` before editing durable project docs unless the user explicitly asked to update them or current approval includes reverse sync;
   - never stage or commit system-level knowledge, feature specs, handoffs, Project Memory, or user preference memory by default; these may contain private/internal content and require explicit user approval plus sanitization before committing;
   - update only scoped sections in project-level Markdown, not task execution logs.
8. Produce a compact next-chat prompt using `references/new-chat-prompt-template.md`.
9. If direct Codex continuation is available and appropriate, create the new thread and send the compact prompt there. Otherwise provide the prompt for manual paste.
10. If expcap is available and the project asks for durable experience capture, run the appropriate finish/save step after the handoff is correct. Do not make expcap a dependency for the handoff.

## Output Rules

- Default to Chinese unless the active project or user uses another language.
- Separate `Confirmed`, `Inferred`, and `Unknown` facts when continuity depends on them.
- Include exact paths for files, specs, codemaps, tests, and validation evidence.
- When recovering from logs, include session/source paths and mark recovered facts as `confirmed from logs`, `inferred from logs`, or `unknown`.
- Do not dump long logs, private data, credentials, tokens, or `.env` contents.
- Do not expose raw transcripts unless the user explicitly asks; summarize and cite local source paths instead.
- Do not claim a task is done unless the handoff includes validation evidence.
- Preserve dirty-work awareness: list existing uncommitted changes, and mark which ones were made by the current agent if known.
- Prefer recap-first handoff: begin with the shortest accurate state summary, then expand only the details needed for continuity.
- Project MD Sync scan is mandatory for every handoff; Project MD Sync write is conditional. Separate durable project knowledge from task-specific state; keep edits small, cited, and reviewable. If no durable knowledge exists, say so explicitly.
- Keep both handoff and prompt compact. Default targets: handoff under about 120 lines, next-chat prompt under about 60 lines. Exceed these only when the next agent would otherwise be unable to continue safely.
- The final next-chat prompt must be directly pasteable even when it is also sent into a created Codex thread. It should tell the next agent what to read first and what to do next, not retell the whole conversation.

## References

- `references/trigger-policy.md`: when to proactively offer or create a new-chat handoff.
- `references/recovery-from-local-logs.md`: how to recover a lost or stale conversation from local Codex / Claude Code records.
- `references/project-md-sync.md`: how to update project-level Markdown so future chats avoid repeated learning and repeated correction.
- `references/handoff-template.md`: durable handoff document shape.
- `references/new-chat-prompt-template.md`: paste-ready prompt for the next chat.
