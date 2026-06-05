# FORGE — Ultimate Truth

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Last updated:** 2026-06-06 (M11 active on `forge/M11-credential-cost-closure`)  
**Status:** M00–M10 **merged** to `main`; **M11 active** — credential/cost closure  
**Main SHA:** `9cd7fd8` (post-M10 forge update)  
**M10 PR head (pre-merge):** `e079f87` · PR CI [27027813185](https://github.com/m-cahill/forge/actions/runs/27027813185) **green**  
**Post-merge CI on `main`:** [27032692673](https://github.com/m-cahill/forge/actions/runs/27032692673) **green**  
**M11 authorization:** kickoff **yes** · `M11_LOCAL_CUDA_SETUP_AUTHORIZED = no` · `M11_TRAINING_AUTHORIZED = no`  
**M11 owner preference:** `prefer_local_cuda` (M12 routing only — not Gate D)  
**M10 probe classification:** `visible_no_torch_cuda` — GPU visible; PyTorch CPU-only; **not** training readiness

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
| Entry / team merger deadline | **June 8, 2026** | Owner — live Kaggle competition page (logged in) | 2026-06-04 |
| Final submission deadline | **June 15, 2026, 11:59 PM UTC** | Owner — live Kaggle competition page (logged in) | 2026-06-04 |
| Daily submission limit | **5 per day** (0/5 used at probe) | Kaggle Submit UI + M01 debug probe | 2026-06-04 |
| Rules accepted / team joined | **Yes** (Submit UI accessible) | Owner — authenticated competition/Rules UI | 2026-06-04 |
| Official rules archive | [`docs/competition_rules.md`](competition_rules.md) | Owner-provided rules text | 2026-06-05 |
| Team size limit | **5** | Competition rules §2.1 | 2026-06-05 |
| Final submissions for judging | **Up to 2** | Competition rules §2.2.b | 2026-06-05 |
| Data license | **CC BY 4.0** (NVIDIA Research attribution) | Competition rules §4.a | 2026-06-05 |
| Prize documentation | Public Kaggle notebook + solution write-up required | Competition rules §8.c | 2026-06-05 |
| Winner code obligations | Training code, inference code, methodology, compute environment | Competition rules §8.a | 2026-06-05 |
| External data/tools | Allowed if reasonably accessible / minimal cost and compliant | Competition rules §6 | 2026-06-05 |
| Private code sharing | Prohibited outside team (public sharing on Kaggle permitted) | Competition rules §3.10 | 2026-06-05 |
| Multiple Kaggle accounts | Prohibited | Competition rules (intro) | 2026-06-05 |
| Submit UI zip constraints | **OPEN** — not recorded | Owner-action | — |

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
| BQ-001 | What is the live daily submission limit? | Controls submission budget | Owner | Pre-M01 submit | **resolved** — 5 per day (Submit UI `0/5 used`; probe 2026-06-04) |
| BQ-002 | What are the exact entry and final deadlines? | Prevents eligibility failure | Owner | M00 | **resolved** — entry Jun 8; final Jun 15 23:59 UTC (owner live page 2026-06-04) |
| BQ-003 | Has the team accepted rules / joined competition? | Required before submission | Owner | Pre-M01 submit | **resolved** — yes; Submit UI accessible (owner 2026-06-04) |
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
| M02 | Exact local evaluation and artifact discipline | `forge/M02-local-eval` → `main` | **merged** (`e78dc97`) | **green** — post-merge [26973864069](https://github.com/m-cahill/forge/actions/runs/26973864069) | 4.6/5 | [M02_summary](milestones/M02/M02_summary.md) |
| M03 | Solver and synthetic trace factory | `forge/M03-solver-factory` → `main` | **merged** (`fe2a7dd`) | **green** — post-merge [26976448338](https://github.com/m-cahill/forge/actions/runs/26976448338) | 4.7/5 | [M03_summary](milestones/M03/M03_summary.md) |
| M04 | Public control adapter reproduction preflight | `forge/M04-control-preflight` → `main` | **merged** (`f54afd0`) | **green** — post-merge [26979013700](https://github.com/m-cahill/forge/actions/runs/26979013700) | 4.6/5 | [M04_summary](milestones/M04/M04_summary.md) |
| M05 | Controlled public baseline reproduction planning | `forge/M05-control-repro-planning` → `main` | **merged** (`34169d0`) | **green** — post-merge [26983281413](https://github.com/m-cahill/forge/actions/runs/26983281413) | 4.6/5 | [M05_summary](milestones/M05/M05_summary.md) |
| M06 | Controlled public baseline reproduction execution gate | `forge/M06-control-repro-execution-gate` → `main` | **merged** (`a7de356`) | **green** — post-merge [26985969954](https://github.com/m-cahill/forge/actions/runs/26985969954) | 4.6/5 | [M06_summary](milestones/M06/M06_summary.md) |
| M07 | Controlled public baseline training authorization gate | `forge/M07-training-authorization-gate` → `main` | **merged** (`06ada17`) | **green** — post-merge [26988100314](https://github.com/m-cahill/forge/actions/runs/26988100314) | 4.6/5 | [M07_summary](milestones/M07/M07_summary.md) |
| M08 | Compute and credential readiness closure | `forge/M08-compute-credential-readiness` → `main` | **merged** (`ac7c5f2`) | **green** — post-merge [26989604207](https://github.com/m-cahill/forge/actions/runs/26989604207) | 4.6/5 | [M08_summary](milestones/M08/M08_summary.md) |
| M09 | Modal/Tinker setup gate | `forge/M09-modal-tinker-setup-gate` → `main` | **merged** (`5a4300b`) | **green** — post-merge [26991673323](https://github.com/m-cahill/forge/actions/runs/26991673323) | 4.6/5 | [M09_summary](milestones/M09/M09_summary.md) |
| M10 | Local 5090 feasibility probe | `forge/M10-local-5090-feasibility-probe` → `main` | **merged** (`dc45813`) | **green** — post-merge [27032692673](https://github.com/m-cahill/forge/actions/runs/27032692673) | 4.6/5 | [M10_summary](milestones/M10/M10_summary.md) |
| M11 | Credential and cost closure continuation | `forge/M11-credential-cost-closure` | **active** | pending PR | — | [M11_plan](milestones/M11/M11_plan.md) |

---

## 6. Submission Ledger

| Submission ID | Date | Candidate | Adapter Hash | Zip Hash | Public Score | Notes |
| ------------- | ---- | --------- | ------------ | -------- | ------------ | ----- |
| — | — | — | — | — | — | No submissions yet |

---

## 7. Run Ledger

| Run ID | Date | Config Hash | Dataset Hash | Adapter Hash | Local Score | Category Scores | Notes |
| ------ | ---- | ----------- | ------------ | ------------ | ----------- | --------------- | ----- |
| m02_fixture_eval | 2026-06-04 | — | `c7ff8ec140feabcee037ddb16b279d68ac1704998d7e34e3d8290d7dd8162219` | — | **0.75** (6/8; fixture only) | [evidence CSV](milestones/M02/evidence/fixture_eval/local_eval_by_category.csv) | **Not** a Kaggle/public score; hand-authored fixture; [evidence](milestones/M02/evidence/fixture_eval/) |
| m03_synthetic_smoke_eval | 2026-06-04 | — | `d177d827b3ba1c066c754f875a0a162f780cbb4dc43be7c004fa18093e4b21df` | — | **1.0** (50/50; synthetic factory self-check) | [evidence CSV](milestones/M03/evidence/synthetic_smoke/local_eval_by_category.csv) | **Not** a model or leaderboard score; [evidence](milestones/M03/evidence/synthetic_smoke/) |

---

## 8. Dataset Ledger

| Dataset Version | Source | Category Counts | Verification Rate | Holdout Check | Notes |
| --------------- | ------ | --------------- | ----------------- | ------------- | ----- |
| m03_synthetic_smoke_v1 | m03_synthetic (solver-verified) | arithmetic 20, string 20, formatting 10 | 100% verified | not production holdout | SHA256 `d177d827b3ba1c066c754f875a0a162f780cbb4dc43be7c004fa18093e4b21df`; [evidence](milestones/M03/evidence/synthetic_smoke/); **not for training** unless reclassified |

---

## 9. Holdout Register

| Holdout | Purpose | Source | Size | Hash | Status | Notes |
| ------- | ------- | ------ | ---- | ---- | ------ | ----- |
| public_train_holdout | Baseline/generalization check | TBD | TBD | TBD | planned | Must not enter training |
| synthetic_balanced_holdout | Broad synthetic regression | TBD | TBD | TBD | planned | Must not enter training |
| hard_category_holdout | Private-style hard categories | TBD | TBD | TBD | planned | Must not enter training |
| formatting_edge_holdout | `\boxed{}` / extractor stress | TBD | TBD | TBD | planned | Must not enter training |
| m02_fixture_holdout | Local eval smoke / fixture validation | `tests/fixtures/eval` | 8 examples | `c7ff8ec140feabcee037ddb16b279d68ac1704998d7e34e3d8290d7dd8162219` | **active-fixture** | Evaluation-only; never train; not leaderboard data |

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
| Public leaderboard overfit | Poor private score | Hard holdouts + anti-forgetting gates | — | M02+ | Per-category gates enforced | open — local per-category reporting exists (M02); production holdouts TBD |
| Fixture score mistaken for leaderboard | Wrong promotion decisions | Label evidence + forge Run Ledger | — | M02 | Fixture 0.75 explicitly not public score | **mitigated** — M02 evidence README + audit GOV-003 |
| Documentation ineligibility | Prize loss | Public notebook/write-up in M06 | — | M06 | Notebook and write-up public | open |
| Daily submission limit unknown | Poor slot allocation | Owner verifies Submit UI | Owner | Pre-M01 submit | BQ-001 closed; value in §1 Competition Snapshot | **resolved** — 5/day (2026-06-04) |
| Rules/team not verified | Eligibility failure | Owner verifies competition enrollment | Owner | Pre-M01 submit | BQ-003 closed; evidence row filled | **resolved** — 2026-06-04 |
| Authenticated Kaggle facts unavailable to Cursor | Guessed limits / wrong intake | Owner-action blockers only | Owner | Pre-M01 submit | DEF-001, DEF-002 closed | **resolved** — intake recorded 2026-06-04 |
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
| local_5090 | NVIDIA GeForce RTX 5090 | Windows 10.0.26200 | Py3.11.9; driver 591.86; torch 2.2.2+cpu (**CUDA false**) | Local eval, QLoRA tests, generation | **probed** — `visible_no_torch_cuda` | [M10 probe](milestones/M10/evidence/local_5090_probe/local_5090_probe.json) 2026-06-05; ~32607 MiB VRAM; **not** training-ready |
| kaggle_notebook | Kaggle Notebook (CPU at probe) | Linux 6.6 / Py3.12 | torch 2.10+cpu; no CUDA | M01 debug probe | probed 2026-06-04 | Interactive; no GPU; ~19.5 GB free; see kaggle_setup_evidence |

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
| Kaggle debug notebook | Met — repo + **interactive probe run** (2026-06-04) |
| Kaggle submission / score / reproduction | **Not claimed** |

### M01 Kaggle interactive probe (2026-06-04)

**Notebook:** `notebooks/forge_m01_kaggle_debug_probe.ipynb` (repo-first; run on Kaggle Interactive)  
**Mode:** Interactive · **Is Kaggle:** true · **Submissions used:** 0/5 → **limit 5/day**  
**Environment:** Python 3.12.13; Linux `6.6.122+`; CWD `/kaggle/working`; `/kaggle/input` has `competitions`  
**Disk:** ~19.5 GB free on `/kaggle/working` · **GPU:** none (`nvidia-smi` not found)  
**Torch:** 2.10.0+cpu · **CUDA:** false  
**Base model paths:** not attached — `nemotron-3-nano-30b-a3b-bf16`, `nvidia-nemotron-3-nano-30b-a3b-bf16` not visible  
**Debug artifact:** `/kaggle/working/tmp/forge_debug/probe_test.txt` (83 B; SHA256 `a8f624087fe0520a0c0c97f914e54f4e7b6478f750b85d5f9d8e971c6e360a8c`)

**Expected outputs:** diagnostics only (e.g. `/kaggle/working/tmp/forge_debug/probe_test.txt`).  
**Does not create:** `/kaggle/working/submission.zip` — that path is for a future submission notebook, not this probe.  
**Not a probe failure:** missing `submission.zip` after this run is **by design**.

**Non-claims:** no submission, no score, no package validity, no model inference, no submission readiness.

Evidence: [`docs/kaggle/kaggle_setup_evidence.md`](kaggle/kaggle_setup_evidence.md)

### Kaggle eligibility intake (owner 2026-06-04)

| Field | Value |
| ----- | ----- |
| Rules accepted / team joined | **Yes** |
| Verified via | Authenticated competition page / Rules or Submit UI |
| Submit UI accessible | **Yes** |
| Team name | not recorded |
| Additional UI notes | not recorded (zip constraints / warnings TBD) |

Evidence: [`docs/kaggle/kaggle_setup_evidence.md`](kaggle/kaggle_setup_evidence.md)

### Owner-action blockers

- **BQ-001:** **Resolved** — 5 submissions per day
- **BQ-003:** **Resolved** — rules accepted; team joined; Submit UI accessible
- **BQ-002:** **Resolved** — entry Jun 8, 2026; final Jun 15, 2026 11:59 PM UTC (owner live page)
- **Submit UI zip constraints:** **OPEN** — owner-action / not recorded (M04 preserved)
- **Kaggle API submission support:** **TBD**

Kaggle **submission is not authorized** without a validated package, local eval, and explicit owner go-ahead. Eligibility ≠ submission readiness.

### Next recommendation

1. **Owner:** Record Submit UI `submission.zip` constraints (**OPEN** — owner-action).  
2. **Cursor:** Complete M04 on `forge/M04-control-preflight`; open PR when green CI.  
3. **Defer:** Kaggle submission until validated package + local eval on real candidates + owner go-ahead.

---

## M02 Closeout Record

**Branch:** `forge/M02-local-eval` (merged)  
**PR:** [#3](https://github.com/m-cahill/forge/pull/3) — **merged** 2026-06-04T19:15:09Z (squash)  
**Squash merge commit on `main`:** `e78dc975c278c73edffb4b920cf72a067c781420`  
**PR head (pre-merge):** `cfd39707116a218d2b44920c28479fec701be12b`  
**PR CI (final head):** [26973225572](https://github.com/m-cahill/forge/actions/runs/26973225572) **green**  
**Post-merge CI on `main`:** [26973864069](https://github.com/m-cahill/forge/actions/runs/26973864069) **green** (Python 3.10–3.12)  
**Local verification:** 106 pytest; ruff/mypy/compileall pass; fixture CLI smoke 6/8 = **0.75 (fixture only — not a public/private score)**

**Artifacts:** [M02_summary](milestones/M02/M02_summary.md) · [M02_audit](milestones/M02/M02_audit.md) (4.6/5) · [M02_run1](milestones/M02/M02_run1.md) · [fixture evidence](milestones/M02/evidence/fixture_eval/)

### M02 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Eval records + `score_examples()` | Met |
| `scripts/eval_predictions.py` + module CLI | Met |
| Per-category CSV + failures JSONL + `input_hashes.json` | Met |
| Artifact hashing utilities | Met |
| Run manifest builder | Met |
| Fixture JSONL + holdout manifest | Met |
| `m02_fixture_holdout` register row | Met — evaluation-only |
| Committed fixture evidence | Met — **not** leaderboard score |
| Kaggle submission / score / training / reproduction | **Not claimed** |

### Fixture score disclaimer

The Run Ledger value **0.75** is from `predictions_mixed.jsonl` against hand-authored fixture examples only. It is **not** a public score, private score, or model-inferred result.

**Non-claims (M02):** no Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter, fixture holdout used for training.

---

## M03 Closeout Record

**Branch:** `forge/M03-solver-factory` (merged)  
**PR:** [#4](https://github.com/m-cahill/forge/pull/4) — **merged** 2026-06-04T20:04:51Z (squash)  
**Squash merge commit on `main`:** `fe2a7dd2e38f158503a49bb81d9ff4a3573601e6`  
**PR head (pre-merge):** `ac661166a4c3b1be63df7a6aaa0d905208baaa79`  
**PR CI (final head):** [26975853847](https://github.com/m-cahill/forge/actions/runs/26975853847) **green**  
**Post-merge CI on `main`:** [26976448338](https://github.com/m-cahill/forge/actions/runs/26976448338) **green** (Python 3.10–3.12)  
**Local verification:** 127 pytest; ruff/mypy/compileall pass; `make_dataset` + synthetic factory self-check 50/50

**Artifacts:** [M03_summary](milestones/M03/M03_summary.md) · [M03_audit](milestones/M03/M03_audit.md) (4.7/5) · [M03_run1](milestones/M03/M03_run1.md) · [synthetic smoke evidence](milestones/M03/evidence/synthetic_smoke/)

### M03 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Solver protocol + arithmetic + string (3 transforms) + formatting stress | Met |
| Synthetic writer + rejection rules + writer-owned `\boxed{}` | Met |
| Dataset manifest + `scripts/make_dataset.py` | Met |
| Smoke dataset `m03_synthetic_smoke_v1` (50 examples, seed 123) | Met |
| Synthetic factory self-check 50/50 | Met — **not** model/LB score |
| Kaggle submission / score / training / reproduction | **Not claimed** |

### Synthetic self-check disclaimer

Run Ledger **1.0** for `m03_synthetic_smoke_eval` is **synthetic factory self-check accuracy** only. It is **not** a public score, private score, or model-inferred result.

**Non-claims (M03):** no Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter; smoke data is not hidden/private benchmark evidence.

---

## M04 Closeout Record

**Branch:** `forge/M04-control-preflight` (merged)  
**PR:** [#5](https://github.com/m-cahill/forge/pull/5) — **merged** 2026-06-04T20:54:54Z (squash)  
**Squash merge commit on `main`:** `f54afd0c6f01c8a8d033e2d79ac3dac512224afd`  
**PR head (pre-merge):** `e7d8429708cb5328d9f1897781ef1976e2f7d672`  
**PR CI (final head):** [26978191986](https://github.com/m-cahill/forge/actions/runs/26978191986) **green**  
**Post-merge CI on `main`:** [26979013700](https://github.com/m-cahill/forge/actions/runs/26979013700) **green** (Python 3.10–3.12)  
**Local verification:** 138 pytest; ruff/mypy/compileall pass; mock manifest `control_public_repro_preflight` validates (preflight only — not adapter/package)

**Artifacts:** [M04_summary](milestones/M04/M04_summary.md) · [M04_audit](milestones/M04/M04_audit.md) (4.6/5) · [M04_run1](milestones/M04/M04_run1.md)

### M04 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Public control preflight dossier | Met |
| Baseline format mapping | Met |
| Adapter candidate manifest contract | Met — 11 tests |
| Promotion preflight gates | Met |
| Mock preflight evidence | Met — validates |
| `validate_candidate_manifest.py` | Met |
| M04 next decision | Met — M05 planning recommended |
| Submit UI zip constraints | **OPEN** — owner-action (not guessed) |
| Kaggle submission / score / training / reproduction | **Not claimed** |

### Mock candidate disclaimer

`docs/milestones/M04/evidence/control_preflight/control_candidate_manifest.preflight.json` is **preflight-only**. Not an adapter, package, or Kaggle-ready candidate. Adapter Candidate Board unchanged (no real control).

**Non-claims (M04):** no Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, vendored/copied baseline code.

### Next recommendation

1. **Owner:** Record Submit UI `submission.zip` constraints (**OPEN**).  
2. **Cursor:** M05 implementation on `forge/M05-control-repro-planning` (authorized).  
3. **Defer:** Training, Kaggle submission, baseline reproduction claims until explicit milestone authorization.

---

## M05 Closeout Record

**Branch:** `forge/M05-control-repro-planning` (merged; branch deleted)  
**PR:** [#6](https://github.com/m-cahill/forge/pull/6) — **merged** 2026-06-04T22:25:51Z (squash)  
**Squash merge commit on `main`:** `34169d062971ac5f754b2e71e5d10c1711c0f612`  
**PR head (pre-merge):** `508f9ac080098b1f35adc58bad14c45eee46ded7`  
**PR CI (final head):** [26982740620](https://github.com/m-cahill/forge/actions/runs/26982740620) **green**  
**Post-merge CI on `main`:** [26983281413](https://github.com/m-cahill/forge/actions/runs/26983281413) **green** (Python 3.10–3.12)  
**Local verification:** 147 pytest; ruff/mypy/compileall pass; mock plan `public_control_repro_plan_v1` validates (preflight only — not training authorization / not reproduction / not adapter/package / not Kaggle-ready)

**Artifacts:** [M05_summary](milestones/M05/M05_summary.md) · [M05_audit](milestones/M05/M05_audit.md) (4.6/5) · [M05_run1](milestones/M05/M05_run1.md)

### M05 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Controlled reproduction planning docs (6) | Met |
| `reproduction_plan.py` + 9 tests | Met |
| `validate_reproduction_plan.py` | Met |
| Mock reproduction plan evidence | Met — preflight only |
| `M05_next_decision.md` | Met — M06 execution gate |
| Submit UI zip constraints | **OPEN** — owner-action (not guessed) |
| Kaggle API submission | **TBD** |
| Kaggle submission / score / training / reproduction | **Not claimed** |

### Mock reproduction plan disclaimer

`docs/milestones/M05/evidence/reproduction_plan/public_control_repro_plan.preflight.json` (`plan_id: public_control_repro_plan_v1`) is **preflight plan evidence only**. Not training authorization, baseline reproduction, real adapter/package, or Kaggle-ready submission. Adapter Candidate Board unchanged (no real control).

**Non-claims (M05):** no Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, vendored/copied baseline code/data, training authorization.

### Next recommendation

1. **Owner:** Record Submit UI `submission.zip` constraints (**OPEN**).  
2. **Owner:** Authorize M06 kickoff + training per [M05_next_decision](milestones/M05/M05_next_decision.md).  
3. **Defer:** Training, Kaggle submission, baseline reproduction claims until M06 owner authorization and manifest gates satisfied.

---

## M06 Closeout Record

**Branch:** `forge/M06-control-repro-execution-gate` (merged; branch deleted)  
**PR:** [#7](https://github.com/m-cahill/forge/pull/7) — **merged** 2026-06-04T23:33:42Z (squash)  
**Squash merge commit on `main`:** `a7de356d8597c7386b30cf8ba1912c02c0894cf7`  
**PR head at merge:** `354f630862ecd4866eb99be66e5649c1926a3a38` (impl `895a3cb`, closeout `354f630`)  
**PR CI (final head):** [26985581070](https://github.com/m-cahill/forge/actions/runs/26985581070) **green** (Python 3.10–3.12)  
**Post-merge CI on `main`:** [26985969954](https://github.com/m-cahill/forge/actions/runs/26985969954) **green** (Python 3.10–3.12)  
**Local verification:** 151 pytest; ruff/mypy/compileall pass; schema-gate manifest validates (gate only — not training authorization)

**Artifacts:** [M06_summary](milestones/M06/M06_summary.md) · [M06_audit](milestones/M06/M06_audit.md) (4.6/5) · [M06_run1](milestones/M06/M06_run1.md)

### M06 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Execution gate doc + compute/credential checklists | Met |
| Gate B schema inspection (derived notes ×4) | Met — baseline `82bd1880` |
| Baseline schema mapping supplement | Met |
| Schema-gate reproduction manifest | Met — validates |
| Reproduction plan contract extensions | Met — 4 new tests |
| M06 next decision → M07 training auth gate | Met |
| Submit UI zip constraints | **OPEN** — owner-action (not guessed) |
| Kaggle API submission | **TBD** |
| Training / inference / submission / reproduction | **Not claimed** |

### Schema inspection evidence

| File | Rows | SHA256 (prefix) |
| ---- | ---- | --------------- |
| corpus.jsonl | 17963 | `1940a41c68d0f70013e0e448e04dd17c9143403bc1ce991e4603e9ad38b9fcf5` |
| problems.jsonl | 9500 | `4b8bd8b62905fe156ffc9033f5677286e75a80e907841b0988a4b50cc4b8742e` |
| generation.jsonl | 9500 | `58383d4ecb831d9a6567a34a9cccb0a48ba78c1511790eb981c011685ccd315d` |
| train.csv | 69029 | `c99877aca84dc1564ef741a722a74458b06aa616b0b627d493a913063bd536ef` |

**Baseline commit (inspection):** `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85`  
**External clone path:** `C:\coding\nemotron-inspect` (outside FORGE tree; not in repo)  
**Committed to FORGE:** derived notes only — no raw rows, code, tokenizer, checkpoints, adapters, or credentials  
**Open mapping:** `corpus.segment` partial — SQ-CORPUS-001; `\boxed{}` not observed in inspected samples

### Schema-gate manifest disclaimer

`public_control_repro_plan.schema_gate.json` (`plan_id: public_control_repro_plan_schema_gate_v1`) is **execution-gate evidence only**. Not training authorization, baseline reproduction, real adapter/package, or Kaggle-ready submission.

**Non-claims (M06):** no Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, vendored/copied baseline code/data, committed credentials, raw baseline data in repo.

### Next recommendation

1. **Owner:** Record Submit UI `submission.zip` constraints (**OPEN**).  
2. **Owner:** Authorize M07 training gate (`training_authorized` + `owner_training_authorization` + `credentials_ready` + compute path) before any SFT/inference.  
3. **Cursor:** Expand M07 plan when owner authorizes kickoff — **do not** start M07 without explicit permission.  
4. **Defer:** Training, Kaggle submission, baseline reproduction claims until M07 Gate C satisfied.

---

## M07 Closeout Record (training authorization gate)

**Branch:** `forge/M07-training-authorization-gate` (merged; branch deleted)  
**PR:** [#8](https://github.com/m-cahill/forge/pull/8) — **merged** 2026-06-05T00:35:34Z (squash)  
**Squash merge commit on `main`:** `06ada1738c914ab23343a20f0c8864d58440256b`  
**PR head at merge:** `90cdab7dd85b1eabcb12495868c40d71595218b5`  
**PR CI (final head):** [26986758980](https://github.com/m-cahill/forge/actions/runs/26986758980) **green** (Python 3.10–3.12)  
**Post-merge CI on `main`:** [26988100314](https://github.com/m-cahill/forge/actions/runs/26988100314) **green** (Python 3.10–3.12)  
**Path:** A — `M07_TRAINING_AUTHORIZED = no`  
**Local verification:** 154 pytest; ruff/mypy/compileall pass; training_blocked manifest validates

**Artifacts:** [M07_summary](milestones/M07/M07_summary.md) · [M07_audit](milestones/M07/M07_audit.md) (4.6/5) · [M07_run1](milestones/M07/M07_run1.md)

### M07 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Training authorization gate doc | Met |
| Baseline schema readiness decision | Met — SQ-CORPUS-001 open |
| Compute/credential gate | Met — TBD preserved |
| Submit UI constraint gate | Met — OPEN preserved |
| `public_control_repro_plan.training_blocked.json` | Met — validates |
| Training config draft + dry-run plan | Met — **not executed** |
| Reproduction plan tests (+3) | Met |
| M07 next decision → M08 | Met |
| Kaggle submission / training / reproduction | **Not claimed** |

### Training-gate manifest

[`public_control_repro_plan.training_blocked.json`](milestones/M07/evidence/training_gate/public_control_repro_plan.training_blocked.json) — `training_authorized: false`, `ready_for_training: false`, `status: preflight`. **Not** training authorization or reproduction evidence.

**Non-claims (M07):** no training, inference, Kaggle submission, public/private score, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, committed credentials.

### Open blockers (post-merge)

- Submit UI `submission.zip` constraints: **OPEN** (owner-action)
- Kaggle API submission: **TBD**
- Modal/Tinker credentials: **TBD** (`credentials_ready: false`)
- local_5090 CUDA/VRAM: **TBD**
- SQ-CORPUS-001 (`corpus.segment`): **partial / open**
- Gate C training authorization: **not provided**

### Next recommendation

1. **Owner:** Record Submit UI zip constraints; provide Gate C when ready for training.  
2. **Cursor:** M08 compute/credential readiness per [M07_next_decision](milestones/M07/M07_next_decision.md) when authorized — **do not** start without kickoff.  
3. **Defer:** Training, Kaggle submission, baseline reproduction until Gate C and readiness gates satisfied.

---

## M08 Closeout Record (compute/credential readiness)

**Branch:** `forge/M08-compute-credential-readiness` (merged; branch deleted)  
**PR:** [#9](https://github.com/m-cahill/forge/pull/9) — **merged** 2026-06-05T01:22:07Z (squash)  
**Squash merge commit on `main`:** `ac7c5f249ca39181d4e167193e6d7c70e5e5a198`  
**PR head at merge:** `448692b`  
**PR CI (final head):** [26988858986](https://github.com/m-cahill/forge/actions/runs/26988858986) **green** (Python 3.10–3.12)  
**Post-merge CI on `main`:** [26989604207](https://github.com/m-cahill/forge/actions/runs/26989604207) **green** (Python 3.10–3.12)  
**Local verification:** 163 pytest; ruff/mypy/compileall pass; readiness manifest validates; probe `--help` only (probe **not** executed)

**Artifacts:** [M08_summary](milestones/M08/M08_summary.md) · [M08_audit](milestones/M08/M08_audit.md) (4.6/5) · [M08_run1](milestones/M08/M08_run1.md)

### M08 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Readiness docs (compute, credential, cost, submit UI, SQ-CORPUS, matrix) | Met |
| `probe_local_5090.py` + `gpu_probe.py` | Met — **not executed** |
| `public_control_repro_plan.readiness.json` | Met — validates |
| Validator extensions + tests (+9) | Met |
| M08 next decision → M09 | Met |
| Training / probe / submission / reproduction | **Not claimed** |

### Readiness manifest

[`public_control_repro_plan.readiness.json`](milestones/M08/evidence/readiness/public_control_repro_plan.readiness.json) — `training_authorized: false`, `ready_for_training: false`, `credentials_ready: false`, `cost_accepted: false`, `compute_path: null`. **Not** training authorization or hardware probe evidence.

**Non-claims (M08):** no local 5090 probe executed, training, inference, Kaggle submission, public/private score, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, committed credentials.

### Open blockers (post-M08)

- Submit UI `submission.zip` constraints: **OPEN**
- Kaggle API submission: **TBD**
- Modal/Tinker/cloud credentials: **TBD** (`credentials_ready: false`)
- Cost acceptance: **TBD** (`cost_accepted: false`)
- local_5090 CUDA/VRAM: **TBD** (probe script exists; not run)
- SQ-CORPUS-001: **open**
- Gate C training authorization: **not provided**

### Authorization state (post-merge)

| Field | Value |
| ----- | ----- |
| `M08_LOCAL_5090_PROBE_AUTHORIZED` | **no** |
| Local 5090 probe executed | **no** |
| `M08_TRAINING_AUTHORIZED` | **no** |
| `credentials_ready` | **false** |
| `cost_accepted` | **false** / TBD |
| Probe script | exists; CUDA/driver/VRAM **TBD** |

### Next recommendation

1. **Owner:** Supply Modal/Tinker/cost status (no secrets); record Submit UI constraints.  
2. **Cursor:** M10 credential/cost closure per [M09_next_decision](milestones/M09/M09_next_decision.md) when authorized — **not started**.  
3. **Defer:** Training, Kaggle submission, baseline reproduction, local probe execution until separately authorized.

---

## M09 Closeout Record (Modal/Tinker setup gate)

**Branch:** `forge/M09-modal-tinker-setup-gate` (merged; branch deleted)  
**PR:** [#10](https://github.com/m-cahill/forge/pull/10) — **merged** 2026-06-05T02:28:19Z (squash)  
**Squash merge commit on `main`:** `5a4300bb1f7b873750089c773e8c0e789f15f870`  
**PR head at merge:** `9be2687`  
**PR CI (final head):** [26990319778](https://github.com/m-cahill/forge/actions/runs/26990319778) **green** (Python 3.10–3.12)  
**Post-merge CI on `main`:** [26991673323](https://github.com/m-cahill/forge/actions/runs/26991673323) **green** (Python 3.10–3.12)  
**Local verification:** 166 pytest; ruff/mypy/compileall pass; modal_tinker_gate manifest validates; probe **not** executed

**Artifacts:** [M09_summary](milestones/M09/M09_summary.md) · [M09_audit](milestones/M09/M09_audit.md) (4.6/5) · [M09_run1](milestones/M09/M09_run1.md)

### M09 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Modal/Tinker readiness evidence | Met — **TBD** (no owner evidence) |
| External compute path decision | Met |
| Credential storage policy check | Met |
| Kaggle API / Submit UI status | Met — OPEN/TBD preserved |
| Local 5090 probe blocked | Met — probe **not** run |
| SQ-CORPUS-001 status | Met — open; prefer `train.csv` |
| `public_control_repro_plan.modal_tinker_gate.json` | Met — validates |
| Validator extensions (+3 tests) | Met |
| M09 next decision → M10 | Met — credential/cost closure |
| Training / probe / submission / reproduction | **Not claimed** |

### Modal/Tinker gate manifest

[`public_control_repro_plan.modal_tinker_gate.json`](milestones/M09/evidence/readiness/public_control_repro_plan.modal_tinker_gate.json) — `training_authorized: false`, `ready_for_training: false`, `credentials_ready: false`, `cost_accepted: false`, `modal_account_status: tbd`, `tinker_account_status: tbd`, `compute_path: null`. **Not** training authorization or credential functionality evidence.

**Non-claims (M09):** no local 5090 probe executed, training, inference, Kaggle submission, public/private score, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, committed credentials.

### Open blockers (post-merge)

- Submit UI `submission.zip` constraints: **OPEN**
- Kaggle API submission: **TBD**
- Modal/Tinker/cloud credentials: **TBD** (`credentials_ready: false`)
- Cost acceptance: **TBD** (`cost_accepted: false`)
- local_5090 CUDA/VRAM: **TBD** (probe not run)
- SQ-CORPUS-001: **open**
- Gate C training authorization: **not provided**

### Authorization state (post-merge)

| Field | Value |
| ----- | ----- |
| `M09_LOCAL_5090_PROBE_AUTHORIZED` | **no** |
| Local 5090 probe executed | **no** |
| `M09_TRAINING_AUTHORIZED` | **no** |
| `credentials_ready` | **false** |
| `cost_accepted` | **false** |
| Modal/Tinker status | **TBD** |

### Next recommendation

1. **Owner:** Supply Modal/Tinker/cost status (no secrets); record Submit UI constraints.  
2. **Cursor:** M10 credential/cost closure per [M09_next_decision](milestones/M09/M09_next_decision.md) when authorized — **not started**.  
3. **Defer:** Training, Kaggle submission, baseline reproduction, local probe until separately authorized.

---

## M10 Closeout Record (Local 5090 Feasibility Probe)

**Branch:** `forge/M10-local-5090-feasibility-probe` (merged; branch deleted)  
**PR:** [#11](https://github.com/m-cahill/forge/pull/11) — **merged** 2026-06-05T18:26:01Z (squash)  
**Squash merge commit on `main`:** `dc45813`  
**PR head at merge:** `e079f87`  
**PR CI (final head):** [27027813185](https://github.com/m-cahill/forge/actions/runs/27027813185) **green** (Python 3.10–3.12)  
**Post-merge CI on `main`:** [27032692673](https://github.com/m-cahill/forge/actions/runs/27032692673) **green** (Python 3.10–3.12)  
**Local verification:** 171 pytest; ruff/mypy/compileall pass; probe executed; manifest validates  
**Supersedes:** M09-seeded M10 stub “Credential and Cost Closure”; M08/M09 `local_5090` TBD fields for this host

### Authorization state

| Field | Value |
| ----- | ----- |
| `M10_LOCAL_5090_PROBE_AUTHORIZED` | **yes** |
| `M10_TRAINING_AUTHORIZED` | **no** |
| `M10_INFERENCE_AUTHORIZED` | **no** |
| `KAGGLE_SUBMISSION_AUTHORIZED` | **no** |

### Probe summary (2026-06-05)

| Field | Value |
| ----- | ----- |
| `nvidia-smi` | available |
| GPU | NVIDIA GeForce RTX 5090 |
| VRAM (MiB) | 32607 |
| Driver | 591.86 |
| PyTorch | 2.2.2+cpu |
| `torch.cuda.is_available()` | **false** |
| Classification | **`visible_no_torch_cuda`** |
| Evidence | [`local_5090_probe.json`](milestones/M10/evidence/local_5090_probe/local_5090_probe.json) |
| Report | [`local_5090_probe_report.md`](milestones/M10/local_5090_probe_report.md) |
| Readiness manifest | [`public_control_repro_plan.local_5090_probe.json`](milestones/M10/evidence/readiness/public_control_repro_plan.local_5090_probe.json) |

### Cross-references

- M08 compute readiness and M09 external compute path docs remain historical; M10 probe evidence supersedes their `local_5090` TBD fields for this host.
- Submit UI `submission.zip` constraints: **OPEN**
- Kaggle API submission: **TBD**

### M10 deliverables

| Deliverable | Status |
| ----------- | ------ |
| Local 5090 probe executed | Met — `visible_no_torch_cuda` |
| Probe JSON + README + report | Met |
| `public_control_repro_plan.local_5090_probe.json` | Met — validates |
| Validator extensions (+5 tests) | Met |
| Competition rules archive | Met |
| M10_next_decision → M11 | Met — credential/cost closure primary |
| Training / submission / reproduction | **Not claimed** |

**Artifacts:** [M10_summary](milestones/M10/M10_summary.md) · [M10_audit](milestones/M10/M10_audit.md) (4.6/5) · [M10_run1](milestones/M10/M10_run1.md)

### Open blockers (post-merge)

- CUDA-enabled PyTorch: **unavailable** in active environment (`2.2.2+cpu`; `torch.cuda.is_available(): false`)
- Submit UI `submission.zip` constraints: **OPEN**
- Kaggle API submission: **TBD**
- Modal/Tinker/cloud credentials: **TBD** (`credentials_ready: false`)
- Cost acceptance: **TBD** (`cost_accepted: false`)
- SQ-CORPUS-001: **open**
- Gate C training authorization: **not provided**

### Next recommendation

**M11 — Credential and Cost Closure Continuation** per [M10_next_decision](milestones/M10/M10_next_decision.md). Secondary: local CUDA PyTorch install + feasibility dry run if owner prefers local path. **Do not start M11** without owner kickoff.

**Non-claims (M10):** no training, inference, Kaggle submission, public/private score, reproduced baseline, adapters, credentials, or baseline code/data copy. Visible GPU is **not** training readiness.

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
| 2026-06-04 | M01 | Kaggle interactive debug probe | BQ-001 closed (5/day); probe SHA256 recorded; env-only (no submission.zip) |
| 2026-06-04 | M01 | Rules/team eligibility verified | BQ-003 closed; Submit UI accessible; team name not recorded |
| 2026-06-04 | M01 | Deadlines owner-reconfirmed | BQ-002 closed; entry Jun 8; final Jun 15 23:59 UTC |
| 2026-06-04 | M02 | M02 kickoff authorized | Local eval only; fixture holdout active-fixture; warn on extra preds |
| 2026-06-04 | M02 | M02 closed; PR #3 CI green | Local eval layer; fixture 0.75 not public score; audit 4.6/5 |
| 2026-06-04 | M02 | PR #3 squash-merged to `main` | `e78dc97`; post-merge CI 26973864069 green |
| 2026-06-04 | M03 | Solver factory on branch; PR #4 CI green | Structured solvers; writer owns boxing; 50 smoke examples; audit 4.7/5 |
| 2026-06-04 | M03 | M04 stub: control reproduction preflight | Defer full adapter sweep until baseline mapping |
| 2026-06-04 | M03 | PR #4 squash-merged to `main` | `fe2a7dd`; post-merge CI 26976448338 green |
| 2026-06-04 | M04 | Public control preflight on branch; PR #5 CI green | Mapping + candidate manifest; no baseline copy; audit 4.6/5 |
| 2026-06-04 | M04 | PR #5 squash-merged to `main` | `f54afd0`; post-merge CI 26979013700 green |
| 2026-06-04 | M05 | M05 kickoff authorized | Branch `forge/M05-control-repro-planning`; planning + reproduction plan contract |
| 2026-06-04 | M05 | Compute path locked | local_5090 preflight; Modal/Tinker future training (not authorized in M05) |
| 2026-06-04 | M05 | M05 closed on branch; PR #6 CI green | `7867e29`; reproduction plan contract; audit 4.6/5; merge pending |
| 2026-06-04 | M05 | M06 stub: execution gate | Per `M05_next_decision.md`; not started |
| 2026-06-04 | M05 | PR #6 squash-merged to `main` | `34169d0`; post-merge CI 26983281413 green |
| 2026-06-04 | M06 | M06 kickoff; Gate B schema inspection authorized | Branch `forge/M06-control-repro-execution-gate`; Gate C no |
| 2026-06-04 | M06 | External schema inspection complete | Baseline `82bd1880`; derived notes only; no raw data in repo |
| 2026-06-04 | M06 | M06 closed on branch; PR #7 CI green | `354f630`; audit 4.6/5; M07 training auth gate stub |
| 2026-06-04 | M06 | PR #7 squash-merged to `main` | `a7de356`; post-merge CI 26985969954 green; branch deleted |
| 2026-06-05 | M07 | M07 training auth gate on branch; PR #8 CI green | Path A blocked; manifest validates; audit 4.6/5 |
| 2026-06-05 | M07 | PR #8 squash-merged to `main` | `06ada17`; post-merge CI 26988100314 green; branch deleted |
| 2026-06-05 | M08 | M08 readiness closure on branch; PR #9 CI green | Readiness manifest; probe script not run; audit 4.6/5 |
| 2026-06-05 | M08 | PR #9 squash-merged to `main` | `ac7c5f2`; post-merge CI 26989604207 green; branch deleted |
| 2026-06-05 | M09 | M09 Modal/Tinker setup gate on branch; PR #10 CI green | `9be2687`; 166 tests; audit 4.6/5 |
| 2026-06-05 | M09 | PR #10 squash-merged to `main` | `5a4300b`; post-merge CI 26991673323 green; branch deleted |
| 2026-06-05 | M10 | M10 local 5090 probe on branch; PR #11 CI green | RTX 5090 visible; torch CPU-only; `visible_no_torch_cuda`; audit 4.6/5 |
| 2026-06-05 | M10 | PR #11 squash-merged to `main` | `dc45813`; post-merge CI 27032692673 green; branch deleted |
