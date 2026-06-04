# M02 Audit — Exact Local Evaluation and Artifact Discipline

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M02 — Exact Local Evaluation and Artifact Discipline |
| **Mode** | DELTA AUDIT |
| **Range** | M01 merge `d59d97b` / intake `ce9dc7f` → M02 PR head `c8dc65b` |
| **Branch** | `forge/M02-local-eval` |
| **PR** | [#3](https://github.com/m-cahill/forge/pull/3) |
| **current_sha** | `c8dc65be9a930b8b4f11ec0d5dfc56464cf47167` |
| **CI Status** | **Green** — [26973038855](https://github.com/m-cahill/forge/actions/runs/26973038855) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — M02 scope delivered; fixture score clearly not competition evidence |

**Overall score: 4.6 / 5.0**

**Why not 5/5:** Fixture eval CLI not run in CI; production holdouts still TBD; Submit UI zip constraints open; no golden tests against official Kaggle metric samples (deferred from M01). No HIGH issues.

**Why not lower:** Deterministic scorer, hashing, manifests, 106 tests, green CI, explicit fixture/local score labeling, holdout discipline documented.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- Local evaluation layer on top of M01 `score_prediction()`
- Artifact hashing and run manifest contract for audit trails
- Fixture holdout registered; production holdouts unchanged (planned)
- Committed tiny evidence with README non-claims
- Extra-prediction warn-by-default + strict flag

**Risks**

- **GOV-003:** Fixture score **0.75** could be misread as leaderboard signal — mitigated by evidence README, summary §9, audit §8
- CLI smoke not in CI — mitigated by unit tests + committed evidence regeneration instructions
- Real candidates not yet scored (no adapters)

**Next action:** Merge PR #3 with permission; plan M03; owner records Submit UI zip constraints.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `src/forge_nemotron/eval/` | New scoring surface |
| `src/forge_nemotron/artifacts/`, `reports/` | Hashing + manifests |
| `scripts/eval_predictions.py` | New CLI |
| `tests/fixtures/eval/`, `tests/unit/test_eval_*` | Fixtures + 15 tests |
| `data/manifests/m02_fixture_holdouts.json` | Holdout registry |
| `docs/milestones/M02/evidence/` | Small committed artifacts |
| `docs/forge.md`, README | Governance |

**Risk zones touched:** eval contracts, artifact provenance. Not touched: training, Kaggle submit, packaging of real adapters.

---

## 4. Architecture & Modularity

### Keep

- Scorer delegates matching to `metric.boxed` (no duplicate metric logic)
- Records separate from scorer and CLI
- Canonical JSON for hashes and committed evidence

### Fix Now

- None required for M02 closeout

### Defer

| Item | To | Rationale |
| ---- | -- | --------- |
| JSON Schema for eval JSONL/manifest | M03+ | Stretch deferred |
| CI job running fixture CLI smoke | M03+ | Optional hardening |
| Golden tests from Kaggle metric samples | M03+ | Samples not ingested |

---

## 5. CI/CD & Workflow Integrity

| Check | Status |
| ----- | ------ |
| PR run green | **Yes** — 26973038855 |
| Required checks | Ruff, format, mypy, pytest — all pass |
| Test delta | +15 tests (106 total) |
| Gate weakening | None observed |

**Guardrail:** Confirm post-merge green on `main` after PR #3 squash merge.

---

## 6. Tests & Coverage (Delta-Only)

| Metric | Result |
| ------ | ------ |
| pytest | 106 passed |
| test_eval_scorer | 10 |
| test_artifact_hashing | 3 |
| test_run_manifest | 2 |
| Coverage % | Not enforced |

---

## 7. Fixture Score vs Competition Score

| Attribute | Fixture smoke 0.75 | Kaggle/public score |
| --------- | ------------------- | --------------------- |
| Data | `tests/fixtures/eval/*.jsonl` | Competition set |
| Purpose | CLI/manifest smoke | Leaderboard |
| Model | None (hand completions) | Nemotron + adapter |
| Claimed in M02 | **No** | **No** |

Audit requires all future docs/PRs to preserve this distinction.

---

## 8. Top Issues

| ID | Category | Severity | Observation | Recommendation | Status |
| -- | -------- | -------- | ----------- | -------------- | ------ |
| GOV-003 | Governance | LOW | Fixture 0.75 confusion risk | Keep labels in evidence + forge | Mitigated |
| GOV-004 | Governance | MEDIUM | Submit UI zip constraints TBD | Owner records from Submit UI | Open |
| CI-001 | CI | LOW | Eval CLI not in workflow | Optional smoke step in M03 | Deferred |

No HIGH issues.

---

## 9. M02 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from `main` | Met |
| Plan + toolcalls | Met |
| Eval records + scorer | Met |
| CLI outputs (JSON/CSV/failures/manifest/hashes) | Met |
| Hashing + manifest tests | Met |
| Fixture data + holdout manifest | Met |
| Fixture smoke | Met — 0.75 local only |
| PR CI green | Met — 26973038855 |
| Non-claims | Met |

---

## 10. Closeout Authorization

M02 may be marked **closed** in governance docs. **Merge** of PR #3 requires separate express owner permission.
