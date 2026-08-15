# New Chat Ready Trigger Policy

## Create Immediately

Create a handoff pack when the user explicitly says to:

- start or prepare a `new chat`;
- create/open a new Codex conversation directly when supported;
- generate a `handoff`, `resume pack`, or `续接 prompt`;
- recover a lost Codex / Claude Code conversation before making a handoff;
- summarize the current work for another agent or future session;
- preserve reusable knowledge in project-level Markdown so future chats avoid repeated learning or repeated corrections;
- pause a task and leave recoverable context.

Before choosing the delivery shape, run a new-chat capability check. In Codex, first look for thread-management tools such as `create_thread` and `send_message_to_thread`. If they are available and safe for the current content, direct thread creation is the preferred delivery mode.

Before calling a thread-creation tool, finish the compact handoff and project sync scan, then pass the Git snapshot gate from `git-snapshot-protection.md`. Do not create a new conversation while task-bearing dirty work exists only in a disposable worktree.

## Offer Proactively

Offer a handoff, and create it if the user agrees, when:

- the task is long-running and context has become noisy;
- the next step depends on many scattered decisions;
- validation is incomplete and another session will continue;
- the user appears to be moving from exploration to implementation in a new chat;
- a context compaction or recovery boundary would likely lose important constraints.

## Do Not Create Yet

Do not create a handoff pack when:

- the user is only asking whether the capability should exist;
- the current task is a tiny one-shot answer with no durable state;
- creating files would violate the current workspace boundary;
- the user asks for a normal summary rather than a next-agent execution package.

Do not create a new Codex conversation directly when:

- the runtime does not expose thread-management tools;
- the prompt contains private material that should be reviewed before being sent elsewhere;
- the user asked only for a reusable handoff document or paste-ready prompt;
- the target workspace or branch for the new thread is ambiguous and the choice changes safety.
- a dirty repository has not been protected by a verified local snapshot commit;
- the runtime would require another worktree and the user did not explicitly request one.

## Disambiguation

If the user's wording is ambiguous, ask one short question only when the choice affects persistence or privacy. Otherwise prefer a safe inline handoff and mention that no file was written.

When a handoff touches SDD-RIPER state, preserve the active spec as the source of truth. The new-chat handoff should point to the spec and summarize the next step; it should not fork an alternative truth.

When direct Codex thread creation is available and safe, create the thread and send the compact prompt automatically before offering manual paste. Still keep a paste-ready prompt in the handoff so the continuation is portable across tools.
