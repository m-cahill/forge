# M05 Next Decision — M06 Recommendation

**Date:** 2026-06-04  
**Branch:** `forge/M05-control-repro-planning`  
**Status:** M05 planning complete (pending closeout audit)

---

## Summary of M05 findings

| Area | Finding |
| ---- | ------- |
| Reproduction plan | `control_reproduction_plan.md` defines phased execution with explicit non-claims |
| Compute path | **local_5090** preflight; **Modal/Tinker** (or equivalent) for future baseline-compatible training |
| Acquisition | Clean-room policy — clone/read outside FORGE only with owner authorization |
| Schema | Inspection workflow + template ready; **no live extraction in M05** |
| Training config | Capture template ready; unused until training authorized |
| Manifest contract | `reproduction_plan.py` + CLI; mock preflight validates |
| Submit UI | Zip constraints **OPEN** — owner-action; not guessed |
| Kaggle API | **TBD** |
| Control candidate | **None**; mock reproduction plan only |

---

## Blocker assessment at M05 closeout

| Blocker | Severity for M06 | Notes |
| ------- | ---------------- | ----- |
| Corpus schema unknown | Medium | Address as **first sub-step** of M06 gate (authorized external inspect) |
| Submit UI zip OPEN | Medium | Does not block training planning; blocks confident submit |
| No training authorization | **Gate** | Owner must authorize before M06 execution |
| Modal/Tinker credentials | Medium | Owner setup before full training |
| No LICENSE observed | Low for execution | Maintains `no_code_copy`; external reference only |

**Conclusion:** Compute path, acquisition policy, and manifest requirements are **clear enough** to recommend M06 as a controlled execution gate, with schema inspection as the opening authorized sub-step—not a separate milestone unless owner prefers isolation.

---

## Recommended M06 direction

**Primary recommendation: Option 1 — Controlled Public Baseline Reproduction Execution Gate**

**Proposed title:** M06 — Controlled Public Baseline Reproduction Execution Gate

**Entry conditions (owner):**

1. Explicit training authorization (`training_authorized` + `owner_training_authorization` in reproduction plan manifest).
2. Compute path selected (Modal/Tinker or approved alternative).
3. Credentials and cost acceptance recorded.

**M06 scope (draft, not started):**

1. Authorized external schema inspection (per `corpus_schema_inspection_plan.md`) — derived notes only.
2. Training config capture from observed baseline commands (reference only until run).
3. First authorized training attempt OR explicit deferral with evidence if blocked.
4. Still: no false reproduction/submission claims without artifacts.

---

## Secondary paths (if owner overrides at kickoff)

| Option | When to choose |
| ------ | -------------- |
| **2 — Baseline Corpus Schema Inspection** | If owner wants schema-only milestone with **no** training discussion on M06 |
| **3 — Submission Package Preflight** | If Submit UI constraints become primary blocker before any training |
| **4 — Holdout Activation / Local Eval Hardening** | If reproduction risk is deemed too high until holdouts and eval gates harden |

---

## Parallel owner-actions

1. Record Submit UI `submission.zip` constraints when inspecting Kaggle Submit page.
2. Confirm Modal/Tinker (or cloud GPU) credentials and budget.
3. Authorize M06 kickoff and training with explicit manifest fields.

---

## Explicit non-actions

M05 decision doc does **not** authorize:

- M06 implementation without owner kickoff
- Model training or inference in M05
- Kaggle submission
- Merge to `main`

---

## M06 seed

Seed `docs/milestones/M06/M06_plan.md` at M05 closeout per workflow (stub pointing to this recommendation).
