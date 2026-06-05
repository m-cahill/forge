# M12 Local CUDA Environment Report

**Date:** 2026-06-05  
**Branch:** `forge/M12-local-cuda-pytorch-enablement`  
**Evidence:** [`evidence/local_cuda_env/cuda_torch_probe.json`](evidence/local_cuda_env/cuda_torch_probe.json)

---

## 1. Authorization

| Field | Value |
| ----- | ----- |
| `M12_LOCAL_CUDA_SETUP_AUTHORIZED` | **yes** |
| `M12_TRAINING_AUTHORIZED` | **no** |
| `M12_INFERENCE_AUTHORIZED` | **no** |
| `KAGGLE_SUBMISSION_AUTHORIZED` | **no** |

---

## 2. Baseline (M10)

| Field | M10 value |
| ----- | --------- |
| Classification | `visible_no_torch_cuda` |
| PyTorch | 2.2.2+cpu |
| `torch.cuda.is_available()` | false |
| GPU visible | yes (RTX 5090, 32607 MiB, driver 591.86) |

---

## 3. M12 isolated environment results

| Field | Value |
| ----- | ----- |
| Environment | `.venv_cuda` (repo root; gitignored) |
| Python | 3.11.9 |
| PyTorch | 2.11.0+cu128 |
| PyTorch CUDA build | 12.8 |
| `torch.cuda.is_available()` | **true** |
| CUDA device count | 1 |
| GPU | NVIDIA GeForce RTX 5090 |
| VRAM total (MiB) | 32607 |
| Driver (nvidia-smi) | 591.86 |
| CUDA version (nvidia-smi header) | 13.1 |
| Tiny CUDA tensor smoke | **passed** |
| Install command source | [PyTorch Get Started](https://pytorch.org/get-started/locally/) — Windows, Pip, CUDA 12.8 |

Install command used:

```powershell
.venv_cuda\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

---

## 4. Classification

**`cuda_ready_probe_only`**

| Meaning | Applies |
| ------- | ------- |
| PyTorch CUDA available | yes |
| Tiny smoke passed | yes |
| Training readiness | **no** |
| Inference readiness | **no** |

This classification is **not** training readiness. A later authorized feasibility dry run is required before any training claim.

---

## 5. What remains before training feasibility

| Blocker | Status |
| ------- | ------ |
| Gate C / `M12_TRAINING_AUTHORIZED` | not provided |
| Training feasibility dry run | not executed |
| Submit UI zip constraints | OPEN |
| SQ-CORPUS-001 | open |
| Modal/Tinker/cost credentials | TBD |
| Main project venv CUDA | still CPU-only (by design; isolated env only) |

---

## 6. M13 recommendation preview

See [`M12_next_decision.md`](M12_next_decision.md). Primary path: **M13 — Local Training Feasibility Dry Run** (still no full baseline training without Gate C).

---

## Non-claims

No Kaggle submission, public/private score, model training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials.
