# Local CUDA Training Feasibility Evidence

## Purpose

This directory holds evidence from the M13 **tiny toy CUDA training-like feasibility loop** on the local RTX 5090 using `.venv_cuda`.

## Non-claims

- **Not** baseline training, public control reproduction, or full SFT.
- **Not** LoRA, QLoRA, PEFT, or adapter training.
- **Not** model inference or text generation.
- **Not** Nemotron or any Hugging Face model loading.
- **Not** an adapter, checkpoint, or Kaggle-ready package.
- **Not** a Kaggle submission or score (public or private).
- **Not** training readiness for Nemotron or adapter feasibility.

## Artifacts

| File | Description |
| ---- | ----------- |
| `feasibility_run.json` | Sanitized JSON telemetry from `scripts/run_cuda_training_feasibility.py` |

## Command

```powershell
.venv_cuda\Scripts\python scripts\run_cuda_training_feasibility.py `
  --out docs\milestones\M13\evidence\local_training_feasibility\feasibility_run.json `
  --steps 3 `
  --device cuda `
  --environment-path .venv_cuda
```

No model weights, adapters, or checkpoints are written by this script.
