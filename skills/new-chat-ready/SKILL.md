---
name: new-chat-ready
description: Prepare seamless new-chat handoff packs when a user wants to start a fresh chat, continue elsewhere, pause a long task, recover from context decay, recover a lost conversation from local Codex or Claude Code logs, or hand work to another agent. Generates a durable handoff document and a paste-ready next-chat prompt grounded in current task state, local conversation records, source files, specs, codemaps, validation evidence, open risks, and constraints.
---

# New Chat Ready

## Core Position

This skill turns an active or recoverable past conversation into an execution handoff.

It is not a generic chat summary. It should preserve the next agent's operating context: the current goal, latest recap checkpoint, workspace, decisions, files, validation evidence, risks, constraints, and the exact next action.

Use it as a cross-cutting handoff layer with SDD-RIPER, CodeMap, expcap, ordinary coding tasks, and local conversation recovery. SDD skills may route to this skill, but the handoff and recovery format lives here.

## Trigger

Use this skill when the user asks for or implies:

- `new chat`, `fresh chat`, `换对话`, `开新会话`, `另开一轮`
- `handoff`, `resume pack`, `交接`, `接着做`, `无缝续接`
- `上下文快满`, `压缩上下文`, `总结给下个 chat`
- `对话丢了`, `恢复对话`, `找回上次对话`, `从 Codex/Claude 日志恢复`
- a durable pause point for a long or risky task

If the user only asks whether this capability is a good idea, answer the design question first. Create a handoff only after the user asks to do it, or when a running task clearly needs a pause/resume artifact.

For detailed trigger boundaries, read `references/trigger-policy.md`.

## Workflow

1. Identify the active task, workspace, and intended next-chat scope.
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
4. Choose where to persist:
   - If an SDD spec is active, update its `Resume / Handoff` area and optionally create a separate handoff file.
   - Otherwise write `mydocs/handoff/YYYY-MM-DD_hh-mm_<task>_new-chat.md` when the user wants a durable artifact and the workspace is writable.
   - If there is no suitable workspace, output the handoff inline.
5. Start from a short recap checkpoint, then write the handoff using `references/handoff-template.md`.
6. Produce a paste-ready next-chat prompt using `references/new-chat-prompt-template.md`.
7. If expcap is available and the project asks for durable experience capture, run the appropriate finish/save step after the handoff is correct. Do not make expcap a dependency for the handoff.

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
- The final next-chat prompt must be directly pasteable. It should tell the next agent what to read first and what to do next.

## References

- `references/trigger-policy.md`: when to proactively offer or create a new-chat handoff.
- `references/recovery-from-local-logs.md`: how to recover a lost or stale conversation from local Codex / Claude Code records.
- `references/handoff-template.md`: durable handoff document shape.
- `references/new-chat-prompt-template.md`: paste-ready prompt for the next chat.
