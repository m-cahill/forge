# M06_plan.md — Controlled Public Baseline Reproduction Execution Gate

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M06 |
| **Title** | Controlled Public Baseline Reproduction Execution Gate |
| **Branch** | `forge/M06-control-repro-execution-gate` |
| **Status** | closed — PR [#7](https://github.com/m-cahill/forge/pull/7); merge pending |
| **Precondition** | M05 merged to `main`; post-merge CI green; owner authorized M06 kickoff |
| **Gate B** | `M06_SCHEMA_INSPECTION_AUTHORIZED = yes` |
| **Gate C** | `M06_TRAINING_AUTHORIZED = no` |

---

## 1. Objective

M06 converts M05 planning artifacts into an execution gate: external schema inspection, reproduction manifest upgrade, compute/credential checklists, and go/no-go for future training — **without** training, inference, or Kaggle submission unless Gate C is separately authorized.

---

## 2. Authorization model

| Gate | Authorizes | M06 |
| ---- | ---------- | --- |
| A | Branch, docs, validation | yes |
| B | External schema inspection (derived notes only) | yes |
| C | Training/inference/submission.zip | **no** |

---

## 3. Deliverables

| # | Deliverable | Path |
| - | ----------- | ---- |
| 7.1 | Execution gate doc | `control_reproduction_execution_gate.md` |
| 7.2 | External schema notes | `external_schema_notes_*.md` |
| 7.3 | Mapping supplement | `baseline_schema_mapping_supplement.md` |
| 7.4 | Schema-gate manifest | `evidence/reproduction_gate/public_control_repro_plan.schema_gate.json` |
| 7.5 | Contract updates | `reproduction_plan.py`, `test_reproduction_plan.py` |
| 7.6 | Compute checklist | `compute_readiness_checklist.md` |
| 7.7 | Credential checklist | `credential_readiness_checklist.md` |
| 7.9 | Next decision | `M06_next_decision.md` |
| 7.10 | Governance | `docs/forge.md`, `README.md`, `M06_toolcalls.md` |

---

## 4. Acceptance criteria

- [x] Branch `forge/M06-control-repro-execution-gate` from green `main`
- [x] Execution gate doc + checklists exist
- [x] Schema inspection complete with derived notes (Gate B)
- [x] Mapping supplement exists
- [x] Schema-gate manifest validates
- [x] Tests pass; CI green on PR — [26985544150](https://github.com/m-cahill/forge/actions/runs/26985544150)
- [x] No raw baseline data/code/credentials committed
- [x] No training, inference, submission, reproduction claims
- [x] Submit UI constraints OPEN (not guessed)
- [x] M06 summary, audit, run1 at closeout
- [x] M07 stub seeded per next decision

---

## 5. Non-claims (preserved)

No Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, committed credentials, or raw baseline data in repo.

---

## 6. Closeout

Use closeout prompt in M06 handoff when PR CI is green. Do not merge without express permission.
