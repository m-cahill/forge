# Kaggle Submission Bible — FORGE

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Authority:** Subordinate to Kaggle rules/UI and [`docs/forge.md`](forge.md); operational companion for submission, notebook, evidence, and debugging.  
**Last updated:** 2026-06-05  
**Status:** M10 rules archive cross-reference

Related: [`docs/competition_rules.md`](competition_rules.md), [`docs/kaggle/kaggle_setup_runbook.md`](kaggle/kaggle_setup_runbook.md), [`docs/kaggle/kaggle_setup_evidence.md`](kaggle/kaggle_setup_evidence.md), [`docs/kaggle/notebook_debug_standard.md`](kaggle/notebook_debug_standard.md)

> **Not PANTANAL:** Other projects may use `submission.csv`. FORGE requires **`submission.zip`** with a LoRA adapter. Do not copy CSV/BirdCLEF rules here.

---

## 1. Authority and source hierarchy

1. Kaggle competition rules, overview, evaluation, data, and Submit UI ([`docs/competition_rules.md`](competition_rules.md) archived copy).
2. [`docs/forge.md`](forge.md) — Ultimate Truth.
3. This bible.
4. Milestone evidence under `docs/milestones/`.
5. Notebook logs and local scratch output (non-authoritative until promoted).

---

## 2. Competition snapshot

| Field | Value (M00) | Notes |
| ----- | ------------- | ----- |
| Competition URL | <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge> | |
| Base model | `NVIDIA-Nemotron-3-Nano-30B` | No standalone model submit |
| Package | `submission.zip` | LoRA adapter + `adapter_config.json` |
| LoRA rank | ≤ 32 | Hard gate |
| Metric | Answer accuracy | Exact string or relative numerical tolerance |
| Output format | Final answer in `\boxed{...}` | |
| Inference | Deterministic (vLLM) | No sampling diversity at eval |
| Entry deadline | **June 8, 2026** | Public; owner reconfirm on Kaggle |
| Final deadline | **June 15, 2026, 11:59 PM UTC** | Public; owner reconfirm on Kaggle |
| Daily submission limit | **5 per day** | Rules §2.2.a; Submit UI verified 2026-06-04 |
| Final submissions | **Up to 2** for judging | Rules §2.2.b |
| Team size | **Max 5** | Rules §2.1 |
| Rules / team status | **Yes** (owner 2026-06-04) | Authenticated account |
| Prize eligibility | Public Kaggle notebook + solution write-up | Rules §8.c; track in `docs/forge.md` |
| Winner obligations | Training + inference code, methodology, compute env | Rules §8.a |
| Data license | CC BY 4.0 (NVIDIA Research attribution) | Rules §4.a |
| External data/tools | Allowed if reasonably accessible / minimal cost | Rules §6 |
| Submit UI zip constraints | **OPEN** | Owner-action; not recorded |

---

## 3. Submission artifact contract

### Required filename

`submission.zip` (unless Submit UI specifies otherwise — record any change in evidence).

### Expected contents

```text
submission.zip
  adapter_config.json
  adapter_model.safetensors   # or equivalent PEFT adapter weights
  (other files required by PEFT / competition, if any)
```

### Hard requirements

- Compatible with **NVIDIA-Nemotron-3-Nano-30B**
- LoRA rank **≤ 32**
- Valid PEFT LoRA layout
- No accidental large unrelated files

### Forbidden / caution

- Standalone full model weights as submission
- Rank > 32 in final candidate
- Unrecorded adapter or package hashes in `docs/forge.md`

### Hashing and manifests

Before any Kaggle upload:

1. Run local package validator (M01+).
2. Record adapter hash, zip hash, and manifest under `submissions/<candidate>/` and `docs/forge.md` Submission Ledger.

---

## 4. Submission workflow

```text
Cursor edits code/notebook in repo
  → git commit
  → operator reuploads/resyncs notebook or zip to Kaggle
  → evidence row in docs/kaggle/kaggle_setup_evidence.md
  → update docs/forge.md if material
```

### Notebook edit policy (binding)

> Do **not** edit Kaggle notebooks on the website as the default workflow. Cursor updates notebooks in the repository; the operator reuploads or resyncs to Kaggle. Kaggle-site edits are **emergency-only** and must be **backported** into the repo before they are project truth.

### Pre-upload gate

- Package validator **pass**
- Rank ≤ 32 confirmed
- Hashes recorded
- No holdout contamination in training data for this candidate

---

## 5. Notebook modes

| Mode | Purpose | Evidence implication |
| ---- | ------- | -------------------- |
| **Interactive** | Debug paths, env, smoke | Does **not** prove scored submission |
| **Commit** | Saved notebook version | Does **not** alone prove leaderboard score |
| **Submit / scored** | Competition scoring | Requires full evidence row + submission ID if any |

Every evidence record must state the mode.

---

## 6. Required Kaggle paths and mounted resources

| Path | Role |
| ---- | ---- |
| `/kaggle/input/` | Mounted competition data, models, datasets |
| `/kaggle/working/` | Writable outputs (e.g. `submission.zip`) |
| `/kaggle/` | Root; list for discovery |

Record observed paths per run (competition layout may vary). FORGE repo mirrors evidence in `docs/kaggle/kaggle_setup_evidence.md`.

---

## 7. Kaggle environment settings

Record for each attempt:

- Accelerator (CPU/GPU/TPU)
- Internet on/off
- `nvidia-smi` when GPU expected
- CUDA / torch versions if used
- Working disk free space
- Runtime limits from competition (confirm on rules page)

Scored path must not depend on disallowed internet installs unless rules explicitly allow.

---

## 8. Dependency strategy

- Prefer Kaggle-preinstalled packages when possible.
- No internet-dependent installs on scored/commit path unless rules and environment allow.
- Record package versions in notebook debug cells.
- Vendor dependencies via attached datasets only with documented process and hashes.

---

## 9. Debug output cell standard

See [`docs/kaggle/notebook_debug_standard.md`](kaggle/notebook_debug_standard.md).

Minimum: Python/platform, cwd, `sys.path`, Kaggle env vars, path listings, input discovery, internet policy, GPU/CUDA, output paths, sizes, SHA256, timing, tracebacks.

---

## 10. Public notebook and write-up eligibility

Required for prize (per competition):

- **Public Kaggle notebook** — reproducible method, cites artifacts/hashes
- **Public solution write-up**

Track status in `docs/forge.md` § Documentation Eligibility Tracker. M06 locks eligibility; start planning in M00/E lane.

Do not claim eligibility without public links and evidence.

---

## 11. Evidence log requirements

Every Kaggle attempt must record:

- Date/time (UTC)
- Notebook URL / version (if available)
- Git commit SHA
- Mode (interactive / commit / submit)
- Accelerator, internet
- Attached data/model inputs
- Input paths observed
- Output paths and SHA256 hashes
- Runtime
- Errors/warnings
- Submission attempted (yes/no)
- Submission ID (if any)
- Public score **only if observed**

Primary log: [`docs/kaggle/kaggle_setup_evidence.md`](kaggle/kaggle_setup_evidence.md).

---

## 12. Prohibited claims without evidence

Do not claim without matching evidence:

- Kaggle execution success (specify mode)
- Commit-mode success implying score
- Submission readiness
- Package validity
- Public or private leaderboard score
- GPU or internet availability
- Model inference quality
- Reproducibility of notebook
- Prize eligibility

---

## 13. Troubleshooting playbook

| Symptom | Checks |
| ------- | ------ |
| Missing `/kaggle/input` data | Dataset attached? Correct competition slug? List dir |
| Adapter not found | Input mount path; filename; snapshot in debug cell |
| Missing `adapter_config.json` | Packaging script; zip listing |
| LoRA rank > 32 | `adapter_config.json`; reject before upload |
| Base model mismatch | Config vs competition requirement |
| OOM | Smaller batch; QLoRA; shorter context |
| Internet install failed | Use preinstalled or vendored deps |
| Commit OK but no submission | Separate commit vs Submit UI upload of zip |
| Submit UI rejects zip | Size, structure, rank; validator log |
| No public score | Wait for grading; check submission ID |

---

## 14. FORGE notebook development workflow

1. Create or edit under `notebooks/` in repo.
2. Include debug standard cells.
3. Commit on milestone branch.
4. Operator uploads to Kaggle.
5. Run interactive smoke first; commit/submit only when ready.
6. Log evidence; update `docs/forge.md` for material events.

---

## 15. M00 open Kaggle questions

| ID | Question | Status |
| -- | -------- | ------ |
| BQ-001 | Daily submission limit | Owner-action (Submit UI) |
| BQ-003 | Rules / team joined | Owner-action |
| — | Exact zip size / extra files | Verify on Submit UI |
| — | Kaggle API submission | TBD |

Public deadlines recorded in `docs/forge.md` (entry June 8, 2026; final June 15, 2026 23:59 UTC). Owner should reconfirm on live site.
