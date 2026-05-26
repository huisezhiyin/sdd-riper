# PROJECT_KNOWLEDGE

This file is the public, sanitized project memory for repository-level facts that future agents should read before synchronizing docs or skills.

## Repository Network

This project has multiple mirrors / downstream copies. Treat the public GitHub repository as the sanitized source for public-facing docs and the internal repository as the internal distribution mirror. The two Aone skill repositories are narrower downstream copies for the two core skills.

| Target | Purpose | Public-safe Path / Remote |
| --- | --- | --- |
| Public repository | Sanitized source for public docs, examples, and bundled skills | `/Users/wuyue/github_project/sdd-riper`, `origin = git@github.com:huisezhiyin/sdd-riper.git` |
| Internal mirror | Internal distribution mirror with internal README, Aone links, and Ant mirror push target | Do not publish internal URLs in public docs. Keep exact remotes in the internal mirror's project knowledge. |
| Aone Light Skill repo | Downstream source for `skills/sdd-riper-one-light/` | Keep only the `sdd-riper-one-light` skill payload synchronized. |
| Aone Standard Skill repo | Downstream source for `skills/sdd-riper-one/` | Keep only the `sdd-riper-one` skill payload synchronized. |

## Sync Rules

- Public docs and public skill sources should be updated in this repository first.
- Internal mirror should then receive the sanitized public changes plus internal-only README / link adjustments.
- Aone skill repositories should receive only their corresponding skill directory content, not the whole SDD-RIPER repo.
- Do not sync `.claude/`, `.agent-memory/`, `.expcap/`, local SQLite/Milvus data, traces, `.env`, credentials, tokens, private logs, or machine-specific paths.
- Do not commit system-level knowledge, feature specs, handoffs, Project Memory, Project Spec, or user preference memory by default. Propose candidates first; commit only after explicit approval and sanitization.
- Do not force-push protected internal branches unless the user confirms the branch protection has been adjusted and history rewrite is intended.

## Update Checklist

When changing README, `AGENTS.md`, skill behavior, memory rules, or public docs:

1. Update this public repository.
2. Run the smallest meaningful validation, at minimum `git diff --check` and local README link checks when README changes.
3. Commit and push `origin/main`.
4. Sync the internal mirror without overwriting internal-only README/AGENTS content unless explicitly intended.
5. If `skills/sdd-riper-one-light/` changed, sync the Aone Light Skill repository.
6. If `skills/sdd-riper-one/` changed, sync the Aone Standard Skill repository.
7. Verify each target with `git status -sb`, the latest commit, and remote branch pointer.

## Internal Details

Exact internal remotes, local internal paths, and mirror-specific push targets belong in the internal mirror's `PROJECT_KNOWLEDGE.md`, not in this public file.
