# Recovery From Local Logs

Use this reference when the current chat cannot provide enough context to create a handoff: the session was lost, context compacted badly, the user switched tools, or the user asks to recover a Codex / Claude Code conversation.

## Recovery Goal

Recover enough task state to create a reliable new-chat handoff. Do not reconstruct or expose the full transcript unless the user explicitly asks.

## Safety Rules

- Search local logs only for the requested recovery scope.
- Prefer workspace path, project name, task keywords, touched files, branch name, and time window over broad home-directory searches.
- Do not copy secrets, tokens, `.env`, credentials, private logs, or unrelated personal conversation into the handoff.
- Mark recovered facts by confidence:
  - `confirmed from logs`: directly visible in a recovered event or transcript.
  - `inferred from logs`: reasonable but needs re-checking.
  - `unknown`: not found or ambiguous.
- Recovery is two-stage by default:
  1. Candidate Search: shallow scan, show likely sessions.
  2. Deep Recovery: after user selection, read selected session(s) deeply and create the handoff.
- If several candidate sessions match, ask the user to choose before reading deeply.
- If exactly one candidate is an obvious high-confidence match, proceed and state why it was selected.

## Source Locations

Codex local records commonly appear in:

- `~/.codex/archived_sessions/*.jsonl`
- `~/.codex/sessions/**/*.jsonl`
- `~/.codex/history.jsonl`
- `~/.codex/logs_*.sqlite`

Claude Code local records commonly appear in:

- `~/.claude/projects/<encoded-workspace>/*.jsonl`
- `~/.claude/projects/<encoded-workspace>/sessions-index.json`
- `~/.claude/sessions/*.json`
- `~/.claude/audit-logs/*.jsonl`

Treat these paths as best-effort conventions. Probe with `find` before assuming they exist.

## Two-Stage Recovery Flow

### Stage 1: Natural Language To Search Anchors

Turn the user's natural-language request into search anchors.

Example:

```text
User: 帮我恢复上次那个三色管控 codemap 的对话

Search anchors:
- task keywords: 三色管控, codemap
- likely workspace: current cwd first; then paths containing lippi-enterprise
- time range: recent sessions first, then broaden if no match
- likely artifacts: mydocs/codemap, create_codemap, feature map
```

Use these anchor types:

   - workspace path;
   - project/repo name;
   - task title or distinctive phrases;
   - file paths or symbols;
   - branch name, commit hash, PR/issue id if known;
   - approximate date/time range.

### Stage 2: Candidate Search

Search shallowly and return candidates. Do not read full transcripts yet unless there is exactly one obvious high-confidence match.

Find candidate sessions:

   - Codex JSONL: search for `cwd`, workspace path, repo name, and keywords.
   - Claude Code JSONL: search under the encoded workspace folder first, then by keywords.
   - SQLite logs: inspect tables, then query only candidate rows if text search is needed.

Rank candidates by:

   - exact workspace path match;
   - latest timestamp in the requested range;
   - keyword density;
   - presence of tool calls, file paths, validation commands, or final summaries.

Candidate list format:

```text
找到 <N> 个候选对话：

1. <Codex | Claude Code>
   时间：<timestamp or range>
   workspace: <path>
   source: <session/log path>
   命中：<keywords/files>
   可能内容：<one-line guess>
   置信度：High / Medium / Low

请选择要恢复哪个：1 / 2 / 全部合并 / 重新搜索 <关键词>
```

### Stage 3: User Selection

Wait for the user to choose before deep reading when:

- two or more candidates are plausible;
- candidate sessions are from different workspaces;
- the top candidate has only medium/low confidence;
- deep reading may expose unrelated private context.

Allow these choices:

- a single candidate id;
- multiple ids to merge;
- `全部合并` when sessions are clearly part of the same task;
- a refined search query or time range.

### Stage 4: Deep Recovery

After selection, extract continuity facts:

   - current goal and task scope;
   - latest recap/checkpoint;
   - decisions and constraints;
   - files touched or generated;
   - validation commands and results;
   - blockers, risks, and next action.

### Stage 5: Handoff

Produce a handoff:

   - cite session/source paths;
   - distinguish confirmed/inferred/unknown;
   - include a paste-ready next-chat prompt;
   - update active spec/handoff if the workspace has one.

## Useful Commands

Use `rg` first for JSONL/text logs:

```bash
rg -n "<workspace-or-keyword>" ~/.codex/archived_sessions ~/.codex/sessions ~/.claude/projects
```

Find likely Claude Code sessions for a workspace:

```bash
find ~/.claude/projects -maxdepth 2 -name "*.jsonl" -print | rg "<encoded-or-plain-project-name>"
```

Inspect Codex SQLite tables before querying:

```bash
sqlite3 ~/.codex/logs_2.sqlite ".tables"
sqlite3 ~/.codex/logs_2.sqlite ".schema logs"
```

Keep command output scoped. If a command returns too much, narrow the query by date, workspace, or file path.

## Recovery Output Shape

```text
Recovered sources:
- <session/log path>: <why selected>

recap:
<current goal>; completed <evidence>; key decisions <decision>; next <action>; risk/validation <state>.

Confirmed from logs:
- ...

Inferred from logs:
- ...

Unknown:
- ...

Paste-ready new chat prompt:
...
```
