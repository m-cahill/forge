# Milestone Summary — M09: Modal/Tinker Setup Gate

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — public control reproduction (external compute setup gate)  
**Milestone:** M09 — Modal/Tinker Setup Gate  
**Timeframe:** 2026-06-05  
**Status:** Closed — PR [#10](https://github.com/m-cahill/forge/pull/10) **merged** to `main` (`5a4300b`) 2026-06-05T02:28:19Z  
**Branch:** `forge/M09-modal-tinker-setup-gate` (deleted after merge)  
**PR head at merge:** `9be2687`  
**PR CI:** [26990319778](https://github.com/m-cahill/forge/actions/runs/26990319778) **green**  
**Post-merge CI:** [26991673323](https://github.com/m-cahill/forge/actions/runs/26991673323) **green**  
**Baseline:** M08 merged `ac7c5f2`

---

## 1. Milestone Objective

Close the external training-path readiness gap by documenting Modal/Tinker (and related) credential and cost status with evidence or explicit **TBD**, so Gate C training authorization can be evaluated with facts — **without** training, inference, Kaggle submission, local GPU probe execution, or baseline reproduction.

---

## 2. Scope Definition

### In Scope

- Modal/Tinker readiness evidence, external compute path decision, credential storage policy check
- Kaggle API / Submit UI status (preserve OPEN/TBD)
- Local 5090 probe blocked document
- SQ-CORPUS-001 status, cost acceptance gate (M09 carry-forward)
- `public_control_repro_plan.modal_tinker_gate.json` + evidence README
- Reproduction plan validator extensions (+3 tests)
- `M09_next_decision.md` → M10 credential/cost closure
- Governance updates (`docs/forge.md`, README, plan, toolcalls, run1, summary, audit)

### Out of Scope

- Model training, inference, Kaggle submission, public/private score
- Baseline reproduction, real adapter package, vendored baseline code/data
- Local 5090 probe execution (`M09_LOCAL_5090_PROBE_AUTHORIZED = no`)
- Gate E training (`M09_TRAINING_AUTHORIZED = no`)
- Merge to `main` (requires express permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Readiness docs | Modal/Tinker, compute path, credential policy, Kaggle status, probe blocked, SQ-CORPUS, cost gate |
| Manifest | `public_control_repro_plan_modal_tinker_gate_v1`; validates |
| Code | `reproduction_plan.py` credential status validation; +3 unit tests |
| Governance | `docs/forge.md`, README, M09 plan/toolcalls/run1/summary/audit |

**Implementation commits:** `e67a290` → `434a7de` (5 commits, Phases A–D + toolcalls)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **166** tests (+3) |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | modal_tinker_gate manifest |
| Local 5090 probe | **not executed** | |
| PR CI #10 | **Green** | [26990264400](https://github.com/m-cahill/forge/actions/runs/26990264400) |
| Training / probe / submission | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M09 delta.
- Test count 163 → 166; M09 manifest and credential status rules covered in unit suite.
- No baseline data, adapters, probe output JSON, or credentials in repo.

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | **OPEN** | Owner-action; not guessed |
| Kaggle API submission | **TBD** | Preserved |
| Modal/Tinker/cloud credentials | **TBD** | `credentials_ready: false` |
| Cost acceptance | **TBD** | `cost_accepted: false` |
| local_5090 CUDA/VRAM | **TBD** | Probe not authorized |
| SQ-CORPUS-001 | **open** | Interim: prefer `train.csv` first |
| Gate C training authorization | **not provided** | |
| validate_reproduction_plan CLI not in CI | Accepted | Verified locally |

No HIGH defects blocking M09 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M10 credential/cost closure | M10 (per `M09_next_decision.md`) |
| Owner Modal/Tinker/cost evidence | Owner — M10 |
| Optional local_5090 probe | Owner authorization phrase |
| Gate C training authorization | Owner — future milestone |
| Submit UI zip constraints | Owner parallel |

---

## 8. Governance Outcomes

- `M09_TRAINING_AUTHORIZED = no`; manifest `training_authorized: false`, `ready_for_training: false`, `compute_path: null`.
- Modal/Tinker account and credential status: **TBD** (no owner evidence in M09).
- Training go/no-go: **NO-GO**; setup gate documentation: **GO**.
- M10 recommended: **Credential and Cost Closure Continuation**.

---

## 9. Readiness Manifest Disclaimer (required)

`public_control_repro_plan.modal_tinker_gate.json` is **Modal/Tinker setup gate evidence only**. It is **not** training authorization, hardware probe evidence, baseline reproduction, adapter/package evidence, or Kaggle-ready submission. The local 5090 probe was **not executed** in M09.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M09 deliverables | Yes |
| PR CI green | Yes — 26990264400 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| No probe output / credentials / adapters in repo | Yes |
| Merge to `main` | Yes — `5a4300b` (2026-06-05T02:28:19Z) |

**Next recommendation:** Owner supplies Modal/Tinker/cost status (no secrets); M10 credential/cost closure per `M09_next_decision.md` when authorized.
