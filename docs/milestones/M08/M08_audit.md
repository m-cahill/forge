# M08 Audit — Compute and Credential Readiness Closure

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M08 — Compute and Credential Readiness Closure |
| **Mode** | DELTA AUDIT |
| **Range** | M07 merge `06ada17` → M08 PR head `5138594` (+ closeout commit pending) |
| **Branch** | `forge/M08-compute-credential-readiness` |
| **PR** | [#9](https://github.com/m-cahill/forge/pull/9) |
| **current_sha** | `5138594` (implementation); closeout commit follows |
| **CI Status** | **Green** — [26988802789](https://github.com/m-cahill/forge/actions/runs/26988802789) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — readiness documented; training blocked; probe not executed |

**Overall score: 4.6 / 5.0**

**Why not 5/5:** Owner evidence still TBD for credentials/cost/CUDA; Submit UI OPEN; SQ-CORPUS-001 open; probe/validate CLI not in CI; training still blocked (expected).

**Why not lower:** Deliverables complete; readiness manifest validates; 163 tests green; explicit non-claims; no secrets, probe output, or baseline copy in repo.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- Structured readiness evidence for compute, credentials, cost, Submit UI, SQ-CORPUS-001
- Readiness manifest with extended validator rules (`cost_accepted`, nullable `compute_path`)
- Safe local probe script + CPU-only parsing tests (probe not run)
- Clear go/no-go matrix and M09 recommendation

**Risks**

- **GOV-007:** Submit UI OPEN — unchanged; not guessed
- **DATA-001:** SQ-CORPUS-001 open — documented; interim `train.csv` path recommended
- **GOV-011:** Probe script exists but not run — CUDA/VRAM remains TBD until Gate B

**Next action:** Merge PR #9 with owner permission; M09 credential/cost gate; optional probe authorization separately.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `docs/milestones/M08/*` | Readiness docs, manifest, run1, summary, audit |
| `src/forge_nemotron/readiness/` | New gpu_probe helpers |
| `src/forge_nemotron/baselines/reproduction_plan.py` | Readiness validation rules |
| `scripts/probe_local_5090.py` | Environment probe CLI |
| `tests/unit/test_gpu_probe.py`, `test_reproduction_plan.py` | +9 tests |
| `docs/forge.md`, `README.md`, `scripts/README.md` | Governance |

**Risk zones touched:** training readiness documentation, compute path selection. Not touched: training execution, Kaggle submit, real adapters, baseline vendoring, probe execution.

---

## 4. M08 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from green `main` | Met |
| M08 plan expanded | Met |
| M08_toolcalls | Met |
| All §4 deliverables | Met |
| Readiness manifest validates | Met |
| Submit UI OPEN (not guessed) | Met |
| No training/inference/submission/credentials/adapters | Met |
| PR CI green | Met — 26988802789 |
| M08_next_decision → M09 | Met — Modal/Tinker setup gate |
| M09 stub seeded | Met (closeout) |

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
| `M08_TRAINING_AUTHORIZED = no` | Yes |
| Readiness manifest accurate (blocked state) | Yes |

---

## 6. Dimension Scores

| Dimension | Score | Notes |
| --------- | ----- | ----- |
| Scope control | 5/5 | Readiness closure only; no training creep |
| Evidence | 4.5/5 | Docs + manifest + CI green; owner facts TBD |
| Reproducibility | 4.5/5 | Probe script documented; not run |
| Competition alignment | 4/5 | Blockers recorded; training still blocked |
| Risk handling | 4.5/5 | OPEN/TBD preserved |
| Documentation | 4.5/5 | forge.md, summary, audit, run1 |

---

## 7. Findings

| ID | Severity | Finding | Status |
| -- | -------- | ------- | ------ |
| GOV-007 | Medium | Submit UI zip constraints OPEN | Deferred — owner |
| GOV-011 | Low | CUDA/VRAM TBD — probe not authorized | Deferred — owner Gate B |
| DATA-001 | Medium | SQ-CORPUS-001 open | Deferred — M09 or owner waiver |
| CI-001 | Low | validate/probe CLI not in workflow | Accepted — unit tests cover rules |

No HIGH findings.

---

## 8. Non-claims (audit attestation)

M08 does **not** claim: local 5090 probe executed, Kaggle submission, public/private score, model training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied/vendored baseline code/data, or committed credentials.
