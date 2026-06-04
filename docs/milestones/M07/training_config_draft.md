# Training Config Draft — Controlled Public Baseline

**Milestone:** M07  
**Status:** **DRAFT — not executed**  
**Authorization:** `M07_TRAINING_AUTHORIZED = no`

This document captures known fields from M05/M06 planning and read-only baseline references. Unknown fields remain **TBD**. Filling this template does **not** imply training occurred.

---

## Base model

| Field | Value |
| ----- | ----- |
| Base model | `NVIDIA-Nemotron-3-Nano-30B` (competition contract) |
| Adapter rank limit | ≤ 32 (submission) |

---

## Package manager and entry scripts (baseline reference)

| Field | Observed in public repo (M05) | FORGE verified |
| ----- | ----------------------------- | -------------- |
| Package manager | `uv` | **no** |
| Primary training entry | `train_sft.py` | **no** |
| Shared modules | `train_common.py`, `loss_config.py`, `lr_schedule.py` | **no** |
| Upload path | `upload_adapter.py` + Modal | **no** |
| Notebook path | `notebook_tinker.py` | **no** |

**Copying policy:** `no_code_copy` — execute from external clone; do not vendor into FORGE.

---

## Expected training command (placeholder)

**Not executed in M07.** Future authorized run (external tree):

```bash
# FUTURE ONLY — requires owner Gate C + external clone at pinned commit
# cd <external_nemotron_clone>  # e.g. tonghuikang/nemotron @ 82bd1880...
# uv run python train_sft.py  # exact args TBD from baseline README when authorized
```

Exact CLI flags, dataset paths, and hyperparameters: **TBD** until owner-authorized config capture.

---

## Expected output artifacts

Per reproduction plan and M05 template:

| Artifact | Status |
| -------- | ------ |
| `dataset_manifest` | TBD |
| `training_config_hash` | TBD |
| `adapter_sha256` | TBD |
| `package_sha256` | TBD |
| `local_eval_run_id` | TBD |

FORGE will record hashes in run manifests under `artifacts/runs/` when training is authorized and executed.

---

## Missing hyperparameters

| Field | Status |
| ----- | ------ |
| LoRA target modules / alpha / dropout | TBD |
| Batch size | TBD |
| Sequence length | TBD |
| Epochs | TBD |
| Optimizer / LR schedule | TBD (baseline has `lr_schedule.py` — not verified in FORGE) |
| Loss config | TBD |
| Seed | TBD |
| Dataset mix (corpus vs train.csv) | TBD — SQ-CORPUS-001 / SQ-CSV-001 |

---

## Needed owner credentials

| Credential | Status |
| ---------- | ------ |
| Modal | TBD |
| Tinker | TBD |
| Cost acceptance | TBD |
| `owner_training_authorization` | **not provided** |

---

## Needed compute path

| Path | M07 status |
| ---- | ---------- |
| `local_5090` | Preflight only; CUDA/VRAM TBD |
| `modal_tinker` | Recommended for baseline parity when authorized — TBD |
| Selected path | **none** |

---

## Data sources (M06 hashes — reference only)

| File | Rows | SHA256 (prefix) |
| ---- | ---- | --------------- |
| corpus.jsonl | 17,963 | `1940a41c…` |
| problems.jsonl | 9,500 | `4b8bd8b6…` |
| generation.jsonl | 9,500 | `58383d4e…` |
| train.csv | 69,029 | `c99877ac…` |

Full hashes in `docs/forge.md` M06 closeout and training-gate manifest.

---

## Non-claims

- No training config hash is claimed.
- No adapter or package exists from this draft.
- Hyperparameters copied from public docs without a FORGE run are **reference only**.
