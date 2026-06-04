# Training Config Capture Template

**Milestone:** M05  
**Purpose:** Record baseline training configuration for future reproduction and candidate manifests  
**Status:** **Unused until training is explicitly authorized**

---

## Instructions

1. Fill this template during or after an **authorized** training milestone.
2. Compute `training_config_sha256` from canonical JSON (sorted keys) and store in candidate manifest.
3. Do not claim reproduction from config capture alone.

---

## Configuration record

| Field | Value | Maps to candidate manifest |
| ----- | ----- | ---------------------------- |
| **capture_id** | e.g. `control_repro_train_v001` | notes / run_id |
| **capture_date_utc** | | `created_at_utc` context |
| **base_model** | `NVIDIA-Nemotron-3-Nano-30B` | `base_model` |
| **adapter_rank** | ≤ 32 | `adapter_rank` |
| **lora_config** | target modules, alpha, dropout, etc. | notes |
| **dataset_manifest_hash** | SHA256 of FORGE dataset manifest | `dataset_manifest_sha256` |
| **training_script_command** | exact command line | notes |
| **package_manager** | pip / uv / other | notes |
| **dependency_lock** | lock file hash or path (external) | notes |
| **seed** | | notes |
| **batch_size** | | notes |
| **sequence_length** | | notes |
| **epochs** | | notes |
| **optimizer** | | notes |
| **learning_rate_schedule** | | notes |
| **loss_config** | | notes |
| **hardware** | e.g. `local_5090`, `modal`, `tinker` | environment ledger |
| **runtime_seconds** | | notes |
| **output_adapter_path** | external path | `adapter_path` when real |
| **adapter_sha256** | | `adapter_sha256` |
| **package_sha256** | after packaging | `package_sha256` |
| **local_eval_run_id** | after eval | `local_eval_run_id` |
| **notes** | | `notes` |

---

## Baseline reference (read-only)

| Field | Observed in public repo | FORGE verified |
| ----- | ----------------------- | -------------- |
| Entry script | `train_sft.py` | no |
| Shared modules | `train_common.py`, `loss_config.py`, `lr_schedule.py` | no |
| Upload path | `upload_adapter.py` + Modal | no |
| Package manager | `uv` | no |

---

## Authorization gate

| Gate | Required |
| ---- | -------- |
| Owner training authorization | yes |
| Reproduction plan `training_authorized: true` | yes |
| Compute path selected | yes |
| Holdout contamination check | before using FORGE holdouts |

**M05:** This template is empty by design. No training config hash is claimed.

---

## Non-claims

- Template existence does not imply training occurred.
- Copied hyperparameters from public docs without a FORGE run are **reference only**, not evidence.
