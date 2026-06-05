# Milestone Summary — M08: Compute and Credential Readiness Closure

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — public control reproduction (readiness closure)  
**Milestone:** M08 — Compute and Credential Readiness Closure  
**Timeframe:** 2026-06-05  
**Status:** Closed on branch — PR [#9](https://github.com/m-cahill/forge/pull/9) open (merge pending owner permission)  
**Branch:** `forge/M08-compute-credential-readiness`  
**PR head (implementation):** `5138594`  
**PR CI:** [26988802789](https://github.com/m-cahill/forge/actions/runs/26988802789) **green**  
**Baseline:** M07 merged `06ada17`

---

## 1. Milestone Objective

Document compute, credential, cost, and submission readiness blockers with evidence or explicit TBD/open status so Gate C training authorization can be evaluated with facts — **without** training, inference, Kaggle submission, local GPU probe execution, or baseline reproduction.

---

## 2. Scope Definition

### In Scope

- Compute, credential, cost, Submit UI, SQ-CORPUS-001, readiness matrix docs
- `public_control_repro_plan.readiness.json` + evidence README
- Safe `probe_local_5090.py` + `gpu_probe.py` parsing helpers (script **not** run)
- Reproduction plan validator extensions + unit tests (+9 tests)
- `M08_next_decision.md` → M09 Modal/Tinker setup gate
- Governance updates (`docs/forge.md`, README, `scripts/README.md`)

### Out of Scope

- Model training, inference, Kaggle submission, public/private score
- Baseline reproduction, real adapter package, vendored baseline code/data
- Local 5090 probe execution (`M08_LOCAL_5090_PROBE_AUTHORIZED = no`)
- Gate D training (`M08_TRAINING_AUTHORIZED = no`)
- Merge to `main` (requires express permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Readiness docs | Six evidence/gate documents + matrix |
| Probe tooling | `scripts/probe_local_5090.py`, `src/forge_nemotron/readiness/gpu_probe.py` |
| Manifest | `public_control_repro_plan_readiness_v1`; validates |
| Code | `reproduction_plan.py` extensions; +9 unit tests |
| Governance | `docs/forge.md`, README, M08 plan/toolcalls/run1/summary/audit |

**Implementation commits:** `5bd4838` → `5138594` (5 commits, Phases A–E)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **163** tests (+9) |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | readiness manifest |
| `probe_local_5090.py --help` | Pass | probe **not** executed |
| PR CI #9 | **Green** | [26988802789](https://github.com/m-cahill/forge/actions/runs/26988802789) |
| Training / probe / submission | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M08 delta.
- Test count 154 → 163; readiness manifest and gpu_probe parsing covered in unit suite.
- No baseline data, adapters, probe output JSON, or credentials in repo.

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | **OPEN** | Owner-action; not guessed |
| Kaggle API submission | **TBD** | Preserved |
| Modal/Tinker/cloud credentials | **TBD** | `credentials_ready: false` |
| Cost acceptance | **TBD** | `cost_accepted: false` |
| local_5090 CUDA/VRAM | **TBD** | Probe script exists; not run |
| SQ-CORPUS-001 | **open** | Interim: prefer `train.csv` first |
| Gate C training authorization | **not provided** | |
| validate_reproduction_plan / probe CLI not in CI | Accepted | Verified locally |

No HIGH defects blocking M08 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M09 Modal/Tinker setup gate | M09 (per `M08_next_decision.md`) |
| Owner credential/cost evidence | Owner — M09 |
| Optional local_5090 probe | Owner authorization phrase |
| Gate C training authorization | Owner — future milestone |
| Submit UI zip constraints | Owner parallel |

---

## 8. Governance Outcomes

- `M08_TRAINING_AUTHORIZED = no`; readiness manifest `training_authorized: false`, `ready_for_training: false`, `compute_path: null`.
- Training go/no-go: **NO-GO**; readiness documentation: **GO**.
- M09 recommended: **Modal/Tinker Setup Gate**.

---

## 9. Readiness Manifest Disclaimer (required)

`public_control_repro_plan.readiness.json` is **readiness evidence only**. It is **not** training authorization, hardware probe evidence, baseline reproduction, adapter/package evidence, or Kaggle-ready submission. `probe_local_5090.py` was **not executed** in M08.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M08 deliverables | Yes |
| PR CI green | Yes — 26988802789 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| No probe output / credentials / adapters in repo | Yes |
| Merge to `main` | Pending owner permission |

**Next recommendation:** Merge PR #9 when authorized; kick off M09 credential/cost closure; owner records Submit UI constraints and Gate C when ready for training.
