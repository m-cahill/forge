# M05_plan.md — Controlled Public Baseline Reproduction Planning and Compute Path

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M05 |
| **Title** | Controlled Public Baseline Reproduction Planning and Compute Path |
| **Branch** | `forge/M05-control-repro-planning` |
| **Status** | closed (PR #6 green; merge pending owner permission) |
| **Precondition** | M04 merged to `main`; post-merge CI green; owner authorized M05 kickoff |
| **Primary goal** | Executable, auditable plan for a future public control reproduction attempt — **no training, inference, Kaggle submission, or reproduction claims** |

---

## 1. Objective

M05 prepares FORGE for the first real public control reproduction attempt by deciding the compute path, artifact requirements, data acquisition rules, manifest contracts, and dry-run evidence requirements.

M05 does **not** execute reproduction. It produces the plan and validation scaffolding required before a future milestone may safely train, package, evaluate, or submit a control candidate.

By the end of M05, FORGE should have:

1. A controlled public baseline reproduction plan.
2. A compute-path decision matrix and recommended path.
3. A baseline data/corpus acquisition policy.
4. A baseline corpus schema inspection plan.
5. A training configuration capture template.
6. A control candidate artifact/run directory contract (via reproduction-plan manifest).
7. A validated reproduction-plan manifest.
8. A mock control-reproduction dry-run manifest (preflight-only).
9. A go/no-go checklist for the future actual reproduction milestone.
10. Green CI and updated `docs/forge.md`.

---

## 2. Current state

M00–M04 merged to `main` (`f54afd0`).

**Capabilities:** `forge_nemotron` package with CI; boxed-answer metric; structural `submission.zip` validator; local eval CLI and run manifests; solver-verified synthetic trace factory; candidate manifest contract and promotion preflight gates; public control preflight dossier and baseline mapping; mock preflight candidate manifest.

**Known facts:**

- Daily submissions: 5/day (0/5 used).
- Rules/team joined: yes.
- Entry deadline: June 8, 2026.
- Final deadline: June 15, 2026 23:59 UTC.
- No Kaggle submission; no public/private score; no training or inference; no reproduced baseline.
- Submit UI `submission.zip` constraints: **OPEN** (owner-action).
- Kaggle API submission: **TBD**.

M04 confirmed `tonghuikang/nemotron` has no observed root license file, large public artifacts, `uv`, Modal, Tinker, and 30B compute dependencies; FORGE posture remains clean-room/external-reference mapping only.

---

## 3. Hard constraints

| Constraint | Rule |
| ---------- | ---- |
| No training | No SFT, QLoRA, Tinker, Modal training, local 5090 training, or Kaggle GPU training |
| No inference | No Nemotron inference |
| No Kaggle submission | No upload, commit, or submit |
| No reproduction claim | Plan only; no score/LB/adapter parity claims |
| No code copying | No copy/vendor/submodule of `tonghuikang/nemotron` |
| No large artifacts | No corpus, tokenizer, checkpoints, zips, or model files in repo |
| Evidence over assumptions | Unknowns remain unknown |

---

## 4. Locked decisions (owner 2026-06-04)

| Topic | Decision |
| ----- | -------- |
| Branch | `forge/M05-control-repro-planning` |
| Compute — preflight | **local_5090** primary for dry-run, env checks, small packaging/eval tests |
| Compute — training (future) | **Modal/Tinker** or equivalent external GPU; requires owner authorization |
| Kaggle notebook | Evidence/submit workflow; not primary training unless GPU confirmed |
| Submit UI zip | **OPEN** — preserve blocker; do not guess |
| Schema inspection | Cursor-executable workflow for **future** milestone; owner auth before clone/download; no extraction in M05 |
| M06 direction | Choose at closeout in `M05_next_decision.md` |

---

## 5. Deliverables

| ID | Deliverable | Path |
| -- | ----------- | ---- |
| 5.1 | Controlled reproduction plan | `docs/milestones/M05/control_reproduction_plan.md` |
| 5.2 | Compute-path decision matrix | `docs/milestones/M05/compute_path_decision.md` |
| 5.3 | Baseline acquisition policy | `docs/milestones/M05/baseline_acquisition_policy.md` |
| 5.4 | Corpus schema inspection plan | `docs/milestones/M05/corpus_schema_inspection_plan.md` |
| 5.5 | External schema notes template | `docs/milestones/M05/external_schema_notes_template.md` |
| 5.6 | Training config capture template | `docs/milestones/M05/training_config_capture_template.md` |
| 5.7 | Reproduction plan manifest contract | `src/forge_nemotron/baselines/reproduction_plan.py` |
| 5.8 | Validation CLI | `scripts/validate_reproduction_plan.py` |
| 5.9 | Mock reproduction plan evidence | `docs/milestones/M05/evidence/reproduction_plan/` |
| 5.10 | M05 next decision | `docs/milestones/M05/M05_next_decision.md` |
| 5.11 | Governance updates | `docs/forge.md`, `README.md`, `scripts/README.md` |

---

## 6. Implementation phases

### Phase A — Branch and plan setup

- Confirm clean `main`; create `forge/M05-control-repro-planning`
- Expand `M05_plan.md`, `M05_toolcalls.md`
- Mark M05 active in `docs/forge.md` and README
- Commit: `docs(milestones): expand M05 control reproduction planning`

### Phase B — Planning documents

- Create §5.1–5.6 planning docs
- Commit: `docs(baseline): define controlled reproduction planning`

### Phase C — Reproduction plan manifest contract

- Add `baselines/reproduction_plan.py` + unit tests
- Commit: `feat(baselines): add reproduction plan manifest contract`

### Phase D — Validation CLI and mock evidence

- Add `validate_reproduction_plan.py`, mock JSON, evidence README
- Commit: `docs(baselines): add reproduction plan preflight evidence`

### Phase E — Next decision and governance updates

- Create `M05_next_decision.md`; finalize `docs/forge.md`
- Commit: `docs(governance): record M05 next decision`

---

## 7. Acceptance criteria

- [x] Branch `forge/M05-control-repro-planning` from green `main`
- [x] All §5 deliverables exist
- [x] Reproduction plan validator tests pass
- [x] CLI validates mock plan; exits nonzero on invalid (unit tests)
- [x] Mock evidence labeled preflight-only
- [x] Submit UI constraints recorded as OPEN or explicitly deferred
- [x] CI green on PR — [26982564940](https://github.com/m-cahill/forge/actions/runs/26982564940)
- [x] No training, inference, submission, reproduction, or score claims
- [x] No baseline code/data copied into FORGE
- [x] No real adapter/package created

---

## 8. Closeout (after implementation)

Use closeout prompt in project workflow: summary, audit, run1, PR instructions, seed M06 stub — **only with owner permission** for merge/closeout.

---

## 9. Final non-claims

M05 must preserve:

- no Kaggle submission, public score, private score
- no model training or inference
- no reproduced public baseline
- no Kaggle-ready adapter or real adapter package
- no copied/vendored public baseline code or data
- no training authorization
