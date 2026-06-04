# M04 Next Decision — M05 Recommendation

**Date:** 2026-06-04  
**Branch:** `forge/M04-control-preflight`  
**Status:** Preflight complete (pending M04 closeout audit)

---

## Summary of M04 findings

| Area | Finding |
| ---- | ------- |
| Baseline workflow | Documented end-to-end pipeline (`reasoning` → `augmentation` → `corpus` → `train_sft` → Modal upload) |
| FORGE mapping | Metric, eval, manifests, packaging validator, candidate manifest — **mapped**; corpus schema and training path — **partial/unknown** |
| License | No LICENSE file observed; **no code copied** |
| Compute | Modal, Tinker, `uv`, GPU for 30B — blockers for naive reproduction |
| Submit UI | Zip constraints **OPEN**; not blocking M04 preflight |
| Control candidate | **None**; mock manifest only |

---

## Recommended M05 direction

**Primary recommendation: Option 1 — Controlled public baseline reproduction attempt (planning + minimal dry-run only if explicitly authorized)**

Rationale:

1. Lane A (public control) remains mandatory per `FORGE_ANCHOR.md`.
2. M04 mapped contracts; next step is a **bounded** reproduction plan: compute path decision, corpus format validation sample, training config capture — still **no false reproduction claim**.
3. Submit UI constraints can proceed in parallel as owner-action without blocking planning.

**Secondary (parallel owner-action):** Record Submit UI `submission.zip` constraints when available.

**Defer unless blockers worsen:**

- Option 3 — Strengthen local eval / holdout gates (if corpus mapping fails in M05 planning)
- Option 2 — Kaggle packaging preflight-only milestone (if Submit UI remains unknown at reproduction kickoff)
- Option 4 — Small training dry-run (only with explicit owner authorization)

---

## M05 seed title (stub)

**M05 — Public control reproduction planning and compute path** (exact slug TBD at closeout)

Deliverables (draft):

- Corpus format validation against a small external sample (not committed to repo if large)
- Training config hash capture plan
- Compute environment decision (5090 / Kaggle GPU / Modal)
- Optional: first structural package dry-run from fixture zip only
- Still: no score claims without evidence

---

## Explicit non-actions

M04 decision doc does **not** authorize:

- M05 implementation start without owner kickoff
- Model training or inference
- Kaggle submission
- Merge to `main`

---

## Owner actions

1. Record Submit UI zip constraints when inspecting Kaggle Submit page.
2. Confirm compute budget/path for baseline reproduction.
3. Authorize M05 kickoff after M04 PR merge and green CI.
