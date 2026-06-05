# M10 Local 5090 Probe Report

**Date:** 2026-06-05  
**Branch:** `forge/M10-local-5090-feasibility-probe`  
**Evidence:** [`evidence/local_5090_probe/local_5090_probe.json`](evidence/local_5090_probe/local_5090_probe.json)

---

## 1. Probe authorization

| Field | Value |
| ----- | ----- |
| `M10_LOCAL_5090_PROBE_AUTHORIZED` | **yes** |
| `M10_TRAINING_AUTHORIZED` | **no** |
| `M10_INFERENCE_AUTHORIZED` | **no** |
| `KAGGLE_SUBMISSION_AUTHORIZED` | **no** |

Probe only — no model load, training, inference, adapters, or Kaggle activity.

---

## 2. Probe command run

```bash
python scripts/probe_local_5090.py --out docs/milestones/M10/evidence/local_5090_probe/local_5090_probe.json
```

**Python:** 3.11.9 (project verification environment)  
**Machine label:** `local_5090`

---

## 3. Hardware summary

| Field | Value |
| ----- | ----- |
| Host OS | Windows 10.0.26200 (AMD64) |
| `nvidia-smi` | **available** |
| GPU name | **NVIDIA GeForce RTX 5090** |
| VRAM total (MiB) | **32607** (~32 GB) |
| Driver version | **591.86** |

The RTX 5090 is **visible** to the system via `nvidia-smi` on the machine where Cursor ran the probe.

---

## 4. CUDA / PyTorch summary

| Field | Value |
| ----- | ----- |
| PyTorch installed | **yes** |
| PyTorch version | `2.2.2+cpu` |
| `torch.cuda.is_available()` | **false** |
| CUDA device count | not reported (CUDA unavailable) |

**Interpretation:** GPU driver stack is present, but the active PyTorch build is **CPU-only**. PyTorch does not see CUDA on this environment.

---

## 5. Disk / system summary

The probe script does not collect disk/RAM metrics in the current implementation. Platform metadata is recorded in the JSON (`platform.system`, `platform.python`, etc.).

---

## 6. Readiness classification

**Classification:** `visible_no_torch_cuda`

| Classification | Meaning |
| -------------- | ------- |
| `visible_no_torch_cuda` | GPU visible via driver tools but PyTorch CUDA unavailable |

This is **not** `cuda_ready_probe_only` (requires `torch.cuda.is_available()` true) and **not** training readiness.

---

## 7. Limitations

- Probe did not load models, datasets, or external baseline artifacts.
- No CUDA toolkit version was queried beyond driver visibility.
- No VRAM free/used breakdown (query uses total memory only).
- CPU-only PyTorch may be an environment choice, not a hardware limitation.
- Visible GPU + driver does **not** prove baseline training feasibility.

---

## 8. Recommendation

**Hardware:** RTX 5090 with ~32 GB VRAM and current driver appears **viable** for future local work once a CUDA-enabled PyTorch (or equivalent stack) is installed and verified.

**Immediate blocker for local CUDA path:** PyTorch CPU build — `torch.cuda.is_available()` is false.

**M11 (probe-result-driven):** Primary recommendation is **M11 — Credential and Cost Closure Continuation** (or Modal/Tinker setup continuation) per decision logic when CUDA/PyTorch are not jointly usable. **Secondary:** if owner prefers local compute, **M11 — Local CUDA Stack Fix + Training Feasibility Dry Run** (still no full baseline training without Gate C).

See [`M10_next_decision.md`](M10_next_decision.md) for the formal M11 recommendation.

---

## Non-claims

No Kaggle submission, public/private score, model training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials.
