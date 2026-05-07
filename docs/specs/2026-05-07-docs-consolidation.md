# Docs Consolidation Spec

Date: 2026-05-07

## Goal

Reduce duplicate article entrances in this repository and make the current SDD-RIPER / Harness story easier to read.

## Context

The repository had several long-form articles from different thinking stages:

- early SDD / document-driven programming framing
- model-era programmer role migration
- Harness engineering case writing
- current minimum chaos unit / water-flow / `sdd-riper-one-light` framing

Each article has value, but keeping all of them as first-class reading creates a noisy entrance and makes the current claim look less focused.

## Boundary

- Keep existing content; do not delete historical articles.
- Move older or overlapping long-form pieces to `docs/archive/`.
- Keep active docs focused on the current public path:
  - Harness core thinking
  - quickstart
  - team adoption
  - Claude Code runtime case study
- Update README navigation and active docs links.

## Non-Goals

- Do not rewrite every archived article.
- Do not rename active article files in this pass.
- Do not change skill protocol behavior.

## Validation

- No active README or docs entry should point to moved article paths.
- `docs/README.md` should explain active vs archived reading paths.
- `git status` should show moves instead of deleted content.

## Validation Result

- `git diff --check` passed.
- Local Markdown link existence check passed across `README.md`, `README.zh-CN.md`, and `docs/**/*.md`.
- Active docs now only reference archived historical articles through `docs/archive/`.

## Change Log

- Created this consolidation spec.
- Moved overlapping historical articles under `docs/archive/`.
- Added docs navigation.
- Updated root README and Chinese README reading paths.
