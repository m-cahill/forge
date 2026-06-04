# M00 Audit — Anchor, Competition Intake, and Kaggle Submission Bible

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M00 — Anchor, competition intake, and Kaggle submission bible |
| **Mode** | BASELINE ESTABLISHMENT (first governance milestone on greenfield repo) |
| **Range** | `9512c89...f61e5cb` (+ closeout commit pending) |
| **Branch** | `forge/M00-anchor-intake` |
| **current_sha** | `f61e5cb` (pre-closeout); see closeout commit after `docs(milestones): close out M00` |
| **CI Status** | **Not configured** — no GitHub Actions workflows; not claimed green |
| **Audit Verdict** | 🟡 **Pass with documented owner-action deferrals** — M00 scope delivered; authenticated Kaggle intake incomplete by design |

**Overall score: 4.0 / 5.0**

**Why not 5/5:** Two M00 exit criteria (`daily submission limit`, `rules/team status`) require authenticated Kaggle UI access the agent cannot perform. They are correctly recorded as owner-action blockers (not guessed). Per FORGE audit posture, unresolved intake blockers that affect submission budgeting prevent a perfect intake score even when implementation scope is complete.

**Why not lower:** No scope creep, no false competition claims, canonical anchor preserved, FORGE-specific bible, scaffold and local import verification documented.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- Ultimate Truth (`docs/forge.md`) with authority rules, ledgers, holdouts, promotion gates, M00 exit checklist
- FORGE Kaggle bible (`submission.zip`, LoRA ≤32, repo-first notebooks, debug standard, prohibited claims)
- Full repo scaffold and `.cursorrules` competition hard gates
- Public deadlines recorded; owner-action discipline for authenticated fields

**Risks**

- Daily submission limit and rules/team status still unknown until owner verifies
- No CI workflow — future PRs lack automated regression signal
- `forge_nemotron` import requires `PYTHONPATH=src` until packaging in M01

**Next action:** Owner completes authenticated Kaggle checklist; then PR/merge M00 and authorize M01 on `forge/M01-control-baseline`.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `docs/` governance + Kaggle | Primary delta |
| `src/forge_nemotron/__init__.py` | Placeholder only |
| Scaffold dirs | `.gitkeep` only |
| `.cursorrules`, `.gitignore`, `README.md` | Policy and ignore rules |

**Risk zones touched:** Documentation/contracts, CI glue (none yet). Not touched: auth, persistence, training, solvers, submissions.

---

## 4. Architecture & Modularity

### Keep

- Package boundary layout per `docs/FORGE_ANCHOR.md` §8 (`metric/`, `solvers/`, `packaging/`, etc.)
- Separation of doctrine (`FORGE_ANCHOR`) vs state (`forge.md`) vs Kaggle ops (bible)

### Fix Now (≤ 90 min)

- None required for M00 closeout

### Defer

| Item | To | Rationale |
| ---- | -- | --------- |
| `pyproject.toml` / editable install | M01 | Import works via `PYTHONPATH` |
| CI (Ruff, pytest, smoke) | M01 or CI milestone | No workflows exist |
| Package validator | M01 | Documented in plan |

---

## 5. CI/CD & Workflow Integrity

| Check | Status |
| ----- | ------ |
| GitHub Actions | **Absent** — `Glob .github/**` → 0 files |
| Required checks | N/A |
| Claimed green CI | **No** — correctly not claimed in `docs/forge.md` |

**Guardrail:** Do not mark CI green in `docs/forge.md` until a workflow runs and passes on PR.

---

## 6. Tests & Coverage (Delta-Only)

| Metric | Result |
| ------ | ------ |
| pytest | Exit 5 — no tests collected |
| Coverage | N/A |
| New logic | `__init__.py` only |

**Fast fix (M01):** Add minimal `tests/unit/test_import.py` when `pyproject.toml` lands.

---

## 7. Security & Supply Chain

- No new dependencies or lockfiles
- `.gitignore` excludes secrets, large weights, `submissions/*`, `artifacts/runs/*`
- No workflow trust boundary changes (no workflows)

---

## 8. Top Issues

| ID | Category | Severity | Observation | Interpretation | Recommendation | Guardrail |
| -- | -------- | -------- | ----------- | -------------- | -------------- | --------- |
| GOV-001 | Governance | MEDIUM | BQ-001 daily limit = OWNER ACTION (`docs/forge.md` L38) | Submission slot planning blocked | Owner records limit from Submit UI | Do not guess; update Competition Snapshot |
| GOV-002 | Governance | MEDIUM | BQ-003 rules/team = OWNER ACTION (`docs/forge.md` L39) | Eligibility risk if not joined | Owner verifies competition enrollment | Block M01 Kaggle submit until verified |
| CI-001 | CI | LOW | No `.github/workflows` | No automated PR signal | Add minimal lint+pytest workflow in M01 | Record CI run ID in milestone ledger |
| DX-001 | DX | LOW | Import needs `PYTHONPATH=src` | Easy footgun for agents | Add `pyproject.toml` in M01 | Document in README until fixed |

No HIGH/CRITICAL issues.

---

## 9. PR-Sized Action Plan

| ID | Task | Category | Acceptance Criteria | Risk | Est |
| -- | ---- | -------- | ------------------- | ---- | --- |
| GOV-001 | Owner: daily limit | Governance | Field in `docs/forge.md` ≠ OWNER ACTION; BQ-001 closed | Med | Owner |
| GOV-002 | Owner: rules/team | Governance | Field verified; BQ-003 closed | Med | Owner |
| CI-001 | Add CI workflow | CI | `gh run list` shows green on PR branch | Low | 90m |
| DX-001 | `pyproject.toml` | DX | `pip install -e .` + `import forge_nemotron` without PYTHONPATH | Low | 60m |

---

## 10. Guardrail Table (M00 Scope)

| Guardrail | Status | Evidence |
| --------- | ------ | -------- |
| No Kaggle submission made | Pass | Submission Ledger empty |
| No score claimed | Pass | No public score in `docs/forge.md` |
| No training performed | Pass | No train scripts implemented |
| No solver implementation | Pass | `solvers/.gitkeep` only |
| No duplicate anchor | Pass | Single `docs/FORGE_ANCHOR.md` |
| Anchor remained canonical at `docs/` | Pass | No root copy |
| Bible uses `submission.zip`, not CSV | Pass | `docs/kaggle_submission_bible.md` L10, §3 |
| Notebook workflow repo-first | Pass | Bible §4, README |
| Debug-output standard exists | Pass | `docs/kaggle/notebook_debug_standard.md` |
| Owner-action blockers without guessing | Pass | Competition Snapshot + evidence |

---

## 11. Quality Gates

| Gate | PASS/FAIL | Notes |
| ---- | --------- | ----- |
| CI Stability | **N/A** | No CI |
| Tests | **PASS** (vacuous) | No tests; no failures |
| Coverage | **N/A** | |
| Workflows | **FAIL** (expected deferral) | None configured |
| Security | **PASS** | No new deps |
| DX | **PARTIAL** | Import via PYTHONPATH |
| Contracts | **PASS** | LoRA zip documented |

---

## 12. Deferred Issues Registry

| ID | Issue | Discovered | Deferred To | Reason | Blocker? | Exit Criteria |
| -- | ----- | ---------- | ----------- | ------ | -------- | ------------- |
| DEF-001 | Daily submission limit | M00 | Owner / pre-M01 submit | Auth UI | Yes for slot plan | Value in Competition Snapshot + BQ-001 closed |
| DEF-002 | Rules/team status | M00 | Owner / pre-M01 submit | Auth UI | Yes for eligibility | BQ-003 closed with evidence row |
| DEF-003 | Zip size/extra files | M00 | M01 / owner | Submit UI | No | Documented in evidence if present |
| DEF-004 | Kaggle API submission | M00 | M01 | Unverified | No | Documented yes/no in evidence |
| DEF-005 | CI pipeline | M00 | M01+ | Out of M00 scope | No for M00 merge | Green workflow on PR |
| DEF-006 | pyproject.toml | M00 | M01 | Out of M00 scope | No | `pip install -e .` works |

---

## 13. Score Trend

| Milestone | Arch | Mod | Health | CI | Sec | Perf | DX | Docs | Overall |
| --------- | ---- | --- | ------ | -- | --- | ---- | -- | ---- | ------- |
| M00 | 4.0 | 4.0 | 4.0 | N/A | 4.0 | N/A | 3.5 | 4.5 | **4.0** |

Weighting: Docs/Governance 35%, Architecture 25%, Health/Scope 20%, DX 10%, CI 10% (N/A → excluded from penalty).

---

## 14. Flake & Regression Log

| Item | Type | First Seen | Status | Notes |
| ---- | ---- | ---------- | ------ | ----- |
| — | — | — | — | No flakes (no CI/tests) |

---

## 15. Next Milestone Recommendation

**M01 — Public control reproduction** on `forge/M01-control-baseline`:

1. Inspect [tonghuikang/nemotron](https://github.com/tonghuikang/nemotron) (recommended; not reproduced).
2. Implement boxed-answer metric extraction and package validator.
3. Add `pyproject.toml` and minimal CI.
4. Do not submit to Kaggle until package validator passes and owner resolves DEF-001/DEF-002.

---

## Machine-Readable Appendix

```json
{
  "milestone": "M00",
  "mode": "BASELINE_ESTABLISHMENT",
  "commit": "f61e5cb",
  "range": "9512c89...f61e5cb",
  "verdict": "yellow",
  "quality_gates": {
    "ci": "not_configured",
    "tests": "pass_vacuous",
    "coverage": "n/a",
    "security": "pass",
    "workflows": "fail_deferred",
    "contracts": "pass"
  },
  "issues": [
    {"id": "GOV-001", "severity": "medium", "category": "governance"},
    {"id": "GOV-002", "severity": "medium", "category": "governance"},
    {"id": "CI-001", "severity": "low", "category": "ci"},
    {"id": "DX-001", "severity": "low", "category": "dx"}
  ],
  "deferred_registry_updates": ["DEF-001", "DEF-002", "DEF-003", "DEF-004", "DEF-005", "DEF-006"],
  "score_trend_update": {"milestone": "M00", "overall": 4.0}
}
```
