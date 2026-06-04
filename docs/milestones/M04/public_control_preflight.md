# Public Control Reproduction Preflight Dossier

**Milestone:** M04  
**Inspection dates:** M01 intake 2026-06-04; M04 re-inspection 2026-06-04 (read-only)  
**Repository:** https://github.com/tonghuikang/nemotron  
**Branch observed:** `master`  
**Status:** **Preflight mapping only — not reproduced in FORGE**

---

## 1. Purpose and non-claims

This dossier prepares FORGE for a future **controlled** attempt to reproduce or externally wrap the public Progress Prize baseline. It records observed structure, workflow, dependencies, and FORGE mappings.

**M04 does NOT claim:**

- Reproduction of the public baseline
- Validation of training or upload code
- Kaggle submission readiness
- Public or private leaderboard score
- Adapter validity
- License clearance for copying code into FORGE

FORGE must produce its own artifacts and evidence before any of the above.

---

## 2. Baseline sources

| Resource | URL | M04 status |
| -------- | --- | ---------- |
| GitHub repo | https://github.com/tonghuikang/nemotron | inspected (read-only) |
| Kaggle writeup | https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge/discussion/689915 | linked; not re-validated in M04 |
| Kaggle notebook | https://www.kaggle.com/code/huikang/end-to-end-finetuning-for-lb-0-85 | linked; title claims LB 0.85 — **not verified by FORGE** |
| Public dashboard | https://nemotron.huikang.dev/ | referenced in baseline README |
| HuggingFace mirror | https://huggingface.co/datasets/Naribow/nvidia-nemotron-progress-prize | noted in M01 intake; not downloaded in M04 |

---

## 3. Observed baseline workflow

Documented pipeline order (from baseline README):

```text
reasoning generation  →  augmentation  →  corpus generation  →  SFT training  →  adapter upload (Modal)
```

| Stage | Observed entry point | Notes |
| ----- | -------------------- | ----- |
| Reasoning generation | `reasoning.py` (~8.7 KB) | Writes to `reasoning/` directory |
| Augmentation | `augmentation.py` (~1.4 KB) | Uses `augmenters/`, `augmentations/` |
| Corpus generation | `corpus.py` (~9.7 KB) | Produces `corpus.jsonl` (~42.6 MB in repo) |
| SFT training | `train_sft.py` (~20.2 KB) | Uses `train_common.py`, `loss_config.py`, `lr_schedule.py`, `trainer/` |
| Adapter upload | `upload_adapter.py` (~6.6 KB) | `uv run modal run upload_adapter.py` |

**Supporting / alternate paths (observed, not fully traced):**

| File | Size (approx.) | Role |
| ---- | -------------- | ---- |
| `notebook_tinker.py` | 55.5 KB | Tinker integration (external service) |
| `generate_csv.py` | 4.4 KB | CSV generation |
| `delete-tinker-checkpoint.sh` | 1.4 KB | Tinker checkpoint cleanup |
| `serve.sh` | local dashboard | Static site on port 33304 |

**Dashboards (static HTML):** `base.html`, `synthetic.html`, `corpus.html`, `training.html`, `metrics.html`, `index.html` — debugging/visualization; deferred for FORGE.

---

## 4. Observed repository structure (M04 re-inspection)

Fresh read-only listing via GitHub API (`master`, 2026-06-04). Aligns with M01 intake; additions noted.

**Core scripts:** `reasoning.py`, `augmentation.py`, `corpus.py`, `train_sft.py`, `upload_adapter.py`, `train_common.py`, `loss_config.py`, `lr_schedule.py`, `generate_csv.py`, `notebook_tinker.py`

**Large data artifacts (in repo, not vendored by FORGE):**

| File | Observed size |
| ---- | ------------- |
| `corpus.jsonl` | ~42.6 MB |
| `tokenizer.json` | ~17.1 MB |
| `generation.jsonl` | ~4.8 MB |
| `vocab.jsonl` | ~5.7 MB |
| `vocab.json` | ~2.6 MB |
| `train.csv` | ~3.1 MB |
| `problems.jsonl` | ~931 KB |

**Package manager:** `uv` (`pyproject.toml`, `uv.lock` ~591 KB) — FORGE uses pip/editable install.

**M04 additions vs M01 intake:** `delete-tinker-checkpoint.sh`, `index.html`, `CNAME`, IDE config dirs (`.claude`, `.codex`, `.vscode`) — no FORGE impact assumed.

---

## 5. Dependency and compute blockers

| Blocker | Category | M04 assessment |
| ------- | -------- | -------------- |
| `uv` package manager | Dependency | FORGE would need wrapper or pip-equivalent env |
| Modal | External service | Required for baseline `upload_adapter.py` path |
| Tinker | External service | `notebook_tinker.py`, checkpoint script suggest account/API |
| 30B model + GPU | Compute | Full SFT not feasible in FORGE CI; local 5090 TBD for authorized training milestone |
| Large committed corpus | Data | Download/verify outside repo; no commit to FORGE |
| Kaggle notebook env | Environment | M01 probe: CPU-only, no base model paths attached |
| FORGE Submit UI zip rules | Governance | **OPEN** — owner-action; see §8 |

---

## 6. License and copying posture

| Item | Status |
| ---- | ------ |
| LICENSE file in repo root | **NOT OBSERVED** (M01 and M04 re-inspection) |
| Code copied into FORGE | **None** — clean-room FORGE modules only |
| Implementation posture | External-reference mapping; wrapper scripts may cite repo URL |
| Data committed to FORGE | **None** from baseline repo in M04 |

If license is clarified later (e.g. MIT/Apache), reassess copying policy in a dedicated governance update.

---

## 7. FORGE mapping

| Baseline concept | FORGE equivalent | M04 status |
| ---------------- | ---------------- | ---------- |
| `\boxed{}` answer format | `forge_nemotron.metric.boxed` | **mapped** (M01) |
| Local accuracy | `forge_nemotron.eval.scorer` + `scripts/eval_predictions.py` | **mapped** (M02) |
| Run provenance | `forge_nemotron.reports.run_manifest` | **mapped** (M02) |
| Dataset provenance | `forge_nemotron.data.manifest` + `scripts/make_dataset.py` | **mapped** (M03) |
| Synthetic traces | M03 solver factory + smoke JSONL | **partial** — different generators than baseline |
| `submission.zip` structure | `forge_nemotron.packaging.validate_submission` | **mapped** (M01) |
| Adapter candidate metadata | `forge_nemotron.adapters.candidate_manifest` | **mapped** (M04) |
| Baseline corpus JSONL | — | **unknown** — format not validated byte-for-byte |
| Baseline SFT / upload | — | **planned** — future authorized milestone |
| Dashboards | — | **deferred** |

---

## 8. Open questions and pre-submission blockers

| ID | Item | Owner | Status |
| -- | ---- | ----- | ------ |
| OQ-M04-001 | Exact `corpus.jsonl` / training example schema vs FORGE JSONL | Cursor | **open** |
| OQ-M04-002 | Modal + Tinker credentials and cost path for reproduction | Owner | **open** |
| OQ-M04-003 | Compute path: local 5090 vs Kaggle GPU vs external | Owner | **open** |
| OQ-M04-004 | Whether baseline rank/hyperparams are fully documented without training run | Cursor | **open** |
| **BQ-SUBMIT-ZIP** | Submit UI `submission.zip` constraints/warnings | Owner | **OPEN** — not recorded |
| **BQ-KAGGLE-API** | Kaggle API programmatic submission | — | **TBD** |

M04 does **not** guess Submit UI constraints. See `docs/kaggle/kaggle_setup_evidence.md`.

---

## 9. Recommended next step (preflight)

After M04 closeout, read `M04_next_decision.md` for the locked M05 recommendation. Preflight expectation: either (a) controlled reproduction attempt with explicit compute authorization, or (b) strengthen local eval / packaging gates if blockers remain.

**M04 does not start M05 or training.**

---

## 10. References

| Reference | Location |
| --------- | -------- |
| M01 intake | [`docs/milestones/M01/public_baseline_intake.md`](../M01/public_baseline_intake.md) |
| FORGE truth | [`docs/forge.md`](../../forge.md) |
| Kaggle evidence | [`docs/kaggle/kaggle_setup_evidence.md`](../../kaggle/kaggle_setup_evidence.md) |
| Mock preflight manifest | [`evidence/control_preflight/`](evidence/control_preflight/) |
