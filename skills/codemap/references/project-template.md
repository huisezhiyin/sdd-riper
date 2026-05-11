# Project CodeMap Template

Use for a repository, service, package, subsystem, or first-time project terrain map.

Project CodeMap is breadth-first and shallow enough to navigate. Its main body should be Context Tree Nodes that route the agent toward capability, module, entry, dependency, validation, and Feature CodeMap drill-downs. It should point to Feature CodeMaps instead of embedding every feature chain.

Template:

# <Project / Service> CodeMap (project)

## 1. Orientation

- Project:
- Role / responsibility:
- Main languages / frameworks:
- Runtime / deployment shape:
- Primary entry types:
- Confidence:
  - confirmed:
  - inferred:
  - unknown:

## 2. Context Tree

```text
Node: <project / service>
  -> Node: Capability Index
  -> Node: Module Index
  -> Node: Entry Index
  -> Node: Domain And Data
  -> Node: External Dependencies
  -> Node: Cross-Module Flows
  -> Node: Validation
  -> Node: Risk Areas
  -> Node: Feature CodeMap Backlog
```

### Node: <project / service>

- Type: `project`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Read First:
  - `<path>`:
- Edges / Children:
  - `Capability Index`:
  - `Module Index`:
  - `Entry Index`:
  - `Domain And Data`:
  - `External Dependencies`:
  - `Cross-Module Flows`:
  - `Validation`:
  - `Risk Areas`:
  - `Feature CodeMap Backlog`:
- Evidence:
- Unknowns:
- Next Drill-Down:

### Node: Capability Index

- Type: `capability`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Children:
  - `<capability>`:
    - Main modules:
    - Entry:
    - Feature CodeMap: `mydocs/codemap/...` or pending
    - Status: `confirmed/inferred/unknown`
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Module Index

- Type: `module`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Children:
  - `<module / package>`:
    - Path:
    - Responsibility:
    - Key dependencies:
    - Risk notes:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Entry Index

- Type: `entry`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Entries:
  - APIs / controllers:
  - CLI / commands:
  - Jobs / schedulers:
  - Consumers / event handlers:
  - UI / routes / hooks:
  - Library exports:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

For each entry, prefer source path and symbol over prose.

### Node: Domain And Data

- Type: `object`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Children:
  - Core domain objects:
  - Database tables / models:
  - Cache keys:
  - State machines:
  - Important enums / statuses:
  - Config namespaces:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: External Dependencies

- Type: `dependency`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Children:
  - RPC / HTTP services:
  - MQ / events:
  - Third-party SDKs:
  - Storage / filesystem:
  - Auth / permission providers:
  - Observability dependencies:
- Edges / Children:
  - used by:
  - produces:
  - failure surfaces:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Cross-Module Flows

- Type: `flow`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Major Flows:
  - Flow:
    - Modules:
    - Entry:
    - Effect:
    - Drill-Down:
- Evidence:
- Unknowns:
- Validation:
- Next Drill-Down:

List only the major flows. Create Feature CodeMaps for deep chains.

### Node: Validation

- Type: `validation`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Validation Entry:
  - Test commands:
  - Test directories:
  - Smoke paths:
  - Local run:
  - Logs / metrics:
  - Known CI checks:
- Edges / Children:
  - proves:
  - does not prove:
- Evidence:
- Unknowns:
- Next Drill-Down:

### Node: Risk Areas

- Type: `risk`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Risks:
  - Risk:
    - Source:
    - Affected capabilities:
    - Suggested Feature CodeMap:
- Unknowns:
- Validation:
- Next Drill-Down:

### Node: Feature CodeMap Backlog

- Type: `capability`
- Status: `confirmed/inferred/unknown`
- Purpose:
- Backlog:
  - `<capability>`:
    - Why:
    - Likely entry:
    - Likely files:
    - Priority:
- Evidence:
- Unknowns:
- Next Drill-Down:

## 3. Compact Indexes

Use these as lookup tables. Promote a row into a Context Tree Node only when it helps route future context.

### Capability Index Table

| Capability | Main Modules | Entry | Feature CodeMap | Status |
| --- | --- | --- | --- | --- |
| | | | `mydocs/codemap/...` or pending | confirmed/inferred/unknown |

### Module Index Table

| Module / Package | Path | Responsibility | Key Dependencies | Risk Notes |
| --- | --- | --- | --- | --- |
| | | | | |

### Cross-Module Flow Table

| Flow | Modules | Entry | Effect | Drill-Down |
| --- | --- | --- | --- | --- |
| | | | | |

### Quick File Index

- `<path>`: project orientation
- `<path>`: important entry
- `<path>`: important config
- `<path>`: important tests

## 4. Maintenance Notes

- Refresh this Project CodeMap when module boundaries, entry types, external dependencies, or validation commands change.
- Do not refresh the whole map for a narrow feature edit; update the relevant Feature CodeMap instead.
