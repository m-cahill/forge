# Controlled Public Baseline Reproduction Plan

**Milestone:** M05  
**Baseline:** https://github.com/tonghuikang/nemotron  
**Status:** **Planning only — not executed, not reproduced**

---

## 1. Purpose and non-claims

This document defines how FORGE may attempt a **controlled** reproduction of the public Progress Prize baseline in a **future authorized milestone**.

**M05 does NOT claim:**

- Baseline reproduction or score parity
- Training, inference, or adapter validity
- Kaggle submission readiness
- Public or private leaderboard score
- License clearance to copy implementation into FORGE

FORGE must produce its own artifacts, manifests, and evidence before any of the above.

---

## 2. Public baseline source summary

| Item | Observation |
| ---- | ------------- |
| Repository | `tonghuikang/nemotron` (read-only reference) |
| Pipeline | `reasoning` → `augmentation` → `corpus` → `train_sft` → Modal upload |
| Package manager | `uv` (`pyproject.toml`, `uv.lock`) |
| External services | Modal (`upload_adapter.py`), Tinker (`notebook_tinker.py`) |
| Large artifacts | `corpus.jsonl` (~42.6 MB), `tokenizer.json`, other JSONL/CSV in repo |
| License | **No LICENSE file observed** at repo root (M01/M04) |
| FORGE posture | Clean-room mapping; **no code copy** into FORGE |

See also: [`public_control_preflight.md`](../M04/public_control_preflight.md), [`baseline_format_mapping.md`](../M04/baseline_format_mapping.md).

---

## 3. Required inputs (future execution)

| Input | Source | FORGE record |
| ----- | ------ | ------------ |
| Repo reference | `https://github.com/tonghuikang/nemotron` | `baseline_repo`, optional `baseline_commit` in reproduction plan manifest |
| Corpus/data | External download outside FORGE tree | Hashes, schema notes — not committed if large |
| Model/base adapter | Nemotron-3-Nano-30B + baseline training path | `training_config_capture_template.md` |
| Training environment | Owner-selected compute path | `compute_path_decision.md` |
| Credentials | Modal, Tinker, cloud GPU as applicable | Listed in manifest `required_credentials`; owner-owned secrets |

---

## 4. Reproduction phases

| Phase | Action | M05 status |
| ----- | ------ | ---------- |
| 1 | Acquire external repo **outside** FORGE working tree (read-only) | Planned — see `baseline_acquisition_policy.md` |
| 2 | Inspect corpus schema (small samples, derived notes only) | Planned — see `corpus_schema_inspection_plan.md` |
| 3 | Map baseline data to FORGE eval format | Planned — partial mapping in M04 |
| 4 | Capture training config (hashes, hyperparams) | Template ready — `training_config_capture_template.md` |
| 5 | Run training | **Deferred** — requires explicit owner authorization + future milestone |
| 6 | Package candidate | **Deferred** — after training evidence + validator pass |
| 7 | Local eval | **Deferred** — FORGE eval CLI exists (M02) |
| 8 | Package validator | **Available** — M01 structural validator |
| 9 | Owner submission go/no-go | **Deferred** — gates in M04 promotion preflight |

---

## 5. Evidence required at each phase

| Phase | Evidence |
| ----- | -------- |
| Acquire | External path (local notes only), optional commit SHA, no FORGE commit of clone |
| Schema inspect | Completed `external_schema_notes_template.md` (derived fields, hashes, row counts) |
| Map to FORGE | Mapping table: baseline fields → `EvaluationExample` / synthetic JSONL |
| Training config | Filled training config template + `training_config_sha256` |
| Training run | Run manifest, adapter SHA256, dataset manifest hash |
| Package | `package_sha256`, validator pass log |
| Local eval | `local_eval_run_id`, per-category CSV, failures JSONL |
| Submit | Owner go-ahead + Kaggle submission ID (future only) |

---

## 6. Blockers

| ID | Blocker | Owner | Status |
| -- | ------- | ----- | ------ |
| BL-M05-001 | Submit UI `submission.zip` constraints/warnings | Owner | **OPEN** — not recorded |
| BL-M05-002 | Kaggle API submission support | — | **TBD** |
| BL-M05-003 | No training authorization in M05 | Owner | **Active** — M05 planning only |
| BL-M05-004 | Baseline LICENSE not observed | Governance | **OPEN** — no code copy |
| BL-M05-005 | Corpus schema not byte-validated | Future milestone | **OPEN** |
| BL-M05-006 | Modal/Tinker credentials and cost | Owner | **OPEN** |
| BL-M05-007 | No real control candidate | — | **OPEN** |

---

## 7. Recommendation for future M06/M07

At M05 closeout, read `M05_next_decision.md` for the locked M06 direction.

**Default expectation (if blockers manageable):** M06 — Controlled Public Baseline Reproduction Execution Gate (owner authorization + compute path + schema notes).

**Alternatives if blockers dominate:**

- M06 — Baseline corpus schema inspection (if schema remains primary blocker)
- M06 — Submission package preflight (if Submit UI constraints block packaging confidence)
- M06 — Holdout activation / local eval hardening (if reproduction remains too risky)

M05 does not start M06 or authorize training.
