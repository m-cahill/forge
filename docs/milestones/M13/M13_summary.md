# Milestone Summary — M13: Local Training Feasibility Dry Run

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — compute readiness  
**Milestone:** M13 — Local Training Feasibility Dry Run  
**Timeframe:** 2026-06-06  
**Status:** Closed — PR [#14](https://github.com/m-cahill/forge/pull/14) **merged** to `main` (`16f19e0`) 2026-06-06T02:26:17Z  
**Branch:** `forge/M13-local-training-feasibility-dry-run` (deleted after merge)  
**PR head at merge:** `2eaeecc`  
**PR CI:** [27049407476](https://github.com/m-cahill/forge/actions/runs/27049407476) **green**  
**Post-merge CI:** [27050035266](https://github.com/m-cahill/forge/actions/runs/27050035266) **green**

---

## 1. Milestone Objective

Verify that the isolated `.venv_cuda` environment can run a **tiny toy CUDA training-like feasibility loop** (forward → backward → optimizer update) on the RTX 5090, record CUDA memory/timing telemetry, and classify the result — **without** real model training, baseline training, adapter training, inference, model loading, or Kaggle submission.

M12 established `cuda_ready_probe_only`; M13 answers whether a minimal training-shaped workload succeeds on CUDA.

---

## 2. Scope Definition

### In Scope

- Feasibility design document
- `scripts/run_cuda_training_feasibility.py` + `cuda_training_feasibility.py` helpers
- Local CUDA dry run in `.venv_cuda` (3 steps, toy MLP, synthetic tensors)
- Sanitized JSON evidence, human report, evidence README
- `public_control_repro_plan_local_training_feasibility_v1` readiness manifest
- Validator rules for `local_training_feasibility_status`
- `M13_next_decision.md` → M14 Local Adapter Feasibility Dry Run
- Governance updates (`docs/forge.md`, README, `scripts/README.md`)

### Out of Scope

- Nemotron or Hugging Face model loading
- Public baseline `train_sft.py`, LoRA/QLoRA/PEFT, full SFT
- Adapter files, checkpoints, `submission.zip`
- Model inference / text generation
- Kaggle upload/submission, public/private scores
- Baseline code/data vendoring
- Merge to `main` (requires express permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Phase A | Branch, expanded plan, toolcalls, forge.md, README |
| Phase B | Design doc, feasibility script + helpers, +12 unit tests, scripts README |
| Phase C | `.venv_cuda` dry run; `cuda_training_feasibility_pass`; evidence JSON + report |
| Phase D | Readiness manifest, validator + tests, next decision |
| CI fix | Skip torch-dependent tests when PyTorch absent on CI runners |

**Implementation commits:** `15ca37e` → `9326041` (5 commits, Phases A–D + CI fix)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | 194 collected; torch tests skip on CI |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | local_training_feasibility manifest |
| PR CI #14 | **Green** | [27048718537](https://github.com/m-cahill/forge/actions/runs/27048718537) |
| CUDA dry run (local `.venv_cuda`) | Pass | `cuda_training_feasibility_pass`; peak ~18 MiB |
| Training / submission / model load | **Not claimed** | |

**Feasibility evidence:** [`feasibility_run.json`](evidence/local_training_feasibility/feasibility_run.json)

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M13 delta.
- New tests for classification helpers and manifest validation; torch loop tests skip on CPU-only CI (correct).
- GPU feasibility run local only (not required in CI).

---

## 6. Risks & Open Blockers (post-M13)

| Item | Status |
| ---- | ------ |
| Gate C / full training authorization | **not provided** |
| Adapter feasibility dry run | **not executed** |
| Submit UI zip constraints | **OPEN** |
| Kaggle API submission | **TBD** |
| Modal/Tinker credentials | **TBD** |
| Cost acceptance | **TBD** |
| SQ-CORPUS-001 | **open** |

---

## 7. Authorized Next Step

**M14 — Local Adapter Feasibility Dry Run** per [M13_next_decision.md](M13_next_decision.md). Requires separate owner kickoff; **not** full baseline training by default.

---

## 8. Non-claims

`cuda_training_feasibility_pass` is **not** baseline training readiness, adapter readiness, or Nemotron training readiness. No Kaggle submission, public/private score, real model training, inference, model loading, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials.
