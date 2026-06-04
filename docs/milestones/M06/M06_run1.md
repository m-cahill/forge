# M06 CI Run 1 — Workflow Analysis

**Milestone:** M06 — Controlled Public Baseline Reproduction Execution Gate  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-04

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26985544150](https://github.com/m-cahill/forge/actions/runs/26985544150) |
| Trigger | `pull_request` |
| Branch | `forge/M06-control-repro-execution-gate` |
| Commit SHA (PR head) | `895a3cb` |
| PR | [#7](https://github.com/m-cahill/forge/pull/7) |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** M06 execution gate — Gate B schema inspection (derived notes), schema-gate reproduction manifest, execution gate docs, reproduction plan validator extensions. No training, inference, submission, or baseline reproduction.

**Run type:** PR certification on `forge/M06-control-repro-execution-gate` (baseline `main` at `34169d0`).

**Baseline reference:** M05 post-merge CI [26983281413](https://github.com/m-cahill/forge/actions/runs/26983281413) green. M06 extends test count 147 → 151.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- `reproduction_plan.py` extensions type-check and test on 3.10–3.12.
- 151 tests (+4): schema-gate file, blocked schema status, ready-for-training gates.
- Docs commit derived metadata only; no corpora or clone in repo.

**Noise / limitations:**

- `validate_reproduction_plan.py` not in CI workflow (verified locally).
- No external clone in CI (inspection performed on operator machine outside tree).
- Node.js 20 deprecation annotation on checkout/setup-python (informational).

---

## 5. Verdict

| Question | Answer |
| -------- | ------ |
| Safe to merge for M06 scope? | **Yes** — pending owner merge permission |
| Regressions detected? | **No** |
| Certification of training/reproduction? | **No** — by design |

---

## 6. Non-claims

This CI run does **not** certify baseline reproduction, training readiness, Kaggle submission, or schema parity with competition data.
