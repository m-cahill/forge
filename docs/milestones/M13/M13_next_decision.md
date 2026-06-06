# M13 Next Decision — M14 Recommendation

**Date:** 2026-06-06  
**Branch:** `forge/M13-local-training-feasibility-dry-run`  
**M13 classification:** `cuda_training_feasibility_pass`  
**Evidence:** [local_training_feasibility_report.md](local_training_feasibility_report.md) · [feasibility_run.json](evidence/local_training_feasibility/feasibility_run.json)

---

## M13 outcomes

| Area | M13 result |
| ---- | ---------- |
| Tiny CUDA training-like loop | **passed** — 3 forward/backward/optimizer steps |
| Workload | FORGE-owned toy MLP, synthetic tensors only |
| CUDA memory telemetry | recorded (before/after/peak) |
| Classification | **`cuda_training_feasibility_pass`** |
| Baseline / adapter / Nemotron training | **not performed** |
| Model inference | **not performed** |
| Model loading | **not performed** |
| Adapter files / checkpoints | **not created** |
| Kaggle submission / score | **not performed / not claimed** |
| Readiness manifest | `public_control_repro_plan_local_training_feasibility_v1` validates |

---

## Primary recommendation: M14 — Local Adapter Feasibility Dry Run

**Proposed title:** M14 — Local Adapter Feasibility Dry Run

**Rationale:**

1. M13 proved `.venv_cuda` can run forward/backward/update on CUDA with tiny memory footprint (~18 MiB peak for toy MLP).
2. Owner preference remains `prefer_local_cuda`.
3. Full baseline training is still **not authorized** (Gate C not provided).
4. Next logical step: probe PEFT/LoRA-style memory patterns with a **still-tiny, still-synthetic** workload — not Nemotron 30B, not full SFT.

**M14 scope (draft — not started):**

1. Owner authorizes adapter feasibility dry run only (`M14_FULL_BASELINE_TRAINING_AUTHORIZED = no`).
2. Tiny synthetic PEFT-style probe (e.g., LoRA on toy module) — **no** Nemotron load, **no** real adapter for submission.
3. Record memory/stack evidence; update readiness manifest.
4. Still: no Kaggle submission without separate authorization.

---

## Secondary M14 options

| Option | When to choose |
| ------ | -------------- |
| **M14 — CUDA Troubleshooting** | If M13 had failed or M14 adapter probe fails |
| **M14 — Submit UI Constraint Preflight** | Submit UI evidence becomes deadline-critical (final Jun 15) |
| **M14 — Corpus Segment Mapping Resolution** | SQ-CORPUS-001 blocks training confidence |
| **M14 — Controlled Public Baseline Training Attempt** | Only if Gate C + all readiness gates satisfied — **not recommended now** |

---

## Parallel owner-actions

1. Record Submit UI `submission.zip` constraints when authenticated evidence exists.
2. Supply Modal/Tinker/cost status when available (no secrets).
3. Provide Gate C only when ready for controlled training.

---

## Non-claims preserved

No Kaggle submission, public/private score, real model training, model inference, model loading, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials.

`cuda_training_feasibility_pass` is **not** baseline training readiness or adapter readiness.
