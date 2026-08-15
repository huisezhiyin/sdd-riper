# Git Snapshot Protection

Use this gate after the handoff and project-knowledge cleanup are written, but before creating a new conversation. Its purpose is to keep recoverable work in Git even if a Codex worktree is later removed.

## Protection Levels

1. **Clean anchor**: if the repository is clean, record the current branch and commit. Do not create an empty snapshot commit.
2. **Local snapshot**: for a dirty repository, create or reuse a dedicated `codex/new-chat-snapshot-*` branch and commit the reviewed worktree state. This is the default protection level.
3. **Remote snapshot**: optionally push the snapshot branch when the user explicitly requests it or project policy already authorizes it. A failed or unavailable push does not invalidate a verified local commit.

`git add` alone is not durable protection against worktree deletion. Treat staging as a preparation step; the local branch and commit are the recovery anchor.

## Snapshot Workflow

1. Inspect before mutating:

   ```bash
   git rev-parse --show-toplevel
   git status --short --branch
   git branch --show-current
   git diff --stat
   git diff --cached --stat
   ```

2. Review tracked, staged, and untracked paths. Preserve existing user changes and mark ownership as unknown when necessary. Honor `.gitignore`; never stage credentials, `.env`, local databases, runtime memory, traces, caches, or other prohibited artifacts.
3. If the worktree is clean, record `<branch>@<HEAD>` and continue without a new branch.
4. If the worktree is dirty:
   - reuse the current branch when it already matches `codex/new-chat-snapshot-*`;
   - otherwise create and switch to `codex/new-chat-snapshot-YYYYMMDD-HHMM-<task>` from the current `HEAD`;
   - stage the reviewed, non-sensitive worktree state, including relevant untracked files;
   - inspect the staged paths and run `git diff --cached --check`;
   - commit with a clear WIP message such as `chore: snapshot before new chat (<task>)`;
   - remain on the snapshot branch so the next conversation sees the exact protected state.
5. Do not bypass commit hooks automatically. If branch creation, staging, hooks, or commit fails, stop before creating the new conversation and report the blocker.
6. Do not delete the original branch, snapshot branch, stash, or any worktree during handoff.

## Optional Remote Protection

- Push only after explicit user approval or an existing project rule clearly authorizes it.
- Use a normal upstream push for the snapshot branch; never force push.
- Skip remote protection when authentication, connectivity, branch policy, privacy, or repository ownership makes it inconvenient or unsafe.
- Record `not requested`, `skipped`, `failed`, or the pushed remote ref in the handoff.

## Verification

Before creating the new conversation, verify and record:

```bash
git status --short --branch
git rev-parse HEAD
git log -1 --oneline
```

The handoff must include the original branch, snapshot branch, commit SHA, remote protection status, and any intentionally excluded dirty paths. A remaining dirty path is acceptable only when it is explicitly excluded and documented; otherwise the snapshot gate has not passed.

## Thread Target

- Prefer creating the next Codex conversation in the same local project environment on the snapshot branch.
- Do not allocate another worktree merely to obtain a fresh chat. If the runtime only supports a new worktree, use the paste-ready fallback unless the user explicitly asks for another worktree.
- In nested repositories or submodules, protect every dirty repository that contains task state, or explicitly report the unprotected repository before continuing.

