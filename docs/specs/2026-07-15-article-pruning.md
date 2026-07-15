# Article Pruning Spec

Date: 2026-07-15

## Goal

Turn the repository's long-form documentation into three distinct, maintainable articles instead of keeping every historical draft in the active tree.

## Boundary

- Keep one thesis article, one practical guide, and one broader Agent / AI Native viewpoint.
- Remove the team guide, the unversioned Claude Code source walkthrough, and all archived historical essays.
- Preserve useful ideas by folding them into the three retained articles.
- Update English and Chinese navigation.
- Do not change skill or protocol behavior.

## Retained Articles

| File | Role |
| --- | --- |
| `docs/code-is-cheap.md` | Why the engineering control plane must move above code |
| `docs/ai-coding-harness-guide.md` | How to package, run, validate, and hand off real coding tasks |
| `docs/general-purpose-agents-are-a-trap.md` | Why concrete capabilities and explicit flows beat vague universality |

## Done Contract

- The repository exposes exactly these three long-form articles.
- No active Markdown link points to removed articles or `docs/archive/`.
- Retained articles use current skill names and describe all four skill entry points accurately.
- `git diff --check` and the local Markdown link check pass.

## Change Log

- Replaced the earlier archive-first consolidation policy with a delete-and-distill policy.
- Historical drafts remain recoverable from Git history rather than the working tree.
- Removed the team guide, the unversioned Claude Code walkthrough, seven historical essays, the archive index, and one now-unused diagram.
- Rewrote the three retained articles so their roles no longer overlap: thesis, practice, and product viewpoint.
- Updated the English README, Chinese README, and docs map.

## Validation

- Exactly three top-level long-form article files remain under `docs/`.
- Every retained article has one H1 and uses current skill names.
- Local Markdown link validation passed across the repository.
- Stale command, model-version, unsupported-metric, and removed-article reference scans passed.
- `git diff --check` passed.

## Resume / Handoff

The pruning objective is complete in the working tree. Changes are not staged or committed.
