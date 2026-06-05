# M11_plan.md — Credential and Cost Closure Continuation

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M11 |
| **Title** | Credential and Cost Closure Continuation |
| **Branch** | `forge/M11-credential-cost-closure` (planned) |
| **Status** | not started — stub seeded at M10 closeout |
| **Authority** | [`docs/milestones/M10/M10_next_decision.md`](../M10/M10_next_decision.md) |

---

## 1. Objective (stub)

Continue closing owner-evidenced gaps for Modal/Tinker/cloud GPU credential readiness and cost acceptance so Gate C training authorization can be evaluated — **without** storing secrets in the repo and **without** training unless separately authorized.

**Context from M10:** Local RTX 5090 is visible (~32 GB VRAM, driver 591.86) but PyTorch is CPU-only (`visible_no_torch_cuda`). External credential/cost closure is the primary M11 path per probe-result-driven decision.

**Out of scope until authorized:** model training, inference, Kaggle submission, full baseline reproduction.

---

## 2. Expected owner inputs

- Modal account/credential status (TBD → ready/blocked) — statement only
- Tinker account/credential status (TBD → ready/blocked) — statement only
- Cloud GPU status (TBD → ready/blocked) — statement only
- Cost acceptance for paid paths (TBD → yes/no with limits)
- Optional: local CUDA PyTorch install authorization for secondary local path
- Optional: Submit UI `submission.zip` constraint evidence

---

## 3. Secondary options (if owner redirects)

| Option | When |
| ------ | ---- |
| M11 — Local CUDA Stack Fix + Training Feasibility Dry Run | Owner prefers local path despite M10 primary recommendation |
| M11 — Submission Package Constraint Preflight | Submit UI becomes deadline-critical |
| M11 — Corpus Segment Mapping Resolution | SQ-CORPUS-001 must close before training auth |

---

*Full plan to be expanded when M11 is authorized.*
