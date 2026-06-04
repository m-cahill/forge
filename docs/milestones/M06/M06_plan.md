# M06_plan.md — Controlled Public Baseline Reproduction Execution Gate

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M06 |
| **Title** | Controlled Public Baseline Reproduction Execution Gate |
| **Branch** | `forge/M06-control-repro-execution` (planned) |
| **Status** | not started — stub seeded at M05 closeout |
| **Depends on** | M05 merged to `main`; owner authorizes M06 kickoff and training |
| **Authority** | [`docs/milestones/M05/M05_next_decision.md`](../M05/M05_next_decision.md) |

---

## 1. Objective (stub)

Execute the first **authorized** steps toward public control reproduction under M05 planning guardrails:

1. Authorized external corpus schema inspection (derived notes only; no large commits).
2. Training config capture from observed baseline (reference until FORGE run).
3. First authorized training attempt **or** explicit deferral with evidence if blocked.

**Out of scope until explicitly authorized:** false reproduction claims, Kaggle submission without validated package, vendoring baseline code/data.

---

## 2. Preconditions

- M05 merged; post-merge CI green
- Owner `training_authorized` + `owner_training_authorization` in reproduction plan manifest
- Compute path and credentials confirmed (Modal/Tinker or approved alternative)
- Submit UI zip constraints recorded (owner-action; parallel if still OPEN)

---

## 3. Open blockers (carry-forward)

- Submit UI `submission.zip` constraints — **OPEN** (owner-action)
- Kaggle API submission — **TBD**
- Baseline LICENSE — **not observed**; `no_code_copy` posture
- No real control candidate yet

---

*Full plan to be expanded when M06 is authorized.*
