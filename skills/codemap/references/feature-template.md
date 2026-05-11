# Feature CodeMap Template

Use for a capability, feature, bug chain, API flow, function/class-centered task, or any request where the agent must understand one behavior from entry to effect.

Feature CodeMap is depth-first and narrow enough to verify. Its main body should be Context Tree Nodes, not a narrative walkthrough.

Template:

# <Feature / Capability> CodeMap (feature)

## 1. Orientation

- Goal:
- Scope:
- Non-Scope:
- Primary question this map answers:
- Confidence:
  - confirmed:
  - inferred:
  - unknown:

## 2. Context Tree

```text
Node: <feature / capability>
  -> Node: Entry
  -> Node: Main Flow
  -> Node: Branches
  -> Node: Data And Dependencies
  -> Node: Effects
  -> Node: Related Capabilities
  -> Node: Risk And Unknowns
  -> Node: Validation
```

### Node: <feature / capability>

- Type: `capability`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Read First:
  - `<path>` :: `<symbol>`:
- Edges / Children:
  - `Entry`:
  - `Main Flow`:
  - `Branches`:
  - `Data And Dependencies`:
  - `Effects`:
  - `Related Capabilities`:
  - `Risk And Unknowns`:
  - `Validation`:
- Evidence:
- Unknowns:
- Next Drill-Down:

### Node: Entry

- Type: `entry`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Read First:
  - `<path>` :: `<handler / function / class>`:
- Edges / Children:
  - calls `Main Flow` via:
  - guarded by:
  - configured by:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Main Flow

- Type: `flow`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Route:
  1. `<path>` :: `<symbol>` -> role:
  2. `<path>` :: `<symbol>` -> role:
  3. `<path>` :: `<symbol>` -> role:
- Key Objects:
  - `<path>` :: `<function/class/model/config>`:
- Edges / Children:
  - branches to `Branches` when:
  - writes or emits through `Effects`:
  - depends on:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

Keep this as a route, not a source summary.

### Node: Branches

- Type: `branch`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Branches:
  - Condition:
    - Source: `<path>` :: `<symbol>`
    - Effect:
    - Status: `confirmed/inferred/unknown`
- Include:
  - feature flags:
  - permissions:
  - compatibility paths:
  - error paths:
  - tenant/env/version branches:
  - async paths:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Data And Dependencies

- Type: `dependency`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Read First:
  - DB / model:
  - Cache:
  - RPC / HTTP:
  - MQ / event:
  - Config / env:
  - Filesystem / SDK / third-party:
- Edges / Children:
  - provides data to:
  - receives writes from:
  - can fail through:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Effects

- Type: `effect`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Effects:
  - State changes:
  - Writes:
  - Returned values / API response:
  - Messages / jobs emitted:
  - Downstream behavior:
  - User-visible or business-visible effect:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Related Capabilities

- Type: `capability`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Relations:
  - upstream:
  - downstream:
  - shared model:
  - shared config:
  - similar historical path:
- Evidence:
- Unknowns:
- Next Drill-Down:

### Node: Risk And Unknowns

- Type: `risk`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Risks:
  - Risk:
    - Evidence:
    - Why it matters:
    - How to verify:
- Unknowns:
  - Unknown:
    - Needed source/log/test/user confirmation:
- Next Drill-Down:

### Node: Validation

- Type: `validation`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Validation Entry:
  - Unit tests:
  - Integration / e2e tests:
  - Local run command:
  - Logs / metrics:
  - Manual check:
- Edges / Children:
  - proves:
  - does not prove:
- Evidence:
- Unknowns:
- Next Drill-Down:

## 3. Compact Indexes

Use these as lookup tables. Promote a row into a Context Tree Node only when it helps route future context.

### Entry Point Index

| Entry | Path | Handler / Function / Class | Status | Notes |
| --- | --- | --- | --- | --- |
| | | | confirmed/inferred/unknown | |

### Key Object Index

| Object | Path | Kind | Responsibility | Used By |
| --- | --- | --- | --- | --- |
| | | function/class/model/config | | |

### Branch Index

| Branch | Source | Condition | Effect | Status |
| --- | --- | --- | --- | --- |
| | `<path>` | | | confirmed/inferred/unknown |

### Quick File Index

- `<path>`: why to read it
- `<path>`: why to read it

## 4. Next Drill-Down

Load these only if the next task needs them:

- For implementation:
- For risk review:
- For debugging:
- For historical / compatibility confirmation:
