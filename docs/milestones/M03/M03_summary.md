# 📌 Milestone Summary — M03: Solver and Synthetic Trace Factory

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Lane B — solver-guided synthetic data (factory proof)  
**Milestone:** M03 — Solver and Synthetic Trace Factory  
**Timeframe:** 2026-06-04  
**Status:** Closed — PR [#4](https://github.com/m-cahill/forge/pull/4) **merged** to `main` (`fe2a7dd`)  
**Branch:** `forge/M03-solver-factory` (merged)  
**PR head (pre-merge):** `ac661166a4c3b1be63df7a6aaa0d905208baaa79`  
**Squash merge on `main`:** `fe2a7dd2e38f158503a49bb81d9ff4a3573601e6`  
**Post-merge CI:** [26976448338](https://github.com/m-cahill/forge/actions/runs/26976448338) **green**  
**Baseline:** M02 merged `e78dc97`

---

## 1. Milestone Objective

Prove the end-to-end verified synthetic trace factory:

```text
solver → generator → verifier → JSONL → manifest + hash → local eval → evidence
```

Without M03, FORGE could not produce deterministic, solver-verified training-style traces aligned with the `\boxed{}` metric — blocking Lane B data work and future adapter sweeps.

---

## 2. Scope Definition

### In Scope

- `src/forge_nemotron/solvers/` — base protocol, arithmetic, string transform (3 types)
- `src/forge_nemotron/generators/` — arithmetic, string, formatting_stress
- `src/forge_nemotron/data/` — synthetic writer, dataset manifest
- `scripts/make_dataset.py`
- Eval split `synthetic_smoke` on `EvaluationExample`
- Committed evidence `docs/milestones/M03/evidence/synthetic_smoke/` (50 examples)
- Unit tests (+21), governance docs, M03 plan/run1/summary/audit

### Out of Scope

- Kaggle submission, public/private score, training, inference, baseline reproduction
- Hypothesis dependency
- Extra string transforms (case, extended ciphers) — deferred
- Large-scale generation, production holdout activation

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Solvers | Structured arithmetic (no eval); string reverse/rotate/substitution |
| Generators | Deterministic seeded batches; writer owns final `\boxed{}` |
| Data | Reject unverified, duplicate IDs; manifest with SHA256 |
| CLI | `make_dataset.py` with optional eval JSONL outputs |
| Evidence | 50-example smoke; factory self-check 50/50 |
| Governance | Dataset + Run Ledger rows; M04 stub seeded |

**Commits:** `e6de36f`, `ef8e758`, `1c7dde2`

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | |
| `mypy src tests` | Pass | |
| `pytest -q` | Pass | **127** tests |
| `compileall src` | Pass | |
| PR CI #4 | **Green** | Run 26975703019 |
| `make_dataset.py` smoke | Pass | seed 123, 50 examples |
| Synthetic factory self-check | Pass | **1.0** (50/50) — not model/LB score |
| Kaggle / training / reproduction | **Not claimed** | |

---

## 5. CI / Automation Impact

- No workflow file changes; existing CI certifies M03 delta.
- Test count 106 → 127 without gate weakening.
- Dataset/eval CLI smokes remain local + committed evidence (not CI jobs).

---

## 6. Issues & Exceptions

| Issue | Status | Reference |
| ----- | ------ | --------- |
| Submit UI zip constraints | Open | Owner-action |
| Factory self-check vs model score | Mitigated | Evidence README + Run Ledger label |
| `make_dataset` not in CI | Accepted | Unit tests + committed evidence |

No HIGH defects blocking M03 closeout.

---

## 7. Deferred Work

| Item | Target |
| ---- | ------ |
| M04 public control reproduction preflight | M04 |
| CI job for dataset/eval CLI smoke | M04+ optional |
| Extra string transform types | M04+ if needed |
| Contamination check vs holdout IDs | Stretch / M04 |

---

## 8. Governance Outcomes

- Verified synthetic pipeline exists and is deterministic for fixed seed.
- Writer enforces final `\boxed{}`; solvers keep unboxed normalized answers.
- `m03_synthetic_smoke_v1` in Dataset Ledger; `m03_synthetic_smoke_eval` in Run Ledger.
- M04 stub: Public Control Adapter Reproduction Preflight.

---

## 9. Synthetic Self-Check Disclaimer (required)

**50/50 = 1.0** is **synthetic factory self-check accuracy** using generated completions as predictions. It is **not** a model score, public score, private score, or leaderboard evidence.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M03 deliverables | Yes |
| PR CI green | Yes — 26975703019 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| Merged to `main` | Yes — `fe2a7dd` (2026-06-04T20:04:51Z) |

**Next recommendation:** Owner records Submit UI zip constraints; authorize M04 preflight planning on new branch (no training without authorization).
