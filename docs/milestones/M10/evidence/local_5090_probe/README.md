# Local 5090 probe evidence (M10)

**Milestone:** M10 — Local 5090 Feasibility Probe  
**Probe date (UTC):** 2026-06-05  
**Authorization:** `M10_LOCAL_5090_PROBE_AUTHORIZED = yes`

## Scope

This directory contains **hardware/environment probe evidence only**.

- **No** model training
- **No** model inference
- **No** model loading
- **No** adapter files
- **No** Kaggle submission
- **No** score

## Artifacts

| File | Description |
| ---- | ----------- |
| `local_5090_probe.json` | Sanitized JSON from `scripts/probe_local_5090.py` |

## Command

```bash
python scripts/probe_local_5090.py --out docs/milestones/M10/evidence/local_5090_probe/local_5090_probe.json
```

## Supersedes

M08/M09 `local_5090` CUDA/VRAM **TBD** fields in `docs/forge.md` are superseded by this probe for the machine where the probe ran.
