# M13 — Local Training Feasibility Report

**Date:** 2026-06-06  
**Branch:** `forge/M13-local-training-feasibility-dry-run`  
**Classification:** `cuda_training_feasibility_pass`

---

## 1. Authorization

```text
M13_LOCAL_TRAINING_FEASIBILITY_AUTHORIZED = yes
M13_FULL_BASELINE_TRAINING_AUTHORIZED = no
M13_INFERENCE_AUTHORIZED = no
KAGGLE_SUBMISSION_AUTHORIZED = no
```

This run exercised a **tiny toy CUDA training-like feasibility loop** only. It is **not** real model training, baseline training, or adapter training.

---

## 2. Command run

```powershell
.venv_cuda\Scripts\python scripts\run_cuda_training_feasibility.py `
  --out docs\milestones\M13\evidence\local_training_feasibility\feasibility_run.json `
  --steps 3 `
  --device cuda `
  --environment-path .venv_cuda
```

Exit code: **0**

---

## 3. Environment

| Field | Value |
| ----- | ----- |
| Host OS | Windows 10 (AMD64) |
| Python | 3.11.9 |
| Environment | `.venv_cuda` (gitignored) |
| PyTorch | 2.11.0+cu128 |
| CUDA build | 12.8 |
| GPU | NVIDIA GeForce RTX 5090 |
| VRAM total | 32606 MiB |

---

## 4. Toy workload

| Field | Value |
| ----- | ----- |
| Kind | `tiny_mlp_synthetic` |
| Architecture | Linear(64→128) → ReLU → Linear(128→32) |
| Batch size | 32 |
| Optimizer | SGD, lr=1e-3 |
| Loss | MSE |
| Dtype | float32 |
| Steps | 3 |
| Seed | 0 |
| Competition data | no |
| Baseline code | no |
| Model artifacts written | no |

---

## 5. CUDA telemetry

### Memory (bytes)

| Phase | Allocated | Reserved |
| ----- | --------- | -------- |
| Before | 0 | 0 |
| After | 18,087,936 | 23,068,672 |
| Peak allocated | 18,225,664 | — |
| Peak reserved | — | 23,068,672 |

### Per-step timing and loss

| Step | Loss | Elapsed (ms) |
| ---- | ---- | ------------ |
| 1 | 1.0284 | 113.811 |
| 2 | 1.1205 | 0.955 |
| 3 | 1.0531 | 0.587 |

Final loss: **1.0531**

---

## 6. Result

| Field | Value |
| ----- | ----- |
| Success | **true** |
| Steps completed | 3 |
| Errors | none |

Forward, backward, and optimizer updates completed on CUDA without OOM or exception.

---

## 7. Classification

**`cuda_training_feasibility_pass`**

Meaning: the isolated `.venv_cuda` environment can run a tiny forward/backward/update loop on the RTX 5090.

This is **not**:

- baseline training readiness,
- adapter training readiness,
- Nemotron training readiness,
- Kaggle submission readiness.

---

## 8. Limitations

- Workload is a tiny random-init MLP — not representative of 30B QLoRA memory or throughput.
- No gradient checkpointing, mixed precision, or PEFT layers exercised.
- Single GPU, single short run — no stability soak.
- Main project venv remains CPU-only by design.
- Gate C full training authorization still **not provided**.

---

## 9. Recommendation

Proceed to **M14 — Local Adapter Feasibility Dry Run** (toy PEFT-style probe, still not full baseline training) per [`M13_next_decision.md`](M13_next_decision.md).

Evidence: [`feasibility_run.json`](evidence/local_training_feasibility/feasibility_run.json)
