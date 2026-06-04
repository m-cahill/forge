# M02_plan.md — Exact Local Evaluation and Artifact Discipline

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M02 |
| **Title** | Exact local evaluation and artifact discipline |
| **Branch** | `forge/M02-local-eval` (planned) |
| **Status** | not started — stub seeded at M01 closeout |
| **Depends on** | M01 merged to `main` |

---

## 1. Objective (stub)

Make every adapter candidate comparable before spending Kaggle submissions: local eval CLI, per-category reporting, run manifest schema, artifact hashing, and golden metric alignment where competition samples are available.

---

## 2. Planned deliverables (from FORGE_ANCHOR §14)

- Local eval CLI under `src/forge_nemotron/eval/`
- Per-category score reports
- Fixed holdout activation (register entries in `docs/forge.md`)
- `run_manifest.json` contract implementation
- Golden tests for boxed metric vs competition examples (if available)
- CI smoke path extension (optional)

---

## 3. Out of scope (initial)

- Kaggle submission
- Full baseline reproduction
- Solver factory (M03)

---

## 4. Preconditions

- M01 merged to `main`
- BQ-001 / BQ-003 remain owner-action until resolved (do not block M02 local work, but block Kaggle submit)

---

*Full plan to be expanded when M02 is authorized.*
