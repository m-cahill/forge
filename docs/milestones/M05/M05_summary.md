# 📌 Milestone Summary — M05: Controlled Public Baseline Reproduction Planning and Compute Path

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — public control reproduction (planning guardrail)  
**Milestone:** M05 — Controlled Public Baseline Reproduction Planning and Compute Path  
**Timeframe:** 2026-06-04  
**Status:** Closed — PR [#6](https://github.com/m-cahill/forge/pull/6) **merged** to `main` (`34169d0`) 2026-06-04T22:25:51Z  
**Branch:** `forge/M05-control-repro-planning` (deleted after merge)  
**PR head:** `508f9ac080098b1f35adc58bad14c45eee46ded7`  
**PR CI:** [26982740620](https://github.com/m-cahill/forge/actions/runs/26982740620) **green**  
**Post-merge CI:** [26983281413](https://github.com/m-cahill/forge/actions/runs/26983281413) **green**  
**Baseline:** M04 merged `f54afd0`

---

## 1. Milestone Objective

Convert M04 preflight into an executable, auditable plan for a future public control reproduction attempt — compute path, acquisition policy, schema inspection workflow, training config capture, and reproduction-plan manifest — **without** training, inference, submission, or reproduction claims.

Without M05, FORGE would risk jumping to training without documented compute decisions, clean-room acquisition rules, or manifest gates for authorization.

---

## 2. Scope Definition

### In Scope

- Six planning documents (reproduction plan, compute path, acquisition, schema inspection, schema template, training config template)
- `baselines/reproduction_plan.py` + 9 unit tests
- `validate_reproduction_plan.py` + mock preflight JSON evidence
- `M05_next_decision.md` (M06 execution gate recommendation)
- Governance updates (`docs/forge.md`, README, `scripts/README.md`)

### Out of Scope

- Model training, inference, Kaggle submission, public/private score
- Baseline reproduction claim, real adapter package, vendored baseline code/data
- Live corpus schema extraction, Modal/Tinker execution
- M06 implementation, merge to `main` (requires owner permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Docs | Planning docs §5.1–5.6; next decision |
| Code | Reproduction plan builder/validator; CLI |
| Evidence | `public_control_repro_plan.preflight.json` + README |
| Governance | M05 plan, toolcalls, forge.md, README |

**Commits:** `9d5b470`, `7532ac0`, `d3dbd8a`, `4d93f4d`, `7867e29` (+ closeout commit pending)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **147** tests |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | Mock preflight plan |
| PR CI #6 | **Green** | Run 26982659564 (final head) |
| Kaggle / training / reproduction | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M05 delta.
- Test count 138 → 147 without gate weakening.
- Reproduction plan CLI not in CI (unit tests cover validator).

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | **OPEN** | Owner-action; not guessed |
| Kaggle API submission | **TBD** | Preserved in planning docs |
| Mock plan vs real reproduction | Mitigated | Evidence README + `non_claims` |
| `validate_reproduction_plan` not in CI | Accepted | Unit tests cover rules |

No HIGH defects blocking M05 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M06 controlled reproduction execution gate | M06 (per `M05_next_decision.md`) |
| Submit UI zip constraints recording | Owner parallel |
| Corpus schema inspection (authorized) | M06 first sub-step |
| CI job for reproduction plan CLI | M06+ optional |

---

## 8. Governance Outcomes

- Compute path locked: **local_5090** preflight; **Modal/Tinker** (or equivalent) for future baseline-compatible training.
- Clean-room acquisition policy and future Cursor schema workflow documented.
- Mock `public_control_repro_plan_v1` validates; **not** training authorization.
- M06 stub: Controlled Public Baseline Reproduction Execution Gate.

---

## 9. Mock Preflight Disclaimer (required)

`public_control_repro_plan.preflight.json` is **preflight plan evidence only**. It is **not** training authorization, baseline reproduction, adapter/package evidence, or Kaggle-ready submission.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M05 deliverables §5 | Yes |
| PR CI green | Yes — 26982659564 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| Merge to `main` | Yes — `34169d0` (2026-06-04T22:25:51Z) |

**Next recommendation:** Owner records Submit UI zip constraints; authorizes M06 kickoff and training with manifest gates.
