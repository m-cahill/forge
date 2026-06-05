# M13_plan.md — Local Training Feasibility Dry Run

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M13 |
| **Title** | Local Training Feasibility Dry Run |
| **Branch** | `forge/M13-local-training-feasibility-dry-run` (planned) |
| **Status** | not started — stub seeded at M12 closeout |
| **Authority** | [`docs/milestones/M12/M12_next_decision.md`](../M12/M12_next_decision.md) |

---

## 1. Objective (stub)

Probe local CUDA memory/stack feasibility on the RTX 5090 using tiny fixtures or a minimal local-only workload — **without** full baseline training, inference on Nemotron, adapters, or Kaggle submission unless separately authorized.

**Context from M12:** `.venv_cuda` has torch 2.11.0+cu128; `cuda_ready_probe_only`; main env remains CPU-only.

**Out of scope until authorized:** full public baseline SFT/QLoRA, Kaggle submission, adapter packaging, reproduced baseline claims.

---

## 2. Expected owner inputs

- `M13_FEASIBILITY_DRY_RUN_AUTHORIZED = yes`
- `M13_TRAINING_AUTHORIZED = no` (unless Gate C explicitly provided)
- Confirmation to use `.venv_cuda` for GPU probes

---

## 3. Hard constraints (draft)

- No full baseline training without Gate C
- No Kaggle submission without separate authorization
- No model weights/adapters committed
- Record evidence honestly if feasibility fails

---

*Full plan to be expanded when M13 is authorized.*
