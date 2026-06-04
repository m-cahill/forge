# 📌 Milestone Summary — M01: Public Control Reproduction Foundation

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Control foundation (Lane A preflight)  
**Milestone:** M01 — Public Control Reproduction Foundation  
**Timeframe:** 2026-06-04  
**Status:** Closed — awaiting merge (PR #2)  
**Branch:** `forge/M01-control-baseline`  
**Implementation commit:** `a901b3bdd793734fd3a07e13566e709d1e7536d3`  
**Baseline:** M00 merged `27d0fed5b62cd3dbef95f8ba32afc6ef4e96d408`

---

## 1. Milestone Objective

Establish the minimum trustworthy local foundation required before any public control adapter work or Kaggle submission: installable package, CI, `\boxed{...}` metric alignment, structural LoRA `submission.zip` validation, documented public baseline intake, and a Kaggle environment debug notebook shell.

Without M01, FORGE would lack automated regression signal, would depend on `PYTHONPATH=src`, and could not safely preflight packages or score completions locally.

---

## 2. Scope Definition

### In Scope

- `pyproject.toml`, `requirements-dev.txt`, editable `forge_nemotron` v0.1.0
- `.github/workflows/ci.yml` (Ruff, MyPy, pytest; Python 3.10–3.12 matrix)
- `src/forge_nemotron/metric/boxed.py` + 61 unit tests
- `src/forge_nemotron/packaging/validate_submission.py` + CLI + 27 unit tests
- `docs/milestones/M01/public_baseline_intake.md` (read-only inspection of `tonghuikang/nemotron`)
- `notebooks/forge_m01_kaggle_debug_probe.ipynb`
- M01 plan, toolcalls, run1, summary, audit; `docs/forge.md` updates

### Out of Scope

- Model training, adapter creation, Kaggle upload, public score
- End-to-end reproduction of `tonghuikang/nemotron`
- Copying public baseline code into FORGE
- Resolving BQ-001 / BQ-003 (owner-action authenticated Kaggle UI)
- Solver factory, local eval CLI (M02+)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Packaging | `pyproject.toml`, `py.typed`, version bump to 0.1.0 |
| CI | GitHub Actions workflow on PR and push to `main` |
| Metric | Boxed extraction, normalization, numeric tolerance, `score_prediction` |
| Packaging | Structural zip validator; rank ≤32 rejection; SHA256 report |
| Docs | Baseline intake, expanded M01 plan, forge.md governance |
| Notebook | Kaggle debug probe (repo-only; no upload) |

**Primary commit:** `a901b3b` — `feat(forge): add M01 metric and package validation foundation` (21 files, +3196 / -208 lines)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `pip install -e .` | Pass | Local + CI (all matrix jobs) |
| `import forge_nemotron` | Pass | v0.1.0, no PYTHONPATH |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | Local + CI |
| `mypy src tests` | Pass | Local + CI |
| `pytest -q` | Pass | 91 tests local; CI pytest step green |
| `compileall src` | Pass | Local |
| GitHub Actions | **Green** | Run [26934972365](https://github.com/m-cahill/forge/actions/runs/26934972365) on PR #2 |
| Validator rank >32 | Pass | Unit tests reject rank 33/64 |
| Baseline reproduction | N/A | Explicitly not claimed |

---

## 5. CI / Automation Impact

- **Added** `.github/workflows/ci.yml` — first FORGE CI workflow.
- **DEF-005** exit criteria met on PR head: green workflow on PR branch.
- **DEF-006** resolved: `pip install -e .` without PYTHONPATH.
- Post-merge CI on `main` not yet verified (awaits PR merge).

---

## 6. Issues & Exceptions

| Issue | Root cause | Status | Reference |
| ----- | ---------- | ------ | --------- |
| BQ-001 daily limit unknown | Authenticated Submit UI | Open — owner-action | `docs/forge.md` §1, §3 |
| BQ-003 rules/team unknown | Authenticated account | Open — owner-action | `docs/forge.md` §1, §3 |
| Public baseline license unclear | No LICENSE in inspected repo | Documented — no copy | `public_baseline_intake.md` |
| Validator structural only | By design for M01 | Documented | Validator docstrings + tests |

No implementation defects blocking M01 closeout.

---

## 7. Deferred Work

| Item | Why deferred | Pre-existed | Status |
| ---- | ------------ | ----------- | ------ |
| BQ-001, BQ-003 | Owner authenticated Kaggle | Yes (M00) | Open |
| Baseline reproduction | Out of M01 scope | Yes | M02+ |
| Kaggle notebook upload | Owner workflow | Yes | Owner reupload when ready |
| Full local eval CLI | M02 scope | N/A | Not started |
| Golden tests from Kaggle metric samples | Samples not ingested | M01-R1 | M02 |

---

## 8. Governance Outcomes

What is now provably true:

- **`forge_nemotron`** is installable at v0.1.0 with 91 unit tests.
- **CI** runs on PRs with lint, format, mypy, pytest across Python 3.10–3.12.
- **Boxed-answer metric** exists as clean-room FORGE code (no `eval`).
- **Package validator** rejects missing config/weights and rank >32 on structural fixtures.
- **`tonghuikang/nemotron`** is documented; **not** reproduced or vendored.
- **Kaggle debug notebook** exists in repo with explicit non-submission disclaimer.
- **No** Kaggle submission, public score, training, or inference claims.

---

## 9. Exit Criteria Evaluation

All acceptance criteria in `M01_plan.md` §7 are **met** except owner-action blockers (explicitly remain open by design). CI green on PR #2 head.

---

## 10. Final Verdict

**M01 objectives met.** Safe to merge PR #2 with express permission. Do not submit to Kaggle until BQ-001/BQ-003 resolved and owner authorizes submission.

---

## 11. Authorized Next Step

- **Authorized:** Merge PR #2 → `main` (express permission only).
- **Authorized:** Seed M02 planning; begin M02 on new branch after merge permission.
- **Not authorized:** Kaggle submission, baseline reproduction claims, M02 implementation without permission.

---

## 12. Canonical References

| Reference | Location |
| --------- | -------- |
| Ultimate Truth | `docs/forge.md` |
| M01 plan | `docs/milestones/M01/M01_plan.md` |
| M01 audit | `docs/milestones/M01/M01_audit.md` |
| M01 CI run | `docs/milestones/M01/M01_run1.md` |
| PR | https://github.com/m-cahill/forge/pull/2 |
| Implementation SHA | `a901b3bdd793734fd3a07e13566e709d1e7536d3` |

---

## Non-Claims (Explicit)

- No Kaggle submission
- No public score
- No reproduced control baseline
- No Kaggle-valid adapter package
- No model training or inference

## Remaining Owner Actions

1. BQ-001: Record daily submission limit from authenticated Submit UI
2. BQ-003: Confirm rules accepted / team joined
3. Reconfirm public deadlines on live Kaggle (BQ-002 partial)
