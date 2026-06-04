# Milestone Summary — M06: Controlled Public Baseline Reproduction Execution Gate

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — public control reproduction (execution gate)  
**Milestone:** M06 — Controlled Public Baseline Reproduction Execution Gate  
**Timeframe:** 2026-06-04  
**Status:** Closed — PR [#7](https://github.com/m-cahill/forge/pull/7) **merged** to `main` (`a7de356`) 2026-06-04T23:33:42Z  
**Branch:** `forge/M06-control-repro-execution-gate` (deleted after merge)  
**PR head at merge:** `354f630`  
**PR CI:** [26985581070](https://github.com/m-cahill/forge/actions/runs/26985581070) **green**  
**Post-merge CI:** [26985969954](https://github.com/m-cahill/forge/actions/runs/26985969954) **green**  
**Baseline:** M05 merged `34169d0`

---

## 1. Milestone Objective

Convert M05 planning into an execution gate: authorized external schema inspection (derived notes only), schema-gate reproduction manifest, compute/credential checklists, and M07 go/no-go — **without** training, inference, submission, or reproduction claims.

---

## 2. Scope Definition

### In Scope

- Gate B schema inspection of `tonghuikang/nemotron` @ `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85`
- Derived schema notes (corpus, problems, generation, train.csv) + mapping supplement
- Execution gate doc + compute/credential checklists
- `public_control_repro_plan.schema_gate.json` + reproduction plan validator extensions
- M06 next decision; M07 stub seeded

### Out of Scope

- Model training, inference, Kaggle submission, public/private score
- Baseline reproduction, real adapter package, vendored baseline code/data
- Gate C training (`M06_TRAINING_AUTHORIZED = no`)
- Merge to `main` (requires express permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Schema (Gate B) | Read-only clone `C:\coding\nemotron-inspect`; hashes, row counts, keys; no raw rows committed |
| Docs | Execution gate, 4 schema notes, mapping supplement, checklists, next decision |
| Code | `schema_inspection_status`, structured `data_sources`, ready-for-training gates |
| Evidence | Schema-gate manifest validates |
| Governance | `docs/forge.md`, README, M06 plan/toolcalls; M07 stub |

**Commit:** `895a3cb`

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **151** tests (+4) |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | Schema-gate manifest |
| PR CI #7 | **Green** | [26985544150](https://github.com/m-cahill/forge/actions/runs/26985544150) |
| Training / submission / reproduction | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M06 delta.
- Test count 147 → 151; schema-gate manifest file tested in unit suite.
- External clone not in repo; inspection outside FORGE tree only.

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | **OPEN** | Owner-action; not guessed |
| Kaggle API submission | **TBD** | Preserved |
| `\boxed{}` in inspected baseline samples | **not observed** in first 50–100 rows per file | Open for M07 |
| `corpus.segment` structure | **partial** | SQ-CORPUS-001 |
| validate_reproduction_plan CLI not in CI | Accepted | Unit tests cover rules |

No HIGH defects blocking M06 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M07 training authorization gate | M07 (per `M06_next_decision.md`) |
| Submit UI zip constraints | Owner parallel |
| local_5090 CUDA probe | Owner / M07 preflight |
| Modal/Tinker credentials | Owner before training |

---

## 8. Governance Outcomes

- `schema_inspection_status: complete` with four data sources in schema-gate manifest.
- Training **not** authorized; `training_authorized: false`.
- M07 recommended: Controlled Public Baseline Training Authorization Gate.

---

## 9. Schema-Gate Disclaimer (required)

`public_control_repro_plan.schema_gate.json` is **execution-gate evidence only**. It is **not** training authorization, baseline reproduction, adapter/package evidence, or Kaggle-ready submission.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M06 deliverables | Yes |
| PR CI green | Yes — 26985544150 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| No raw baseline data in repo | Yes |
| Merge to `main` | Yes — `a7de356` (2026-06-04T23:33:42Z) |

**Next recommendation:** Owner authorizes M07 Gate C when ready; record Submit UI zip constraints when available.
