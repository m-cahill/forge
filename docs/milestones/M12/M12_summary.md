# Milestone Summary — M12: Local CUDA PyTorch Environment Enablement

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — compute readiness  
**Milestone:** M12 — Local CUDA PyTorch Environment Enablement  
**Timeframe:** 2026-06-05  
**Status:** Closed — PR [#13](https://github.com/m-cahill/forge/pull/13) **merged** to `main` (`78605a1`) 2026-06-05T22:43:53Z  
**Branch:** `forge/M12-local-cuda-pytorch-enablement` (deleted after merge)  
**PR head at merge:** `f531202`  
**PR CI:** [27043585782](https://github.com/m-cahill/forge/actions/runs/27043585782) **green**  
**Post-merge CI:** [27043969691](https://github.com/m-cahill/forge/actions/runs/27043969691) **green**

---

## 1. Milestone Objective

Convert the local RTX 5090 from M10’s `visible_no_torch_cuda` state into an evidence-backed isolated CUDA PyTorch environment where `torch.cuda.is_available()` is true — **without** training, inference, model loading, adapters, or Kaggle submission.

---

## 2. Scope Definition

### In Scope

- Isolated `.venv_cuda` setup plan using official PyTorch selector (CUDA 12.8 / `cu128`)
- `scripts/verify_cuda_torch.py` and `cuda_torch_verify.py` helpers
- Sanitized CUDA environment evidence JSON and reports
- `public_control_repro_plan_local_cuda_env_v1` readiness manifest
- `M12_next_decision.md` → M13 Local Training Feasibility Dry Run
- Governance updates (`docs/forge.md`, README, `.gitignore`)

### Out of Scope

- Training, inference, Nemotron/model loading
- Adapter files, `submission.zip`, Kaggle upload
- Main project environment mutation (remains CPU-only by design)
- Baseline reproduction or code/data vendoring
- Merge to `main` (requires express permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Phase A | Branch, expanded plan, toolcalls, forge.md, README, `.gitignore` |
| Phase B | Setup plan, verification script, +9 unit tests, `scripts/README.md` |
| Phase C | `.venv_cuda` created locally; torch 2.11.0+cu128 installed; evidence recorded |
| Phase D | Readiness manifest, environment report, next decision, ledger updates |

**Implementation commits:** `8dc72d0` → `21c60e4` (4 commits, Phases A–D)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **183** tests (+9) |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | local_cuda_env manifest |
| PR CI #13 | **Green** | [27043336258](https://github.com/m-cahill/forge/actions/runs/27043336258) |
| CUDA recheck (local `.venv_cuda`) | Pass | `cuda_ready_probe_only` |
| Training / submission / model load | **Not claimed** | |

**CUDA evidence:** [`cuda_torch_probe.json`](evidence/local_cuda_env/cuda_torch_probe.json)

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M12 delta.
- Test count 174 → 183; CUDA verify helpers covered on CPU-only runners.
- GPU/CUDA smoke runs locally only (not required in CI).

---

## 6. Risks & Open Blockers (post-M12)

| Item | Status |
| ---- | ------ |
| Gate C / training authorization | **not provided** |
| Training feasibility dry run | **not executed** |
| Submit UI zip constraints | **OPEN** |
| Kaggle API submission | **TBD** |
| Modal/Tinker credentials | **TBD** |
| Cost acceptance | **TBD** |
| SQ-CORPUS-001 | **open** |
| Main env PyTorch CUDA | still CPU-only (`visible_no_torch_cuda`) |

---

## 7. Authorized Next Step

**M13 — Local Training Feasibility Dry Run** per [M12_next_decision.md](M12_next_decision.md). Requires separate owner kickoff; **not** full baseline training by default.

---

## 8. Non-claims

`cuda_ready_probe_only` is **not** training readiness. No Kaggle submission, public/private score, model training, inference, model loading, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials.
