# M01 Audit — Public Control Reproduction Foundation

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M01 — Public Control Reproduction Foundation |
| **Mode** | DELTA AUDIT |
| **Range** | M00 merge `27d0fed` → M01 implementation `a901b3b` |
| **Branch** | `forge/M01-control-baseline` |
| **PR** | [#2](https://github.com/m-cahill/forge/pull/2) |
| **current_sha** | `a901b3bdd793734fd3a07e13566e709d1e7536d3` |
| **CI Status** | **Green** — run [26934972365](https://github.com/m-cahill/forge/actions/runs/26934972365) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — M01 scope delivered; owner-action Kaggle blockers remain outside milestone scope |

**Overall score: 4.5 / 5.0**

**Why not 5/5:** Authenticated Kaggle intake (BQ-001, BQ-003) remains owner-action; validator is structural-only (not vLLM/Kaggle certified); baseline not reproduced (by design). No HIGH issues in M01 deliverables.

**Why not lower:** CI green on PR, 91 tests, clean scope, no false competition claims, DEF-005/DEF-006 closed for M01 intent.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- First green CI workflow with lint, format, mypy, pytest matrix
- Editable package (`forge_nemotron` 0.1.0) without PYTHONPATH
- Boxed-answer metric and structural submission validator with strong unit coverage
- Public baseline intake with license/copying posture documented
- Kaggle debug notebook aligned to debug standard

**Risks**

- Owner must still verify submission limit and rules/team before any Kaggle upload
- Structural validator pass ≠ Kaggle acceptance
- Metric not yet golden-tested against official competition sample outputs

**Next action:** Merge PR #2 with permission; owner completes BQ-001/BQ-003; plan M02 local eval.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `src/forge_nemotron/metric/`, `packaging/` | New competition-facing utilities |
| `tests/unit/` | 91 tests |
| `.github/workflows/ci.yml` | New trust signal |
| `pyproject.toml`, `requirements-dev.txt` | DX |
| `docs/milestones/M01/`, `docs/forge.md` | Governance |
| `notebooks/` | Debug probe only |

**Risk zones touched:** CI glue, metric/contracts, packaging validation. Not touched: training, Kaggle submit, data pipelines.

---

## 4. Architecture & Modularity

### Keep

- Separate `metric/` and `packaging/` packages per FORGE_ANCHOR §8
- Validator returns structured `ValidationReport` (JSON-serializable)
- Tests use programmatic zip fixtures labeled structural-only

### Fix Now

- None required for M01 closeout

### Defer

| Item | To | Rationale |
| ---- | -- | --------- |
| Golden metric tests from Kaggle samples | M02 | Align extractor to official examples |
| `adapter_manifest.py` dataclass | M02 | Run manifest schema |
| Full-model compatibility checks in validator | M02+ | Needs vLLM/load evidence |

---

## 5. CI/CD & Workflow Integrity

| Check | Status |
| ----- | ------ |
| Workflow exists | **Yes** — `.github/workflows/ci.yml` |
| PR run green | **Yes** — 26934972365 |
| Required checks | Ruff, format, mypy, pytest — all pass |
| GPU / training in CI | Correctly absent |

**Guardrail:** Post-merge, confirm first green run on `main` after PR #2 merge.

---

## 6. Tests & Coverage (Delta-Only)

| Metric | Result |
| ------ | ------ |
| pytest | 91 passed (local + CI) |
| test_import | 3 |
| test_metric_boxed | 61 |
| test_package_validator | 27 |
| Coverage % | Not enforced in M01 |

---

## 7. Security & Supply Chain

- Dev deps only: pytest, ruff, mypy (pinned minimums in requirements-dev.txt)
- No `eval` in metric module
- `.gitignore` excludes weights, zips, caches
- CI `permissions: contents: read` only

---

## 8. Top Issues

| ID | Category | Severity | Observation | Recommendation | Status |
| -- | -------- | -------- | ----------- | -------------- | ------ |
| GOV-001 | Governance | MEDIUM | BQ-001 owner-action | Owner records daily limit | Open |
| GOV-002 | Governance | MEDIUM | BQ-003 owner-action | Owner verifies enrollment | Open |
| MET-001 | Metric | LOW | No Kaggle golden tests yet | Add in M02 | Deferred |
| PKG-001 | Packaging | LOW | Structural validator only | Document; expand after upload evidence | Deferred |

No HIGH/CRITICAL issues.

---

## 9. Guardrail Table (M01 Scope)

| Guardrail | Status | Evidence |
| --------- | ------ | -------- |
| No Kaggle submission | Pass | Submission ledger empty |
| No score claimed | Pass | forge.md |
| No baseline reproduction claim | Pass | public_baseline_intake.md |
| No code copy from public repo | Pass | Clean-room metric/validator |
| Validator rejects rank >32 | Pass | test_package_validator |
| No PYTHONPATH required | Pass | pip install -e . |
| CI not falsely claimed green | Pass | Run 26934972365 |
| Notebook non-submission disclaimer | Pass | Notebook cell 0 |

---

## 10. Quality Gates

| Gate | PASS/FAIL | Notes |
| ---- | --------- | ----- |
| CI Stability | **PASS** | PR green |
| Tests | **PASS** | 91 tests |
| Workflows | **PASS** | CI added |
| Security | **PASS** | No eval; minimal deps |
| DX | **PASS** | pyproject.toml |
| Contracts | **PASS** | LoRA zip + boxed metric |
| Scope control | **PASS** | No training/submit creep |

---

## 11. Deferred Issues Registry

| ID | Issue | Deferred To | Blocker? | Exit Criteria |
| -- | ----- | ----------- | -------- | ------------- |
| DEF-001 | Daily submission limit | Owner | Yes for submit budget | BQ-001 closed |
| DEF-002 | Rules/team status | Owner | Yes for eligibility | BQ-003 closed |
| DEF-005 | CI pipeline | **Closed M01** | — | Green PR run |
| DEF-006 | pyproject.toml | **Closed M01** | — | pip install -e . works |
| M01-R1 | Metric golden tests | M02 | No | Kaggle-aligned tests pass |

---

## 12. Score Trend

| Milestone | Arch | Mod | Health | CI | Sec | DX | Docs | Overall |
| --------- | ---- | --- | ------ | -- | --- | -- | ---- | ------- |
| M00 | 4.0 | 4.0 | 4.0 | N/A | 4.0 | 3.5 | 4.5 | 4.0 |
| M01 | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | **4.5** |

---

## 13. Next Milestone Recommendation

**M02 — Exact local evaluation and artifact discipline**

- Local eval CLI, per-category reporting, run manifests
- Golden metric tests where competition samples available
- Holdout register activation
- Do not submit to Kaggle until owner resolves DEF-001/DEF-002

---

## Machine-Readable Appendix

```json
{
  "milestone": "M01",
  "mode": "DELTA_AUDIT",
  "commit": "a901b3bdd793734fd3a07e13566e709d1e7536d3",
  "verdict": "pass",
  "overall": 4.5,
  "ci_run_id": 26934972365,
  "quality_gates": {
    "ci": "pass",
    "tests": "pass",
    "workflows": "pass",
    "security": "pass",
    "contracts": "pass"
  },
  "issues_open": ["GOV-001", "GOV-002", "MET-001", "PKG-001"]
}
```
