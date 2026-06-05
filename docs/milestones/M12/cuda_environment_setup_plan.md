# M12 CUDA Environment Setup Plan

**Milestone:** M12 — Local CUDA PyTorch Environment Enablement  
**Date:** 2026-06-05  
**Branch:** `forge/M12-local-cuda-pytorch-enablement`

---

## 1. Purpose and non-claims

This plan documents how to create an **isolated** local CUDA PyTorch environment for the RTX 5090 host.

**Purpose:** enable `torch.cuda.is_available()` in `.venv_cuda` and record evidence.

**Non-claims:**

* not training readiness
* not inference readiness
* not model loading
* not adapter creation
* not Kaggle submission
* not reproduced baseline

---

## 2. Current M10 baseline facts

| Field | Value |
| ----- | ----- |
| GPU | NVIDIA GeForce RTX 5090 |
| VRAM | 32607 MiB |
| Driver | 591.86 |
| Host OS | Windows 10.0.26200 |
| Python (probe env) | 3.11.9 |
| PyTorch (main env) | 2.2.2+cpu |
| `torch.cuda.is_available()` | **false** |
| Classification | `visible_no_torch_cuda` |

Evidence: [`docs/milestones/M10/evidence/local_5090_probe/local_5090_probe.json`](../M10/evidence/local_5090_probe/local_5090_probe.json)

---

## 3. Target isolated environment

| Setting | Value |
| ------- | ----- |
| Path | `.venv_cuda/` (repo root) |
| Git status | **gitignored** — never committed |
| Main project venv | **not mutated** |

---

## 4. Python interpreter choice

Use **Python 3.11.x**, matching the M10 probe family (3.11.9 target).

Create the environment with the project’s normal Python 3.11 interpreter:

```powershell
python -m venv .venv_cuda
```

Record the exact `python --version` from `.venv_cuda\Scripts\python.exe` in evidence.

---

## 5. Official PyTorch install selector command

**Source:** [PyTorch Get Started — Locally](https://pytorch.org/get-started/locally/)  
**Selector inputs:** Windows · Pip · Python · **CUDA 12.8** (Blackwell / RTX 5090)

**Recorded command (selector output, 2026-06-05):**

```powershell
.venv_cuda\Scripts\python -m pip install --upgrade pip
.venv_cuda\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

**Rationale:** NVIDIA Blackwell RTX GPUs require CUDA 12.8+ for native support; PyTorch publishes `cu128` wheels for Windows. Use the wheel’s **bundled CUDA runtime** — do not install a standalone system CUDA toolkit in M12.

**If install fails:** record failure in `cuda_torch_probe.json`, classify as `blocked_install_failed`, and do not claim CUDA readiness.

---

## 6. Verification commands

After install:

```powershell
.venv_cuda\Scripts\python scripts\verify_cuda_torch.py --help
.venv_cuda\Scripts\python scripts\verify_cuda_torch.py `
  --environment-path .venv_cuda `
  --out docs\milestones\M12\evidence\local_cuda_env\cuda_torch_probe.json `
  --tiny-smoke
```

Optional driver visibility (no model load):

```powershell
nvidia-smi
```

---

## 7. Backout / cleanup instructions

Remove the isolated environment only — **do not** uninstall packages from the main project venv:

```powershell
Remove-Item -Recurse -Force .venv_cuda
```

Committed evidence under `docs/milestones/M12/evidence/` may remain as historical record.

---

## 8. Risks and limitations

| Risk | Handling |
| ---- | -------- |
| Wrong CUDA wheel | Use live selector; record exact command |
| Blackwell compatibility | CUDA 12.8 (`cu128`) per NVIDIA/PyTorch guidance |
| Main env corruption | Isolated `.venv_cuda` only |
| Tensor smoke ≠ training | No models; tiny tensor only |
| `cuda_ready_probe_only` overclaim | Explicit non-claims; not training readiness |
| Environment committed | `.gitignore` + pre-commit hygiene |
