---
name: codemap
description: Generate, update, or drift-check agent-facing CodeMaps as progressive code terrain indexes for projects, features, capabilities, functions, modules, or bug chains. Use when Codex needs to inspect an unfamiliar codebase, map a feature/capability from entry to effect, create or update `mydocs/codemap/*`, answer `create_codemap`, `MAP`, `PROJECT MAP`, code terrain, impact-map, "where should the agent look first", check whether existing CodeMaps are stale after a diff, or prepare SDD-RIPER Research without loading the whole repository into context.
---

# Codemap

## Core Position

Create CodeMaps for agents, not CodeWiki for humans.

CodeMap saves context attention, not necessarily raw token count. It does not replace source code, tests, logs, or the current Spec. It routes the agent toward the right source-linked evidence, in the right order, with progressive disclosure.

Use a CodeMap as:

- `Project CodeMap`: breadth-first project terrain, capability index, module boundaries, dependency index, and drill-down pointers.
- `Feature CodeMap`: depth-first capability terrain from entry to effect, including branches, dependencies, risks, and validation entry points.

## Workflow

1. Restate the requested scope and choose mode:
   - `feature`: capability, business feature, bug chain, API flow, function/class-centered investigation.
   - `project`: repository, service, package, subsystem, or first-time onboarding map.
   - `drift-check`: compare current diff or touched files with existing CodeMaps.
   - `update-existing`: refresh an existing CodeMap after code terrain changes.
2. Before writing a durable CodeMap, tell the user why a map/update is useful, the selected mode, scope, and expected path. Do not silently write persistent maps unless current task approval already covers it.
3. Read `references/principles.md` when the output shape, boundary, or CodeWiki-vs-CodeMap distinction matters.
4. For drift checks, read `references/drift-check.md`.
5. For updating an existing map, read `references/update-existing.md`.
6. Inspect code with search first (`rg`, `rg --files`, language-aware tools if available). Prefer source facts over inferred naming matches.
7. Build progressive Context Tree Nodes:
   - start with a small orientation node;
   - add capability, module, entry, branch, effect, dependency, risk, and validation nodes only where they route future context;
   - keep compact indexes as lookup tables, not as the main structure;
   - point nodes to files, functions, classes, tests, configs, logs, and related maps;
   - mark each important relationship as `confirmed`, `inferred`, or `unknown`.
8. Write the map under `mydocs/codemap/` when the user requests a durable artifact or the work feeds SDD-RIPER Research:
   - feature: `mydocs/codemap/YYYY-MM-DD_hh-mm_<feature>功能.md`
   - project: `mydocs/codemap/YYYY-MM-DD_hh-mm_<project>项目总图.md`
9. Keep the CodeMap narrow enough to guide the next agent action. Do not paste large source blocks or turn it into a narrative system document.

## Templates

- For feature/capability maps, follow `references/feature-template.md`.
- For project/system maps, follow `references/project-template.md`.
- For drift checks, follow `references/drift-check.md`.
- For existing map updates, follow `references/update-existing.md`.
- If a task spans multiple repositories, create one Project CodeMap per relevant project, then add a separate interface or cross-service flow summary.

## Output Rules

- Prefer path-linked, source-grounded bullets over prose.
- Separate `Confirmed`, `Inferred`, and `Unknown`.
- Include `Next Drill-Down` so the next agent knows what to read only if needed.
- Include `Validation Entry` so the map can feed Spec / Plan / Review.
- Treat stale or conflicting CodeMaps as indexes to re-check, not truth.
- Do not treat CodeMap as a changelog. Update only terrain-changing facts: entries, flows, module boundaries, dependencies, risks, validation entry points, or behavior rule locations.
