# M06 Next Decision — M07 Recommendation

**Date:** 2026-06-04  
**Branch:** `forge/M06-control-repro-execution-gate`  
**Gate B:** `M06_SCHEMA_INSPECTION_AUTHORIZED = yes` — **complete**  
**Gate C:** `M06_TRAINING_AUTHORIZED = no`

---

## Summary of M06 findings

| Area | Finding |
| ---- | ------- |
| Schema inspection | **Complete** — corpus, problems, generation, train.csv derived notes |
| Baseline commit | `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85` |
| FORGE mapping | Core eval fields **mapped**; `corpus.segment` and boxed-in-corpus **partial/unknown** in samples |
| Reproduction manifest | `public_control_repro_plan_schema_gate_v1` validates; `schema_inspection_status: complete` |
| Training | **Not authorized** in M06 |
| Submit UI zip | **OPEN** — not guessed |
| Kaggle API | **TBD** |
| Compute/credentials | **TBD** — no training compute authorized |

---

## Blocker assessment for M07

| Blocker | Severity | Notes |
| ------- | -------- | ----- |
| No Gate C training authorization | **Gate** | Required before any SFT/inference |
| Modal/Tinker credentials | High | Owner setup |
| local_5090 CUDA probe | Medium | TBD — preflight only until evidenced |
| Submit UI zip OPEN | Medium | Blocks confident submit, not schema/training auth gate |
| `corpus.segment` structure | Medium | Partial mapping — may need M07 data-mapping work in parallel |
| No LICENSE observed | Low | Maintains `no_code_copy` |

---

## Recommended M07 direction

**Primary: Option 1 — Controlled Public Baseline Training Authorization Gate**

**Proposed title:** M07 — Controlled Public Baseline Training Authorization Gate

**Entry conditions (owner):**

1. `M06_TRAINING_AUTHORIZED = yes` (or equivalent manifest: `training_authorized: true` + `owner_training_authorization`).
2. `compute_path` selected (Modal/Tinker or approved alternative).
3. `credentials_ready: true` or documented waiver.
4. Training config captured per M05 template.

**M07 scope (draft — not started):**

1. Owner authorization record in reproduction plan manifest.
2. First authorized training attempt **or** explicit deferral with evidence.
3. Still: no false reproduction/submission claims without artifacts.

---

## Secondary paths (if owner overrides)

| Option | When to choose |
| ------ | -------------- |
| **2 — Baseline Corpus Schema Completion / Data Mapping** | If `corpus.segment` parsing blocks training config |
| **3 — Submission Package Preflight** | If Submit UI constraints become primary blocker |
| **4 — Local Eval/Holdout Hardening** | If reproduction risk too high before training |

---

## Parallel owner-actions

1. Record Submit UI `submission.zip` constraints when available.
2. Confirm Modal/Tinker credentials and budget.
3. Authorize training with explicit manifest fields before M07 execution.

---

## Explicit non-actions

M06 decision doc does **not** authorize:

- M07 implementation
- Model training, inference, or Kaggle submission
- Merge to `main`
