# SDD Feature Spec Template (Workflow-aligned)

本模板是 `Feature Spec`：当前任务真相源。它只维护本次功能、bug、重构、文档或跨项目任务的目标、边界、进度、计划、验证和恢复点。

`Project Spec` / `Project Memory` 是另一类产物，只记录稳定、可复用、跨任务会影响判断的项目事实。不要把任务执行流水写进 Project Spec，也不要把项目长期记忆混进 Feature Spec；可复用事实先进入本模板的 `Project Sync Candidates`。

本模板包含两个版本：**单项目模板**（默认）和 **多项目模板**（`mode=multi_project` 时使用）。Agent 根据启动模式自动选择对应模板。

---

## 单项目模板（默认）

```markdown
# SDD Spec: <Task Name>

## 0. Open Questions
- [ ] None

## 1. Requirements (Context)
- **Goal**: ...
- **In-Scope**: ...
- **Out-of-Scope**: ...

## 1.1 Context Sources
- Requirement Source: `...`
- Design Refs: `...`
- Chat/Business Refs: `...`
- Extra Context: `...`

## 1.5 Codemap Used (Feature/Project Index)
- Codemap Mode: `feature` / `project`
- Codemap File: `mydocs/codemap/YYYY-MM-DD_hh-mm_<name>.md`
- Key Index:
  - Entry Points / Architecture Layers: ...
  - Core Logic / Cross-Module Flows: ...
  - Dependencies / External Systems: ...

## 1.6 Context Bundle Snapshot (Lite/Standard)
- Bundle Level: `Lite` / `Standard`
- Bundle File: `mydocs/context/YYYY-MM-DD_hh-mm_<task>_context_bundle.md`
- Key Facts: ...
- Open Questions: ...

## 1.7 Minimum Chaos Unit Assessment
- Final Goal: ...
- Current Task Unit: ...
- Why this unit is small enough: ...
- In-Scope Boundary: ...
- Out-of-Scope Boundary: ...
- Verification Evidence: ...
- Failure / Rework Plan: ...
- Model Autonomy Space: ...
- User Decision: Accepted / Revise / Split Further

## 2. Research Findings
- 事实与约束: ...
- 风险与不确定项: ...

## 2.1 Next Actions
- 下一步动作 1 ...
- 下一步动作 2 ...

## 3. Innovate (Optional: Options & Decision)
### Option A
- Pros: ...
- Cons: ...
### Option B
- Pros: ...
- Cons: ...
### Decision
- Selected: ...
- Why: ...
### Skip (for small/simple tasks)
- Skipped: true/false
- Reason: ...

## 4. Plan (Contract)
### 4.1 File Changes
- `path/to/file`: 变更说明

### 4.2 Signatures
- `fn/class signature`: ...

### 4.3 Implementation Checklist
- [ ] 1. ...
- [ ] 2. ...
- [ ] 3. ...

### 4.4 Spec Review Notes (Optional Advisory, Pre-Execute)
- Spec Review Matrix:
| Check | Verdict | Evidence |
|---|---|---|
| Requirement clarity & acceptance | PASS/FAIL/PARTIAL | ... |
| Plan executability | PASS/FAIL/PARTIAL | ... |
| Risk / rollback readiness | PASS/FAIL/PARTIAL | ... |
- Readiness Verdict: GO/NO-GO (Advisory)
- Risks & Suggestions: ...
- Phase Reminders (for later sections): ...
- User Decision (if NO-GO): Proceed / Revise

### 4.5 Route Alignment (Water Flow Check)
- Original assumption: ...
- Current implementation route: ...
- Why it fits code terrain: ...
- Scope impact: None / Changed
- User Decision if route changed: Accepted / Revise

## 5. Execute Log
- [ ] Step 1: ...
- [ ] Step 2: ...

## 6. Review Verdict
- Review Matrix (Mandatory):
| Axis | Key Checks | Verdict | Evidence |
|---|---|---|---|
| Spec Quality & Requirement Completion | Goal/In-Scope/Acceptance 是否完整清晰；需求是否达成 | PASS/FAIL/PARTIAL | `spec section + test/log/人工验收` |
| Spec-Code Fidelity | 文件、签名、checklist、行为是否与 Plan 一致 | PASS/FAIL/PARTIAL | `diff + code refs + execute log` |
| Code Intrinsic Quality | 正确性、鲁棒性、可维护性、测试、关键风险 | PASS/FAIL/PARTIAL | `test/lint/review evidence` |
- Overall Verdict: PASS/FAIL
- Blocking Issues: ...
- Regression risk: Low/Medium/High
- Follow-ups: ...

## 7. Plan-Execution Diff
- Any deviation from plan: ...

## 8. Archive Record (Recommended at closure)
- Archive Mode: `snapshot` / `thematic`
- Audience: `human` / `llm` / `both`
- Source Targets:
  - `mydocs/specs/...`
  - `mydocs/codemap/...`
- Archive Outputs:
  - `mydocs/archive/YYYY-MM-DD_hh-mm_<topic>_human.md`
  - `mydocs/archive/YYYY-MM-DD_hh-mm_<topic>_llm.md`
- Key Distilled Knowledge: ...

## 9. Project Sync Candidates
- Stable project facts discovered:
  - ...
- Suggested destination:
  - `mydocs/project/PROJECT_SPEC.md`
  - `mydocs/project/PROJECT_MEMORY.md`
- Sync decision: Not synced / Synced / Skipped
- Reason:
  - ...
```

---

## 多项目模板（`mode=multi_project` 时使用）

```markdown
# SDD Spec: <Task Name>

## 0. Open Questions
- [ ] None

## 0.1 Project Registry
| project_id | project_path | project_type | marker_file |
|---|---|---|---|
| web-console | ./web-console | typescript | package.json |
| api-service | ./api-service | java | pom.xml |

## 0.2 Multi-Project Config
- **workdir**: `./`
- **active_project**: `web-console`
- **active_workdir**: `./web-console`
- **change_scope**: `local`
- **related_projects**: `api-service`

## 1. Requirements (Context)
- **Goal**: ...
- **In-Scope**: ...
- **Out-of-Scope**: ...

## 1.1 Context Sources
- Requirement Source: `...`
- Design Refs: `...`
- Chat/Business Refs: `...`
- Extra Context: `...`

## 1.5 Codemap Used (Per-Project Index)
### web-console
- Codemap File: `mydocs/codemap/YYYY-MM-DD_hh-mm_web-console项目总图.md`
- Key Index: ...

### api-service
- Codemap File: `mydocs/codemap/YYYY-MM-DD_hh-mm_api-service项目总图.md`
- Key Index: ...

## 1.6 Context Bundle Snapshot (Lite/Standard)
- Bundle Level: `Lite` / `Standard`
- Bundle File: `mydocs/context/YYYY-MM-DD_hh-mm_<task>_context_bundle.md`
- Key Facts: ...
- Open Questions: ...

## 1.7 Minimum Chaos Unit Assessment
- Final Goal: ...
- Current Task Unit: ...
- Why this unit is small enough: ...
- In-Scope Boundary: ...
- Out-of-Scope Boundary: ...
- Verification Evidence: ...
- Failure / Rework Plan: ...
- Model Autonomy Space: ...
- User Decision: Accepted / Revise / Split Further

## 2. Research Findings
- 事实与约束: ...
- 风险与不确定项: ...
- 跨项目依赖关系: ...

## 2.1 Next Actions
- 下一步动作 1 ...
- 下一步动作 2 ...

## 3. Innovate (Optional: Options & Decision)
### Option A
- Pros: ...
- Cons: ...
### Option B
- Pros: ...
- Cons: ...
### Decision
- Selected: ...
- Why: ...
### Skip (for small/simple tasks)
- Skipped: true/false
- Reason: ...

## 4. Plan (Contract)
### 4.1 File Changes (grouped by project)
#### [web-console]
- `src/pages/release.tsx`: 变更说明

#### [api-service]
- `src/main/java/.../ReleaseController.java`: 变更说明

### 4.2 Signatures (grouped by project)
#### [web-console]
- `function triggerRelease(config: ReleaseConfig): Promise<Result>`: ...

#### [api-service]
- `public ResponseEntity<Result> release(ReleaseRequest req)`: ...

### 4.3 Implementation Checklist (grouped by project, dependency order)
#### [api-service] (provider first)
- [ ] 1. ...
- [ ] 2. ...

#### [web-console] (consumer second)
- [ ] 3. ...
- [ ] 4. ...

### 4.4 Contract Interfaces (cross-project only)
| Provider | Interface / API | Consumer(s) | Breaking Change? | Migration Plan |
|---|---|---|---|---|
| api-service | `POST /api/release` | web-console | No | N/A |

### 4.5 Spec Review Notes (Optional Advisory, Pre-Execute)
- Spec Review Matrix:
| Check | Verdict | Evidence |
|---|---|---|
| Requirement clarity & acceptance | PASS/FAIL/PARTIAL | ... |
| Plan executability | PASS/FAIL/PARTIAL | ... |
| Risk / rollback readiness | PASS/FAIL/PARTIAL | ... |
| Cross-project contract completeness | PASS/FAIL/PARTIAL | ... |
- Readiness Verdict: GO/NO-GO (Advisory)
- Risks & Suggestions: ...
- Phase Reminders (for later sections): ...
- User Decision (if NO-GO): Proceed / Revise

### 4.6 Route Alignment (Water Flow Check)
- Original assumption: ...
- Current implementation route: ...
- Why it fits code terrain / project contract: ...
- Scope impact: None / Changed
- User Decision if route changed: Accepted / Revise

## 5. Execute Log (grouped by project)
#### [api-service]
- [ ] Step 1: ...

#### [web-console]
- [ ] Step 2: ...

## 6. Review Verdict
- Review Matrix (Mandatory):
| Axis | Key Checks | Verdict | Evidence |
|---|---|---|---|
| Spec Quality & Requirement Completion | Goal/In-Scope/Acceptance 是否完整清晰；需求是否达成 | PASS/FAIL/PARTIAL | `spec section + test/log/人工验收` |
| Spec-Code Fidelity | 文件、签名、checklist、行为是否与 Plan 一致 | PASS/FAIL/PARTIAL | `diff + code refs + execute log` |
| Code Intrinsic Quality | 正确性、鲁棒性、可维护性、测试、关键风险 | PASS/FAIL/PARTIAL | `test/lint/review evidence` |
- Overall Verdict: PASS/FAIL
- Blocking Issues: ...
- Regression risk (per project):
  - web-console: Low/Medium/High
  - api-service: Low/Medium/High
- Cross-project consistency: PASS/FAIL
- Follow-ups: ...

## 6.1 Touched Projects
| project_id | Files Changed | Reason |
|---|---|---|
| api-service | `ReleaseController.java` | 新增发布接口 |
| web-console | `release.tsx` | 对接发布接口 |

## 7. Plan-Execution Diff
- Any deviation from plan: ...
- Orphan changes (files outside registered projects): None

## 8. Archive Record (Recommended at closure)
- Archive Mode: `snapshot` / `thematic`
- Audience: `human` / `llm` / `both`
- Source Targets:
  - `mydocs/specs/...`
  - `mydocs/codemap/...`
- Archive Outputs:
  - `mydocs/archive/YYYY-MM-DD_hh-mm_<topic>_human.md`
  - `mydocs/archive/YYYY-MM-DD_hh-mm_<topic>_llm.md`
- Key Distilled Knowledge: ...

## 9. Project Sync Candidates
- Stable per-project facts discovered:
  - `project_id`: ...
- Cross-project reusable facts:
  - ...
- Suggested destination:
  - `mydocs/project/PROJECT_SPEC.md`
  - `mydocs/project/PROJECT_MEMORY.md`
- Sync decision: Not synced / Synced / Skipped
```

---

## Project Spec / Project Memory Boundary

Use `mydocs/project/PROJECT_SPEC.md` for stable project truth:

- domain concepts and business invariants;
- module boundaries and ownership;
- architecture conventions;
- core links to project / feature codemaps;
- build, test, release, and validation entry points.

Use `mydocs/project/PROJECT_MEMORY.md` for reusable experience:

- common pitfalls;
- verified debugging paths;
- known flaky areas;
- project-specific agent heuristics;
- decisions that future tasks should remember.

Do not write task execution logs, one-off commands, temporary dirty state, or unverified assumptions into project-level files. Keep those in the active Feature Spec.

## 使用要求

### 通用

- 中大型任务建议先具备 `Codemap + Context Bundle + 首版 Spec`；小任务可先出首版 Spec 再补齐。
- 首版 Spec 允许先完成 Research 最小章节，后续章节按 RIPER 阶段逐步补齐。
- 未经 `Plan Approved` 禁止进入 Execute。
- `review_spec` 为建议性预审：`NO-GO` 不强制阻塞执行；若继续执行需记录用户决策。
- `review_spec` 按阶段检查：未到阶段的缺失内容仅记录为 Reminder。
- Review 未通过则返回 Research/Plan 重新闭环。
- 任务收口时建议填写 `§8 Archive Record` 并执行 `archive` 生成沉淀文档。

### 多项目专属

- `§0.1 Project Registry` 和 `§0.2 Multi-Project Config` 在 bootstrap 时由 Agent 自动生成（通过 Auto-Discovery 或用户提供的 projects 列表）。
- `§4. Plan` 的 File Changes、Signatures、Checklist 必须按项目分组，Provider 优先于 Consumer。
- `§4.4 Contract Interfaces` 仅在 `change_scope=cross` 时必填。
- `§6.1 Touched Projects` 在任何跨项目改动后必填。
- `§6. Review Verdict` 必须包含 per-project regression risk 和 cross-project consistency 检查。
- 建议在 closure 阶段执行 `archive`，沉淀跨项目契约与演进结论。
