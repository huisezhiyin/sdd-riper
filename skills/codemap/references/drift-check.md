# CodeMap Drift Check

Use this when current changes may have made an existing CodeMap stale.

## Goal

Decide whether existing `mydocs/codemap/*` maps still route agents correctly after a diff or touched-file set.

Drift check does not automatically rewrite maps. It reports whether an update is needed and why.

## Inputs

- Current diff or touched files.
- Existing CodeMap files under `mydocs/codemap/`.
- Current task / spec / handoff when available.

## Terrain-Changing Diff

Suggest or require an update only when the diff changes:

- entry points;
- main call/effect chains;
- module boundaries or ownership;
- critical branches or business rule locations;
- external dependencies or integration contracts;
- risk points;
- validation entry points;
- filenames/symbols that existing CodeMaps use as `Read First` anchors.

Do not update CodeMaps for:

- typo fixes;
- copy/text changes;
- log wording;
- small style tweaks;
- isolated test data changes;
- implementation details that do not change how a future agent navigates terrain.

## Verdicts

- `No Update Needed`: existing CodeMaps still route correctly.
- `Update Suggested`: map is still usable, but a small refresh would prevent confusion.
- `Update Required`: map points to stale/renamed/incorrect terrain, or omits a new route/risk that future agents need.

## Workflow

1. Identify touched files and changed symbols.
2. Search existing CodeMaps for those paths, symbols, modules, and feature names.
3. Compare map claims with source facts.
4. Produce a short verdict. Do not rewrite unless current task approval includes durable map updates.

## Output Shape

```text
Codemap Drift Check:
- Verdict: No Update Needed / Update Suggested / Update Required
- Reason:
- Touched terrain:
- Affected CodeMaps:
- Suggested patch:
- Need approval before writing: Yes / No
```
