# FORGE — Ultimate Truth

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Last updated:** 2026-06-03  
**Status:** M00 — Anchor and competition intake (in progress)  
**Branch:** `forge/M00-anchor-intake`

---

## Authority and Update Rule

`docs/forge.md` is the active Ultimate Truth for FORGE. It records current project state, milestone status, material decisions, run outcomes, Kaggle submissions, CI posture, risks, and final candidate selection.

`docs/FORGE_ANCHOR.md` defines strategy and doctrine (canonical location: **`docs/FORGE_ANCHOR.md`**). If strategy changes materially, update this file first, then update `docs/FORGE_ANCHOR.md` only when the doctrine itself changes. Do not create duplicate anchor copies.

No milestone may close unless:
- this file is updated,
- the milestone summary exists,
- the milestone audit exists,
- all material evidence, hashes, CI state, submissions, and deferrals are recorded.

---

## 1. Competition Snapshot

| Field | Value | Source / Verification | Verified At |
| ----- | ----- | --------------------- | ----------- |
| Competition URL | <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge> | Kaggle | 2026-06-03 |
| Base model | NVIDIA-Nemotron-3-Nano-30B | Kaggle Overview | 2026-06-03 |
| Submission format | `submission.zip` containing LoRA adapter + `adapter_config.json` | Kaggle Overview | 2026-06-03 |
| LoRA rank limit | ≤ 32 | Kaggle Overview | 2026-06-03 |
| Metric | Answer accuracy (exact string or relative numerical tolerance) | Kaggle Evaluation | 2026-06-03 |
| Output format | Final answer in `\boxed{...}` | Kaggle Overview | 2026-06-03 |
| Inference | Deterministic (vLLM, fixed parameters) | Kaggle Overview | 2026-06-03 |
| Prize eligibility | Public Kaggle notebook + solution write-up required | Kaggle Rules | 2026-06-03 |
| Entry deadline | **June 8, 2026** | Kaggle public page (owner reconfirm on site) | 2026-06-03 |
| Final deadline | **June 15, 2026, 11:59 PM UTC** | Kaggle public page (owner reconfirm on site) | 2026-06-03 |
| Daily submission limit | **OWNER ACTION** — do not guess | Authenticated Kaggle Submit UI | — |
| Rules accepted | **OWNER ACTION** — do not guess | Authenticated account/team status | — |

---

## 2. Current Strategy

FORGE is a solver-guided, artifact-first, audit-governed LoRA competition system. The core thesis: reproduce a strong public control adapter, build better verified data for hard/private-style categories, train specialists, and legally merge/compress them into a rank-32 adapter that preserves solved categories while improving unsolved ones.

**Active lane priorities:**
1. Lane A — Public control reproduction (mandatory first)
2. Lane B — Solver-guided synthetic data
3. Lane E — Documentation and prize eligibility (parallel from day one)

---

## 3. Current Blocking Questions

| ID | Question | Why It Matters | Owner | Target | Status |
| -- | -------- | -------------- | ----- | ------ | ------ |
| BQ-001 | What is the live daily submission limit? | Controls submission budget | Owner | M00 | **owner-action** — authenticated Submit UI |
| BQ-002 | What are the exact entry and final deadlines? | Prevents eligibility failure | Cursor | M00 | **partial** — public dates recorded; owner reconfirm on site |
| BQ-003 | Has the team accepted rules / joined competition? | Required before submission | Owner | M00 | **owner-action** — authenticated status |
| BQ-004 | What public baseline/control repo will M01 reproduce first? | Determines M01 scope | Cursor | M01 | **resolved (recommendation)** — see § M01 Recommendation |

---

## 4. Active Milestone Exit Criteria — M00

M00 may close only when:

- [x] `docs/FORGE_ANCHOR.md` exists in canonical location (`docs/`).
- [x] `docs/forge.md` is current (M00 implementation pass).
- [ ] Live Kaggle daily submission limit is recorded (**owner-action**).
- [x] Entry deadline and final deadline are recorded (public dates; owner reconfirm).
- [ ] Rules/team entry status is verified (**owner-action**).
- [x] Repo scaffold exists.
- [x] `docs/milestones/M00/M00_plan.md` exists.
- [ ] `docs/milestones/M00/M00_summary.md` exists (closeout).
- [ ] `docs/milestones/M00/M00_audit.md` exists (closeout).
- [x] M01 recommendation is recorded (below).
- [x] `docs/kaggle_submission_bible.md` exists (FORGE-specific).
- [x] `docs/kaggle/kaggle_setup_runbook.md`, `kaggle_setup_evidence.md`, `notebook_debug_standard.md` exist.

---

## 5. Milestone Ledger

| Milestone | Title | Branch | Status | CI | Audit Score | Summary |
| --------- | ----- | ------ | ------ | -- | ----------- | ------- |
| M00 | Anchor and competition intake | `forge/M00-anchor-intake` | in progress | local verify only | — | — |
| M01 | Public control reproduction | `forge/M01-control-baseline` (planned) | not started | — | — | — |
| M02 | Exact local evaluation | — | not started | — | — | — |
| M03 | Solver and synthetic trace factory | — | not started | — | — | — |
| M04 | Adapter sweep | — | not started | — | — | — |
| M05 | Merge and compression lab | — | not started | — | — | — |
| M06 | Final documentation and eligibility | — | not started | — | — | — |
| M07 | Final submission lock | — | not started | — | — | — |

---

## 6. Submission Ledger

| Submission ID | Date | Candidate | Adapter Hash | Zip Hash | Public Score | Notes |
| ------------- | ---- | --------- | ------------ | -------- | ------------ | ----- |
| — | — | — | — | — | — | No submissions yet |

---

## 7. Run Ledger

| Run ID | Date | Config Hash | Dataset Hash | Adapter Hash | Local Score | Category Scores | Notes |
| ------ | ---- | ----------- | ------------ | ------------ | ----------- | --------------- | ----- |
| — | — | — | — | — | — | — | No runs yet |

---

## 8. Dataset Ledger

| Dataset Version | Source | Category Counts | Verification Rate | Holdout Check | Notes |
| --------------- | ------ | --------------- | ----------------- | ------------- | ----- |
| — | — | — | — | — | No datasets yet |

---

## 9. Holdout Register

| Holdout | Purpose | Source | Size | Hash | Status | Notes |
| ------- | ------- | ------ | ---- | ---- | ------ | ----- |
| public_train_holdout | Baseline/generalization check | TBD | TBD | TBD | planned | Must not enter training |
| synthetic_balanced_holdout | Broad synthetic regression | TBD | TBD | TBD | planned | Must not enter training |
| hard_category_holdout | Private-style hard categories | TBD | TBD | TBD | planned | Must not enter training |
| formatting_edge_holdout | `\boxed{}` / extractor stress | TBD | TBD | TBD | planned | Must not enter training |

---

## 10. Adapter Candidate Board

### Control
| Candidate | Family | Rank | Local Score | Public Score | Status |
| --------- | ------ | ---- | ----------- | ------------ | ------ |
| — | — | — | — | — | No control yet |

### Specialists
| Candidate | Family | Target Category | Rank | Local Score | Status |
| --------- | ------ | --------------- | ---- | ----------- | ------ |
| — | — | — | — | — | No specialists yet |

### Merged/Compressed
| Candidate | Ingredients | Rank | Local Score | Public Score | Status |
| --------- | ----------- | ---- | ----------- | ------------ | ------ |
| — | — | — | — | — | No merged candidates yet |

### Final Shortlist
| Candidate | Role | Package Hash | Public Score | Selected |
| --------- | ---- | ------------ | ------------ | -------- |
| — | — | — | — | — |

---

## 11. Candidate Promotion Gates

A candidate may advance only when all applicable gates are satisfied:

| Gate | Required Evidence |
| ---- | ----------------- |
| Package validity | Submission validator pass, package hash recorded |
| Rank compliance | LoRA rank ≤ 32 confirmed |
| Local metric | Local score and category scores recorded |
| Regression posture | Control comparison recorded |
| Data provenance | Dataset/config hashes recorded |
| Holdout discipline | No holdout contamination known |
| Submission evidence | Kaggle submission ID and public score recorded if submitted |
| Documentation impact | Notebook/write-up implications recorded when relevant |

---

## 12. Risk and Deferral Register

| Risk | Impact | Mitigation | Owner | Target Milestone | Exit Criteria | Status |
| ---- | ------ | ---------- | ----- | ---------------- | ------------- | ------ |
| Invalid submission package | Wastes submissions | Package validator before every upload | — | M01 | Validator implemented and passes | open |
| Public leaderboard overfit | Poor private score | Hard holdouts + anti-forgetting gates | — | M02+ | Per-category gates enforced | open |
| Documentation ineligibility | Prize loss | Public notebook/write-up in M06 | — | M06 | Notebook and write-up public | open |
| Daily submission limit unknown | Poor slot allocation | Verify in Kaggle Submit UI | Owner | M00 | Limit recorded in Competition Snapshot | **owner-action** |
| Hard-category misidentification | Training time wasted | Control error analysis before major data generation | — | M01/M02 | Error taxonomy exists | open |
| Catastrophic forgetting | Public/local score regression | Per-category anti-forgetting gates | — | M04+ | Control categories preserved | open |
| Data leakage / rule violation | Disqualification risk | Provenance + holdout checks | — | M02+ | Dataset manifest and contamination check pass | open |
| Unreproducible notebook | Prize eligibility risk | Notebook cites exact hashes and instructions | — | M06 | Public notebook reruns or documents limits | open |
| Authenticated Kaggle facts unavailable to Cursor | Wrong intake or guessed limits | Owner-action blockers in evidence docs | Owner | M00 | BQ-001, BQ-003 filled from live UI | open |

---

## 13. Documentation Eligibility Tracker

| Artifact | Status | Public Link | Hash | Notes |
| -------- | ------ | ----------- | ---- | ----- |
| Kaggle notebook | not started | — | — | Required for prize |
| Solution write-up | not started | — | — | Required for prize |
| Training instructions | not started | — | — | — |
| Dataset provenance | not started | — | — | — |
| Contribution award form | not applicable | — | — | — |

---

## 14. Environment and Compute Ledger

| Environment ID | Hardware | OS | Python/CUDA | Purpose | Status | Notes |
| -------------- | -------- | -- | ----------- | ------- | ------ | ----- |
| local_5090 | RTX 5090 Blackwell | TBD | TBD | Local eval, QLoRA tests, generation | available | Verify CUDA stack |
| kaggle_notebook | Kaggle GPU/Notebook | TBD | TBD | Public notebook eligibility | planned | Must remain reproducible |

---

## 15. Final Decision Log

*No final decisions yet. This section will document why final candidates were selected.*

---

## M01 Recommendation (from M00)

M01 should inspect and attempt to reproduce or wrap the public Progress Prize control baseline from [tonghuikang/nemotron](https://github.com/tonghuikang/nemotron), beginning with boxed-answer metric extraction and package validation before any Kaggle submission.

This is a **recommended control target**, not a reproduced baseline. The repo identifies itself as the Progress Prize winning submission and exposes training flow entry points (`reasoning.py`, `augmentation.py`, `corpus.py`, `train_sft.py`, `upload_adapter.py`).

Stub plan: `docs/milestones/M01/M01_plan.md`.

---

## Appendix: Material Decisions

| Date | Milestone | Decision | Rationale |
| ---- | --------- | -------- | --------- |
| 2026-06-03 | M00 | Initialize FORGE project | Late entry but sufficient time for final prize attempt |
| 2026-06-03 | M00 | Canonical anchor at `docs/FORGE_ANCHOR.md` | Single doctrine copy; no repo-root duplicate |
| 2026-06-03 | M00 | Public deadlines recorded from Kaggle public sources | Entry Jun 8, 2026; final Jun 15, 2026 23:59 UTC; owner reconfirm |
| 2026-06-03 | M00 | M01 control baseline recommendation | `tonghuikang/nemotron` Progress Prize repo |
| 2026-06-03 | M00 | Notebook workflow | Repo edit → commit → Kaggle reupload; no default Kaggle-site edits |
