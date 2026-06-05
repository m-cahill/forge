# M09 Audit — Modal/Tinker Setup Gate

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M09 — Modal/Tinker Setup Gate |
| **Mode** | DELTA AUDIT |
| **Range** | M08 merge `ac7c5f2` → M09 PR head `434a7de` (+ closeout commit follows) |
| **Branch** | `forge/M09-modal-tinker-setup-gate` |
| **PR** | [#10](https://github.com/m-cahill/forge/pull/10) |
| **current_sha** | `434a7de` (implementation); closeout commit follows |
| **CI Status** | **Green** — [26990264400](https://github.com/m-cahill/forge/actions/runs/26990264400) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — setup gate documented; training blocked; probe not executed |

**Overall score: 4.6 / 5.0**

**Why not 5/5:** Owner evidence still TBD for Modal/Tinker/cost; Submit UI OPEN; SQ-CORPUS-001 open; validate CLI not in CI; training still blocked (expected).

**Why not lower:** All M09 deliverables complete; manifest validates; 166 tests green; explicit non-claims; no secrets, probe output, or baseline copy in repo.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- Dedicated Modal and Tinker readiness evidence documents
- External compute path decision updated from M05/M08 baseline
- Credential storage policy check with repo hygiene attestation
- M09 readiness manifest with Modal/Tinker status fields and blockers
- Validator rules for credential status enums and `credentials_ready` consistency

**Risks**

- **GOV-007:** Submit UI OPEN — unchanged; not guessed
- **GOV-012:** Modal/Tinker/cost TBD — documented; blocks Gate C
- **DATA-001:** SQ-CORPUS-001 open — interim `train.csv` path documented

**Next action:** Merge PR #10 with owner permission; M10 credential/cost closure; optional probe authorization separately.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `docs/milestones/M09/*` | Readiness docs, manifest, run1, summary, audit |
| `src/forge_nemotron/baselines/reproduction_plan.py` | Credential status validation |
| `tests/unit/test_reproduction_plan.py` | +3 tests |
| `docs/forge.md`, `README.md` | Governance |

**Risk zones touched:** external compute readiness, credential/cost gates. Not touched: training execution, Kaggle submit, real adapters, baseline vendoring, probe execution.

---

## 4. M09 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from green `main` | Met |
| M09 plan expanded | Met |
| M09_toolcalls | Met |
| All §7 deliverables | Met |
| Readiness manifest validates | Met |
| Submit UI OPEN (not guessed) | Met |
| Local probe blocked (not run) | Met |
| No training/inference/submission/credentials/adapters | Met |
| PR CI green | Met — 26990264400 |
| M09_next_decision → M10 | Met — credential/cost closure |
| M10 stub seeded | Met (closeout) |

---

## 5. Guardrail Verification

| Guardrail | Verified |
| --------- | -------- |
| No training / inference | Yes |
| No Kaggle submission | Yes |
| No `submission.zip` / adapter files | Yes |
| No baseline code/data in FORGE repo | Yes |
| No committed credentials | Yes |
| No local 5090 probe executed | Yes |
| `M09_TRAINING_AUTHORIZED = no` | Yes |
| Readiness manifest accurate (blocked/TBD state) | Yes |

---

## 6. Dimension Scores

| Dimension | Score | Notes |
| --------- | ----- | ----- |
| Scope control | 5/5 | Setup gate only; no training creep |
| Evidence | 4.5/5 | Docs + manifest + CI green; owner facts TBD |
| Reproducibility | 4.5/5 | Manifest validates; probe not run |
| Competition alignment | 4/5 | Blockers recorded; training still blocked |
| Risk handling | 4.5/5 | OPEN/TBD preserved |
| Documentation | 4.5/5 | forge.md, summary, audit, run1 |

---

## 7. Findings

| ID | Severity | Finding | Status |
| -- | -------- | ------- | ------ |
| GOV-007 | Medium | Submit UI zip constraints OPEN | Deferred — owner |
| GOV-012 | Medium | Modal/Tinker/cost TBD | Deferred — owner M10 |
| GOV-011 | Low | CUDA/VRAM TBD — probe not authorized | Deferred — owner Gate D |
| DATA-001 | Medium | SQ-CORPUS-001 open | Deferred — prefer train.csv first |
| CI-001 | Low | validate CLI not in workflow | Accepted — unit tests cover rules |

No HIGH findings.

---

## 8. Non-claims (audit attestation)

M09 does **not** claim: local 5090 probe executed, Kaggle submission, public/private score, model training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied/vendored baseline code/data, or committed credentials.
