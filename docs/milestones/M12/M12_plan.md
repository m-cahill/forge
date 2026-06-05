# M12_plan.md — Local CUDA PyTorch Environment Enablement

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M12 |
| **Title** | Local CUDA PyTorch Environment Enablement |
| **Branch** | `forge/M12-local-cuda-pytorch` (planned) |
| **Status** | not started — stub seeded at M11 closeout |
| **Authority** | [`docs/milestones/M11/M11_next_decision.md`](../M11/M11_next_decision.md) |

---

## 1. Objective (stub)

Enable CUDA-visible PyTorch in the active local environment so the probed RTX 5090 can be evaluated as a training compute path — **without** training unless separately authorized.

**Context from M11:** GPU visible (`visible_no_torch_cuda`); owner preference `prefer_local_cuda`; Modal/Tinker/cost remain TBD.

**Out of scope until authorized:** model training, inference, Kaggle submission, full baseline reproduction.

---

## 2. Expected owner inputs

- `M12_LOCAL_CUDA_SETUP_AUTHORIZED = yes` (Gate D)
- Confirmation of target Python environment (venv/conda/system)
- Optional: CUDA toolkit / driver compatibility notes (no secrets)

---

## 3. Hard constraints (draft)

- No training without `M12_TRAINING_AUTHORIZED = yes`
- No Kaggle submission without separate authorization
- Record probe re-run evidence after CUDA PyTorch install

---

*Full plan to be expanded when M12 is authorized.*
