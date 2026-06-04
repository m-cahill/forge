# M05_plan.md — Controlled Public Baseline Reproduction Planning

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M05 |
| **Title** | Controlled Public Baseline Reproduction Planning |
| **Branch** | `forge/M05-baseline-repro-plan` (planned) |
| **Status** | not started — stub seeded at M04 closeout |
| **Depends on** | M04 merged to `main` |
| **Authority** | [`docs/milestones/M04/M04_next_decision.md`](../M04/M04_next_decision.md) |

---

## 1. Objective (stub)

Plan the first **controlled** public baseline reproduction attempt for `tonghuikang/nemotron` without false reproduction claims:

- Decide compute path (local 5090, Kaggle GPU, Modal/Tinker, or hybrid)
- Define baseline data acquisition policy (no vendoring into FORGE without governance)
- Validate corpus/training example schema against a small external sample
- Capture training config hash requirements for real candidates
- Define first real control candidate run manifest requirements
- Optional: structural package dry-run from fixture zip only

**Out of scope until explicitly authorized:** full SFT training, Kaggle submission, public score claims, copying baseline implementation code.

---

## 2. Preconditions

- M04 merged; post-merge CI green
- Owner authorizes M05 kickoff
- Owner go/no-go for any training or large data download

---

## 3. Open blockers (carry-forward)

- Submit UI `submission.zip` constraints — **OPEN** (owner-action)
- Kaggle API submission — **TBD**
- Baseline LICENSE file — **not observed**

---

*Full plan to be expanded when M05 is authorized.*
