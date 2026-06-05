# M10_plan.md — Credential and Cost Closure Continuation

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M10 |
| **Title** | Credential and Cost Closure Continuation |
| **Branch** | `forge/M10-credential-cost-closure` (planned) |
| **Status** | not started — stub seeded at M09 closeout |
| **Authority** | [`docs/milestones/M09/M09_next_decision.md`](../M09/M09_next_decision.md) |

---

## 1. Objective (stub)

Continue closing owner-evidenced gaps for Modal/Tinker/cloud GPU credential readiness and cost acceptance so Gate C training authorization can be evaluated — **without** storing secrets in the repo and **without** training unless separately authorized.

**Out of scope until authorized:** model training, inference, Kaggle submission, local 5090 probe execution (unless owner authorizes), baseline reproduction claims.

---

## 2. Expected owner inputs

- Modal account/credential status (TBD → ready/blocked) — statement only
- Tinker account/credential status (TBD → ready/blocked) — statement only
- Cloud GPU status (TBD → ready/blocked) — statement only
- Cost acceptance for paid paths (TBD → yes/no with limits)
- Optional: `M10_LOCAL_5090_PROBE_AUTHORIZED = yes` for probe only
- Optional: Submit UI `submission.zip` constraint evidence

---

## 3. Secondary options (if owner redirects)

| Option | When |
| ------ | ---- |
| M10 — Local 5090 Feasibility Probe | CUDA/VRAM evidence needed before external spend |
| M10 — Submission Package Constraint Preflight | Submit UI becomes deadline-critical |
| M10 — Corpus Segment Mapping Resolution | SQ-CORPUS-001 must close before training auth |

---

*Full plan to be expanded when M10 is authorized.*
