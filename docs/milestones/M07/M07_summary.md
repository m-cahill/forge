# Milestone Summary — M07: Controlled Public Baseline Training Authorization Gate

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane A — public control reproduction (training authorization gate)  
**Milestone:** M07 — Controlled Public Baseline Training Authorization Gate  
**Timeframe:** 2026-06-05  
**Status:** Closed — PR [#8](https://github.com/m-cahill/forge/pull/8) **merged** to `main` (`06ada17`) 2026-06-05T00:35:34Z  
**Branch:** `forge/M07-training-authorization-gate` (deleted after merge)  
**PR head at merge:** `90cdab7`  
**PR CI:** [26986758980](https://github.com/m-cahill/forge/actions/runs/26986758980) **green**  
**Post-merge CI:** [26988100314](https://github.com/m-cahill/forge/actions/runs/26988100314) **green**  
**Baseline:** M06 merged `a7de356`

---

## 1. Milestone Objective

Formal gate before any controlled public baseline training: evaluate schema readiness, compute/credentials, Submit UI constraints, and owner Gate C authorization; produce blocked training-gate manifest and future-only dry-run plan — **without** training, inference, submission, or reproduction claims.

---

## 2. Scope Definition

### In Scope

- Training authorization gate + schema/compute/submit UI gate docs
- `public_control_repro_plan.training_blocked.json` + evidence README
- Reproduction plan tests (+3) for ready-for-training and training-blocked file
- Training config draft (not executed) + dry-run command plan (future only)
- `M07_next_decision.md` → M08 compute/credential closure recommendation
- Governance updates (`docs/forge.md`, README, M07 plan/toolcalls)

### Out of Scope

- Model training, inference, Kaggle submission, public/private score
- Baseline reproduction, real adapter package, vendored baseline code/data
- Gate C training (`M07_TRAINING_AUTHORIZED = no`)
- New external schema inspection (uses M06 derived notes)
- Merge to `main` (requires express permission)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Gate docs | Authorization, schema readiness, compute/credential, Submit UI gates |
| Evidence | Training-blocked manifest; validates |
| Code | +3 unit tests in `test_reproduction_plan.py` |
| Planning | Training config draft, dry-run command plan (not executed) |
| Governance | `docs/forge.md`, README, M07 plan; M08 stub seeded |

**Commits (implementation):** `42816f8` → `410638a` (+ `ce1d258` toolcalls pre-PR)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **154** tests (+3) |
| `compileall src` | Pass | |
| `validate_reproduction_plan.py` | Pass | training_blocked manifest |
| PR CI #8 | **Green** | [26986703969](https://github.com/m-cahill/forge/actions/runs/26986703969) |
| Training / submission / reproduction | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M07 delta.
- Test count 151 → 154; training-blocked manifest file tested in unit suite.
- No baseline data, adapters, or credentials in repo.

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | **OPEN** | Owner-action; not guessed |
| Kaggle API submission | **TBD** | Preserved |
| Modal/Tinker credentials | **TBD** | `credentials_ready: false` |
| local_5090 CUDA/VRAM | **TBD** | Not probed in M07 |
| SQ-CORPUS-001 (`corpus.segment`) | **open** | Partial mapping documented |
| `\boxed{}` in M06 samples | **not observed** | Unknown for full corpus |
| validate_reproduction_plan CLI not in CI | Accepted | Unit tests cover rules |

No HIGH defects blocking M07 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M08 compute/credential readiness closure | M08 (per `M07_next_decision.md`) |
| Gate C training authorization | Owner — future milestone |
| Submit UI zip constraints | Owner parallel |
| Controlled baseline training attempt | After Gate C + readiness |

---

## 8. Governance Outcomes

- `M07_TRAINING_AUTHORIZED = no`; manifest `training_authorized: false`, `ready_for_training: false`.
- Training go/no-go: **NO-GO**; gate documentation: **GO**.
- M08 recommended: Compute/Credential Readiness Closure.

---

## 9. Training-Gate Disclaimer (required)

`public_control_repro_plan.training_blocked.json` is **training-gate evidence only**. It is **not** training authorization, baseline reproduction, adapter/package evidence, or Kaggle-ready submission. `training_config_draft.md` and `dry_run_command_plan.md` are **draft/future-only** — not executed configs or commands.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M07 deliverables | Yes |
| PR CI green | Yes — 26986703969 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| No raw baseline data in repo | Yes |
| Merge to `main` | Yes — `06ada17` (2026-06-05T00:35:34Z) |

**Next recommendation:** Kick off M08 compute/credential closure when authorized; owner records Submit UI constraints and Gate C when ready for training.
