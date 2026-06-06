# M14_plan.md — Local Adapter Feasibility Dry Run

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M14 |
| **Title** | Local Adapter Feasibility Dry Run |
| **Branch** | `forge/M14-local-adapter-feasibility-dry-run` (planned) |
| **Status** | not started — stub seeded at M13 closeout |
| **Authority** | [`docs/milestones/M13/M13_next_decision.md`](../M13/M13_next_decision.md) |

---

## 1. Objective (stub)

Probe local CUDA PEFT/LoRA-style memory patterns using a **still-tiny, still-synthetic** workload in `.venv_cuda` — **without** loading Nemotron, full baseline training, real submission adapters, or Kaggle upload unless separately authorized.

**Context from M13:** `cuda_training_feasibility_pass` on RTX 5090; toy MLP forward/backward/update succeeded; peak ~18 MiB.

**Out of scope until authorized:** Nemotron 30B load, full public baseline SFT/QLoRA, Kaggle submission, real adapter packaging, reproduced baseline claims.

---

## 2. Expected owner inputs

- `M14_ADAPTER_FEASIBILITY_DRY_RUN_AUTHORIZED = yes`
- `M14_FULL_BASELINE_TRAINING_AUTHORIZED = no` (unless Gate C explicitly provided)
- Confirmation to use `.venv_cuda` for GPU probes

---

## 3. Hard constraints (draft)

- No Nemotron or Hugging Face 30B model loading without separate authorization
- No full baseline training without Gate C
- No Kaggle submission without separate authorization
- No real adapter weights committed
- Record evidence honestly if feasibility fails

---

*Full plan to be expanded when M14 is authorized.*
