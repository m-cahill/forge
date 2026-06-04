# FORGE — Ultimate Truth

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Last updated:** 2026-06-04  
**Status:** M00 and M01 **merged** to `main`; **active milestone:** M02 planning (not started)  
**Main SHA:** `d59d97b91252f9236e374292bbba8f9027edcbc1` (M01 squash merge via PR [#2](https://github.com/m-cahill/forge/pull/2))  
**M01 PR head (pre-merge):** `94d29f289dee778b45e2ec8da707112a75e86bdf` · final PR CI [26935090190](https://github.com/m-cahill/forge/actions/runs/26935090190)

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
| BQ-001 | What is the live daily submission limit? | Controls submission budget | Owner | Pre-M01 submit | **owner-action** — authenticated Submit UI |
| BQ-002 | What are the exact entry and final deadlines? | Prevents eligibility failure | Cursor | M00 | **partial** — public dates recorded; owner reconfirm on site |
| BQ-003 | Has the team accepted rules / joined competition? | Required before submission | Owner | Pre-M01 submit | **owner-action** — authenticated status |
| BQ-004 | What public baseline/control repo will M01 reproduce first? | Determines M01 scope | Cursor | M01 | **resolved (recommendation)** — `tonghuikang/nemotron`; see § M01 Recommendation |

---

## 4. M00 Closeout Record

**Branch:** `forge/M00-anchor-intake` (merged)  
**PR:** [#1](https://github.com/m-cahill/forge/pull/1) — **merged** 2026-06-04 (squash)  
**Squash merge commit on `main`:** `27d0fed5b62cd3dbef95f8ba32afc6ef4e96d408`  
**PR head at merge:** `e9f5ed563a23bade8881ea6fba1ef6b78d6dd4da`  
**CI:** Not configured — no GitHub Actions workflows; no PR CI; **no post-merge CI**  
**Post-merge local verification (`main`):** `compileall` pass; `import forge_nemotron` pass; `pytest` exit 5 / 0 tests collected

### M00 exit criteria

| Criterion | Status |
| --------- | ------ |
| `docs/FORGE_ANCHOR.md` at `docs/` | Met |
| `docs/forge.md` current | Met |
| Kaggle bible + runbooks | Met |
| Public entry/final deadlines | Met (owner reconfirm recommended) |
| Daily submission limit | **Deferred** — owner-action (DEF-001) |
| Rules/team status | **Deferred** — owner-action (DEF-002) |
| Repo scaffold | Met |
| `M00_plan.md`, `M00_toolcalls.md` | Met |
| `M00_summary.md`, `M00_audit.md` | Met |
| M01 recommendation | Met |
| No false submission/score/training claims | Met |

**Artifacts:** [`docs/milestones/M00/M00_summary.md`](milestones/M00/M00_summary.md) · [`docs/milestones/M00/M00_audit.md`](milestones/M00/M00_audit.md) (audit score **4.0/5**)

---

## 5. Milestone Ledger

| Milestone | Title | Branch | Status | CI | Audit Score | Summary |
| --------- | ----- | ------ | ------ | -- | ----------- | ------- |
| M00 | Anchor and competition intake | `forge/M00-anchor-intake` → `main` | **merged** (`27d0fed`) | not configured; local verify pass | 4.0/5 | [M00_summary](milestones/M00/M00_summary.md) |
| M01 | Public control reproduction foundation | `forge/M01-control-baseline` → `main` | **merged** (`d59d97b`) | **green** — post-merge [26935381116](https://github.com/m-cahill/forge/actions/runs/26935381116) | 4.5/5 | [M01_summary](milestones/M01/M01_summary.md) |
| M02 | Exact local evaluation and artifact discipline | `forge/M02-local-eval` (planned) | **next** — not started | — | — | [M02_plan](milestones/M02/M02_plan.md) (stub) |
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

| Risk | Impact | Mitigation | Owner | Target | Exit Criteria | Status |
| ---- | ------ | ---------- | ----- | ------ | ------------- | ------ |
| Invalid submission package | Wastes submissions | Package validator before every upload | — | M01 | Validator implemented and passes | **resolved** — validator implemented |
| Public leaderboard overfit | Poor private score | Hard holdouts + anti-forgetting gates | — | M02+ | Per-category gates enforced | open |
| Documentation ineligibility | Prize loss | Public notebook/write-up in M06 | — | M06 | Notebook and write-up public | open |
| Daily submission limit unknown | Poor slot allocation | Owner verifies Submit UI | Owner | Pre-M01 submit | BQ-001 closed; value in §1 Competition Snapshot | **owner-action** |
| Rules/team not verified | Eligibility failure | Owner verifies competition enrollment | Owner | Pre-M01 submit | BQ-003 closed; evidence row filled | **owner-action** |
| Authenticated Kaggle facts unavailable to Cursor | Guessed limits / wrong intake | Owner-action blockers only | Owner | Pre-M01 submit | DEF-001, DEF-002 closed | open |
| Hard-category misidentification | Training time wasted | Control error analysis | — | M01/M02 | Error taxonomy exists | open |
| Catastrophic forgetting | Score regression | Anti-forgetting gates | — | M04+ | Control categories preserved | open |
| Data leakage / rule violation | Disqualification | Provenance + holdout checks | — | M02+ | Contamination check pass | open |
| Unreproducible notebook | Prize risk | Notebook cites hashes | — | M06 | Public notebook documented | open |
| No CI workflow | Regressions undetected | Add CI in M01+ | — | M01+ | Green workflow on PR (DEF-005) | **resolved** — PR #2 run 26935049071 green on head |

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

## M01 Closeout Record

**Branch:** `forge/M01-control-baseline` (merged)  
**PR:** [#2](https://github.com/m-cahill/forge/pull/2) — **merged** 2026-06-04 (squash)  
**Squash merge commit on `main`:** `d59d97b91252f9236e374292bbba8f9027edcbc1`  
**PR head at merge:** `94d29f289dee778b45e2ec8da707112a75e86bdf`  
**Implementation commit (on branch):** `a901b3bdd793734fd3a07e13566e709d1e7536d3`  
**PR CI (final head):** **Green** — [26935090190](https://github.com/m-cahill/forge/actions/runs/26935090190)  
**Post-merge CI on `main`:** **Green** — [26935381116](https://github.com/m-cahill/forge/actions/runs/26935381116) on `d59d97b` (push; Python 3.10–3.12)  
**Local verification (pre-merge):** 91 pytest passed; ruff/mypy/compileall pass; `forge_nemotron` 0.1.0

**Artifacts:** [M01_summary](milestones/M01/M01_summary.md) · [M01_audit](milestones/M01/M01_audit.md) (4.5/5) · [M01_run1](milestones/M01/M01_run1.md)

### M01 deliverables

| Deliverable | Status |
| ----------- | ------ |
| `pyproject.toml` / editable install | Met |
| CI workflow | Met — green on PR #2 |
| Boxed-answer metric + tests | Met — 61 tests |
| Package validator + tests | Met — 27 tests; rank >32 rejected |
| Public baseline intake | Met — no reproduction claim |
| Kaggle debug notebook | Met — repo only |
| Kaggle submission / score / reproduction | **Not claimed** |

### Owner-action blockers (unchanged)

- **BQ-001:** Daily submission limit — authenticated Submit UI
- **BQ-003:** Rules/team status — authenticated account

Do not submit to Kaggle until these are recorded with evidence.

### Next recommendation

1. **Owner:** Complete BQ-001, BQ-003, deadline reconfirm, and Submit UI zip constraints; update `docs/kaggle/kaggle_setup_evidence.md`.  
2. **Owner:** Reupload/run `notebooks/forge_m01_kaggle_debug_probe.ipynb` on Kaggle (interactive probe only; no submission).  
3. **Cursor (when authorized):** Expand M02 plan and implement on `forge/M02-local-eval` — local eval CLI, manifests, golden metric tests, artifact hashing.  
4. **Defer:** Public baseline training/reproduction until M02 eval discipline is in place.

---

## Appendix: Material Decisions

| Date | Milestone | Decision | Rationale |
| ---- | --------- | -------- | --------- |
| 2026-06-03 | M00 | Initialize FORGE project | Late entry; final prize attempt |
| 2026-06-03 | M00 | Canonical anchor at `docs/FORGE_ANCHOR.md` | Single doctrine copy |
| 2026-06-03 | M00 | Public deadlines from Kaggle public sources | Entry Jun 8; final Jun 15 23:59 UTC |
| 2026-06-03 | M00 | M01 baseline recommendation | `tonghuikang/nemotron` |
| 2026-06-03 | M00 | Notebook workflow repo-first | Commit in repo → reupload Kaggle |
| 2026-06-04 | M00 | M00 closed with owner-action deferrals | BQ-001/BQ-003 not guessed; audit 4.0/5 |
| 2026-06-04 | M00 | CI deferred | No `.github/workflows`; local verify only |
| 2026-06-04 | M00 | PR #1 squash-merged to `main` | `27d0fed`; no post-merge CI |
| 2026-06-04 | M01 | Kickoff planning branch | `forge/M01-control-baseline`; preflight before reproduction |
| 2026-06-04 | M01 | CI strategy selected | Option A — minimal CI in M01 (owner authorized) |
| 2026-06-04 | M01 | Implementation complete | pyproject.toml, boxed metric, package validator, CI workflow, baseline intake, debug notebook |
| 2026-06-04 | M01 | PR #2 opened; CI green | Run 26934972365; 91 tests; audit 4.5/5 |
| 2026-06-04 | M01 | M01 closed (not merged) | Summary/audit/run1; M02 stub seeded |
| 2026-06-04 | M01 | PR #2 squash-merged to `main` | `d59d97b`; post-merge CI 26935381116 green |
