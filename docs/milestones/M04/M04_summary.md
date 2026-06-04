# 📌 Milestone Summary — M04: Public Control Adapter Reproduction Preflight

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — public control reproduction (preflight only)  
**Milestone:** M04 — Public Control Adapter Reproduction Preflight  
**Timeframe:** 2026-06-04  
**Status:** Closed — PR [#5](https://github.com/m-cahill/forge/pull/5) open; CI green on head `26861ff`  
**Branch:** `forge/M04-control-preflight`  
**PR head:** `26861ffbbb526ad313bdd299e26c1de1b7d5d7e8`  
**PR CI:** [26977971068](https://github.com/m-cahill/forge/actions/runs/26977971068) **green**  
**Baseline:** M03 merged `fe2a7dd`

---

## 1. Milestone Objective

Map the public Progress Prize baseline (`tonghuikang/nemotron`) into FORGE contracts and define what evidence a real control adapter candidate must carry **before** any training or Kaggle submission — without claiming reproduction.

Without M04, FORGE would risk ad-hoc adapter promotion without documented baseline blockers, manifest discipline, or M05 direction.

---

## 2. Scope Definition

### In Scope

- Public control preflight dossier and baseline format mapping (M01 + read-only GitHub re-inspection)
- `adapters/candidate_manifest.py` with full status enum and validation rules
- Mock preflight manifest evidence + `validate_candidate_manifest.py`
- Promotion preflight gates and `M04_next_decision.md`
- 11 unit tests; governance updates (`docs/forge.md`, README, kaggle evidence)

### Out of Scope

- Model training, inference, Kaggle submission, public/private score
- Baseline reproduction claim, real adapter package, vendored baseline code/data
- JSON Schema, manifest diff helper (stretch deferred)
- M05 implementation

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Docs | `public_control_preflight.md`, `baseline_format_mapping.md`, gates, next decision |
| Code | Candidate manifest builder/validator; CLI script |
| Evidence | `control_candidate_manifest.preflight.json` + README |
| Governance | M04 plan, toolcalls, forge.md active record → closeout |

**Commits:** `c33e627`, `b1fd36a`, `dea0f6f`, `ace83b1`, `26861ff`

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **138** tests |
| `compileall src` | Pass | |
| `validate_candidate_manifest.py` | Pass | Mock preflight manifest |
| PR CI #5 | **Green** | Run 26977971068 |
| Kaggle / training / reproduction | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M04 delta.
- Test count 127 → 138 without gate weakening.
- Candidate manifest CLI not in CI (local verification only).

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | **OPEN** | Owner-action; preserved in kaggle evidence |
| Kaggle API submission | **TBD** | Gates doc |
| Mock manifest vs real adapter | Mitigated | Evidence README + non_claims |
| `validate_candidate_manifest` not in CI | Accepted | Unit tests cover validator |

No HIGH defects blocking M04 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M05 controlled baseline reproduction planning | M05 (per `M04_next_decision.md`) |
| Submit UI zip constraints recording | Owner parallel |
| CI job for candidate manifest CLI | M05+ optional |
| JSON Schema / manifest diff | Stretch deferred |

---

## 8. Governance Outcomes

- Baseline workflow and FORGE mapping documented with explicit unknowns.
- Candidate manifest contract enforces rank ≤32, base model, and status-specific hash rules.
- Mock `control_public_repro_preflight` validates; **not** on Adapter Candidate Board as a real candidate.
- M05 stub: Controlled Public Baseline Reproduction Planning.

---

## 9. Mock Preflight Disclaimer (required)

`control_candidate_manifest.preflight.json` is **schema/gate evidence only**. It is **not** an adapter, `submission.zip`, Kaggle-ready candidate, or reproduction evidence.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M04 deliverables 4.1–4.9 | Yes |
| PR CI green | Yes — 26977971068 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| Merge to `main` | **Pending owner permission** |

**Next recommendation:** Merge PR #5 with permission; owner records Submit UI zip constraints; authorize M05 planning kickoff (no training without explicit go-ahead).
