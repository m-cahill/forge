# M12 Next Decision — M13 Recommendation

**Date:** 2026-06-05  
**Branch:** `forge/M12-local-cuda-pytorch-enablement`  
**M12 classification:** `cuda_ready_probe_only`  
**Evidence:** [local_cuda_environment_report.md](local_cuda_environment_report.md) · [cuda_torch_probe.json](evidence/local_cuda_env/cuda_torch_probe.json)

---

## M12 outcomes

| Area | M12 result |
| ---- | ---------- |
| Isolated `.venv_cuda` created | **yes** (gitignored) |
| CUDA PyTorch install | **success** — torch 2.11.0+cu128 |
| `torch.cuda.is_available()` | **true** |
| RTX 5090 detected | **yes** — 32607 MiB |
| Tiny CUDA tensor smoke | **passed** |
| Classification | **`cuda_ready_probe_only`** |
| Training / inference / submission | **not performed** |
| Readiness manifest | `public_control_repro_plan_local_cuda_env_v1` validates |

---

## Primary recommendation: M13 — Local Training Feasibility Dry Run

**Proposed title:** M13 — Local Training Feasibility Dry Run

**Rationale:**

1. M12 achieved CUDA PyTorch readiness in isolated `.venv_cuda`.
2. Owner preference remains `prefer_local_cuda`.
3. Training is still **not authorized** — feasibility dry run only (memory/stack probe, no full SFT).
4. Modal/Tinker/cost remain TBD; local path is now the most actionable compute option.

**M13 scope (draft — not started):**

1. Owner authorizes feasibility dry run only (`M13_TRAINING_AUTHORIZED = no` unless Gate C provided).
2. Probe QLoRA/memory headroom with tiny fixtures — **no** full baseline training.
3. Update readiness manifest and compute ledger.
4. Still: no Kaggle submission without separate authorization.

---

## Secondary M13 options

| Option | When to choose |
| ------ | -------------- |
| **M13 — Modal/Tinker Setup Execution** | Owner prefers external path or local feasibility fails |
| **M13 — Submit UI Constraint Preflight** | Submit UI evidence becomes deadline-critical (final Jun 15) |
| **M13 — Corpus Segment Mapping Resolution** | SQ-CORPUS-001 blocks training confidence |
| **M13 — Controlled Public Baseline Training Attempt** | Only if Gate C + all readiness gates satisfied — **not recommended now** |

---

## Parallel owner-actions

1. Record Submit UI `submission.zip` constraints when authenticated evidence exists.
2. Supply Modal/Tinker/cost status when available (no secrets).
3. Provide Gate C only when ready for controlled training.

---

## Explicit non-actions

This decision doc does **not** authorize:

- M13 implementation without owner kickoff,
- model training, inference, or Kaggle submission,
- claiming training readiness from `cuda_ready_probe_only`,
- merge to `main` without express permission.
