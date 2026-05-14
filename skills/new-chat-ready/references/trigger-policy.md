# New Chat Ready Trigger Policy

## Create Immediately

Create a handoff pack when the user explicitly says to:

- start or prepare a `new chat`;
- generate a `handoff`, `resume pack`, or `续接 prompt`;
- summarize the current work for another agent or future session;
- pause a task and leave recoverable context.

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

## Disambiguation

If the user's wording is ambiguous, ask one short question only when the choice affects persistence or privacy. Otherwise prefer a safe inline handoff and mention that no file was written.

When a handoff touches SDD-RIPER state, preserve the active spec as the source of truth. The new-chat handoff should point to the spec and summarize the next step; it should not fork an alternative truth.
