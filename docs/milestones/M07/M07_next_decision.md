# M07 Next Decision — M08 Recommendation

**Date:** 2026-06-05  
**Branch:** `forge/M07-training-authorization-gate`  
**Path:** A — `M07_TRAINING_AUTHORIZED = no`

---

## Summary of M07 findings

| Area | Finding |
| ---- | ------- |
| Training authorization (Gate C) | **Not provided** — `training_authorized: false` |
| Training-gate manifest | `public_control_repro_plan.training_blocked.json` validates |
| Schema inspection | **Complete** (M06) — carried forward |
| Schema mapping gaps | `corpus.segment` **partial** (SQ-CORPUS-001); `\boxed{}` not observed in M06 samples |
| Compute | local_5090 **available**; CUDA/VRAM **TBD** |
| Credentials | **false** / TBD — Modal, Tinker |
| Submit UI zip constraints | **OPEN** — owner-action |
| Training / inference / submission | **Not performed** |

---

## Blocker assessment for M08

| Blocker | Severity | Notes |
| ------- | -------- | ----- |
| No Gate C training authorization | **Gate** | Required before any SFT/inference |
| Credentials / cost | **High** | `credentials_ready` false |
| local_5090 CUDA probe | **Medium** | TBD |
| SQ-CORPUS-001 | **Medium** | May block confident training config |
| Submit UI OPEN | **Medium** | Blocks submission, not training auth docs |

---

## Recommended M08 direction

**Primary: Option 2 — Compute/Credential Readiness Closure**

**Proposed title:** M08 — Compute and Credential Readiness Closure (or equivalent slug)

**Rationale:** M07 produced a blocked training-gate record. The highest-leverage next step is evidenced compute/credential readiness (CUDA/VRAM probe when authorized, Modal/Tinker status, cost acceptance) so Gate C can be evaluated with facts—not guesses.

**M08 scope (draft — not started):**

1. Owner-supplied or authorized-probe CUDA/VRAM evidence for local_5090.
2. Credential readiness checklist closure (no secrets in repo).
3. Updated reproduction plan fields: `credentials_ready`, `compute_path` selection.
4. Still: no training/inference/submission without separate Gate C.

---

## Secondary paths

| Option | When to choose |
| ------ | -------------- |
| **1 — Controlled Public Baseline Training Attempt** | Owner supplies `M07/M08_TRAINING_AUTHORIZED = yes` + manifest fields + compute path |
| **3 — Corpus Segment Mapping Resolution** | If owner wants SQ-CORPUS-001 closed before any training authorization |
| **4 — Submission Package Constraint Preflight** | If Submit UI constraints become urgent before June 15 deadline |

---

## Parallel owner-actions

1. Record Submit UI `submission.zip` constraints when available.
2. Provide Gate C authorization string + compute path + `credentials_ready` + cost acceptance when ready for training.
3. Optional: authorize local_5090 environment probe (no training).

---

## Explicit non-actions

This decision doc does **not** authorize:

- M08 implementation without owner kickoff,
- model training, inference, or Kaggle submission,
- merge to `main`.

Seed M08 stub at M07 closeout per closeout prompt.
