# M05 Audit — Controlled Public Baseline Reproduction Planning and Compute Path

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M05 — Controlled Public Baseline Reproduction Planning and Compute Path |
| **Mode** | DELTA AUDIT |
| **Range** | M04 merge `f54afd0` → M05 PR head `7867e29` |
| **Branch** | `forge/M05-control-repro-planning` |
| **PR** | [#6](https://github.com/m-cahill/forge/pull/6) |
| **current_sha** | `7867e29de8402fc9f92f035c0482ece3688ebf23` |
| **CI Status** | **Green** — [26982564940](https://github.com/m-cahill/forge/actions/runs/26982564940) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — planning contracts delivered; mock plan labeled; no baseline copy; no training authorization |

**Overall score: 4.6 / 5.0**

**Why not 5/5:** Submit UI zip constraints still OPEN; reproduction plan CLI not in CI; corpus schema not extracted (expected for M05); no real control candidate (expected).

**Why not lower:** Complete planning suite, authorization/copying validator with tests, green CI, explicit non-claims, compute path locked, M06 direction documented.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- End-to-end controlled reproduction plan with phase evidence requirements
- Compute-path matrix with locked recommendation (local_5090 preflight; Modal/Tinker future)
- Acquisition policy and future Cursor schema inspection workflow
- Reproduction plan manifest with `training_authorized` / `kaggle_submission_authorized` gates
- Mock preflight evidence + CLI; 9 tests for authorization and copying policy

**Risks**

- **GOV-008:** Mock reproduction plan could be mistaken for training authorization — mitigated by README, `non_claims`, `training_authorized: false`
- **GOV-007:** Submit UI constraints OPEN — documented; not guessed

**Next action:** Merge PR #6 with owner permission; authorize M06 execution gate only.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `baselines/reproduction_plan.py` | New planning contract |
| `docs/milestones/M05/*` | Planning docs + small JSON evidence |
| `scripts/validate_reproduction_plan.py` | New CLI |
| Tests +9 | Reproduction plan validation |

**Risk zones touched:** future reproduction authorization, baseline reference posture. Not touched: training, Kaggle submit, real adapters, baseline repo vendoring.

---

## 4. M05 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from green `main` | Met |
| All §5 deliverables | Met |
| Validator tests pass | Met — 9 tests |
| CLI validates mock plan | Met (local) |
| Mock evidence preflight-only | Met |
| Submit UI OPEN (not guessed) | Met |
| PR CI green | Met — 26982564940 |
| No training/submission/score/reproduction claims | Met |
| No baseline code/data copied | Met |
| No real adapter/package | Met |

---

## 5. Validator Rules Verified (tests)

| Rule | Test coverage |
| ---- | ------------- |
| `training_authorized` true without `owner_training_authorization` | `test_training_authorized_without_owner_record_rejected` |
| `kaggle_submission_authorized` true without owner record | `test_kaggle_authorized_without_owner_record_rejected` |
| `code_copy_allowed` without license evidence | `test_copying_allowed_without_license_rejected` |
| Missing required `non_claims` | `test_missing_non_claims_rejected` |
| `ready_for_training` requires authorization fields | `test_ready_for_training_*` |

---

## 6. Closeout Authorization

M05 may be marked **closed** in governance docs. **Merge** of PR #6 requires separate express owner permission. **M06 implementation** requires separate authorization and `training_authorized` manifest gates.
