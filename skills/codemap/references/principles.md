# CodeMap Principles

## Definition

CodeMap is an agent-facing progressive code terrain index.

It is not CodeWiki. CodeWiki explains a codebase for humans. CodeMap routes context for agents.

## Core Idea

Save context attention, not necessarily raw token count.

Do not compress source code into a second-hand summary. Help the agent decide where to look, what chain to follow, what branches to verify, and which evidence to load next.

## Evidence Layers

Use CodeMap as an index layer:

```text
CodeMap: where to look and why
Source code: what is true now
Tests/logs/runtime: what is proven
Spec: what this task should change and how to validate it
```

When CodeMap conflicts with source code, source code wins and the CodeMap should be updated.

## Progressive Disclosure

Structure the map as context tree nodes:

```text
Orientation node
  -> Capability / module / entry nodes
  -> Selected feature or project subtree nodes
  -> Key file, function, class, branch nodes
  -> Evidence and validation nodes
```

The first screen should be small. Deeper nodes should be loaded only when a task needs them.

## Node Contract

Each important node should use a compact, repeatable shape:

- `Node`: stable name for this capability, module, entry, branch, effect, dependency, risk, or validation target.
- `Type`: `project`, `capability`, `module`, `entry`, `flow`, `branch`, `object`, `dependency`, `effect`, `risk`, or `validation`.
- `Status`: `confirmed`, `inferred`, or `unknown`.
- `Purpose`: why this node matters for the next agent.
- `Read First`: source files, symbols, configs, tests, logs, or docs to load first.
- `Edges / Children`: related nodes and why the relationship matters.
- `Evidence`: the source of the relationship, not a paste of the source.
- `Unknowns`: facts that must not be assumed.
- `Validation`: tests, commands, logs, or manual checks that can prove behavior.
- `Next Drill-Down`: what to load only when the next task needs more detail.

Do not make every row in an index a full node. Promote an item to a node only when it helps route future context.

## Relationship Marking

Mark important relationships:

- `confirmed`: verified by source, tests, config, logs, or explicit docs.
- `inferred`: plausible from names or partial links, but not fully traced.
- `unknown`: important but not yet confirmed.

Never hide uncertainty. A useful CodeMap tells the next agent what not to trust yet.

## Boundary

Do not include:

- large source snippets;
- full module documentation;
- generic onboarding prose;
- every file under a directory;
- speculative business history without a source;
- implementation plans that belong in a Spec.

Do include:

- entry points;
- call and effect chains;
- critical branches;
- data and external dependencies;
- source-linked risks;
- validation entry points;
- next drill-down suggestions.
