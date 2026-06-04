# Baseline Format Mapping — tonghuikang/nemotron → FORGE

**Milestone:** M04  
**Source:** M01 intake + M04 read-only GitHub re-inspection (2026-06-04)  
**Posture:** Mapping only; no reproduction claim; no code copied

---

## Mapping table

| Public baseline concept | Observed file / command | FORGE equivalent | M04 status |
| ----------------------- | ------------------------ | ---------------- | ---------- |
| Competition metric / `\boxed{}` | Implicit in training/eval | `forge_nemotron.metric.boxed` | **mapped** |
| Local eval scoring | Dashboard / training metrics HTML | `eval/scorer.py`, `scripts/eval_predictions.py` | **mapped** |
| Eval examples JSONL | `problems.jsonl`, eval splits (exact schema TBD) | `tests/fixtures/eval/examples.jsonl`, synthetic smoke JSONL | **partial** |
| Predictions JSONL | Generation outputs | `predictions_*.jsonl` fixture pattern | **mapped** (pattern) |
| Corpus generation | `corpus.py`, `corpus.jsonl` | `scripts/make_dataset.py`, `data/manifests/*` | **partial** — schema not validated |
| Reasoning traces | `reasoning.py`, `reasoning/` | M03 synthetic `examples.jsonl` (solver-verified) | **partial** — different pipeline |
| Augmentation | `augmentation.py`, `augmenters/` | — | **deferred** |
| Problems / investigations | `problems/`, `investigators/` | M03 solvers (narrow categories) | **partial** |
| SFT training | `train_sft.py`, `trainer/` | Future `training/` + run manifest | **planned** |
| Training config | `loss_config.py`, `lr_schedule.py`, `train_common.py` | Future `configs/train/` + `training_config_sha256` in candidate manifest | **planned** |
| Adapter weights | Training output → zip | `packaging/validate_submission.py` | **mapped** (structural) |
| Adapter upload | `uv run modal run upload_adapter.py` | Local validator + future submission ledger | **planned** |
| Run / experiment index | `metrics.html`, training artifacts | `reports/run_manifest.py` | **mapped** |
| Dataset manifest | Implicit in corpus workflow | `data/manifest.py` | **mapped** |
| Candidate metadata | Not formalized in baseline repo | `adapters/candidate_manifest.py` | **mapped** (M04) |
| Tokenizer / vocab | `tokenizer.json`, `vocab.json(l)` | — | **unknown** — not required for M04 preflight |
| Dashboards | `*.html`, `serve.sh` | Future `reports/` | **deferred** |
| CSV export | `generate_csv.py`, `train.csv` | — | **deferred** |
| Tinker path | `notebook_tinker.py` | — | **unknown** — external dependency |
| HuggingFace dataset mirror | Naribow HF dataset | External reference only | **deferred** |

---

## Command mapping

| Baseline command | FORGE M04 equivalent |
| ---------------- | -------------------- |
| `uv run python3 reasoning.py` | No FORGE command — document only |
| `uv run python3 augmentation.py` | No FORGE command — document only |
| `uv run python3 corpus.py` | `python scripts/make_dataset.py` (different data model) |
| `uv run python3 train_sft.py` | **Not implemented** — blocked until authorized milestone |
| `uv run modal run upload_adapter.py` | `python scripts/validate_submission.py` (local structural check only) |

---

## Hash and manifest fields (candidate manifest)

| Baseline artifact (inferred) | FORGE candidate manifest field |
| ---------------------------- | ------------------------------ |
| Trained adapter directory | `adapter_path`, `adapter_sha256` |
| `submission.zip` | `package_path`, `package_sha256` |
| Corpus / dataset | `dataset_manifest_sha256` |
| Training hyperparameters file | `training_config_sha256` |
| Local eval run | `local_eval_run_id`, `local_score`, `local_score_by_category` |

Preflight mock manifest uses `status: preflight` with null hashes — see `evidence/control_preflight/`.

---

## Non-claims

This table does not assert byte-level compatibility, score parity, or successful Kaggle load. Rows marked **unknown** or **partial** require evidence in a future milestone before promotion.
