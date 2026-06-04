# M05 CI Run 1 — Workflow Analysis

**Milestone:** M05 — Controlled Public Baseline Reproduction Planning and Compute Path  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-04

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26982564940](https://github.com/m-cahill/forge/actions/runs/26982564940) |
| Trigger | `pull_request` |
| Branch | `forge/M05-control-repro-planning` |
| Commit SHA (PR head) | `7867e29de8402fc9f92f035c0482ece3688ebf23` |
| PR | [#6](https://github.com/m-cahill/forge/pull/6) |
| Event time (UTC) | 2026-06-04T22:09:01Z → ~2026-06-04T22:09:31Z |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** Controlled public baseline reproduction planning — six planning docs, reproduction plan manifest contract, validation CLI, mock preflight evidence, M06 recommendation. No training, inference, submission, or baseline reproduction.

**Run type:** PR certification after five implementation commits on `forge/M05-control-repro-planning` (baseline `main` at `f54afd0`).

**Baseline reference:** M04 merged `f54afd0`; post-merge CI [26979013700](https://github.com/m-cahill/forge/actions/runs/26979013700) green. M05 extends test count 138 → 147.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26982564940/job/79624995328) |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26982564940/job/79624995327) |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26982564940/job/79624995343) |

Each job runs: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- New `baselines/reproduction_plan.py` type-checks and tests on Python 3.10–3.12.
- 147 unit tests (+9): training authorization gates, copying policy, non_claims, ready_for_training rules.
- Planning docs and small mock JSON only; no vendored baseline code or corpora.

**Noise / limitations:**

- `validate_reproduction_plan.py` not executed in CI (verified locally on mock plan).
- No GPU, training, Kaggle, Modal/Tinker execution, or baseline reproduction.

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass (local + CI) |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | 147 passed |
| `python -m compileall src` | Pass |
| `validate_reproduction_plan.py` (mock preflight) | Pass |

---

## 6. Verdict

**CI truth signal:** Green on PR #6 head `7867e29`. Safe to close M05 governance artifacts; **merge** requires separate owner permission.

**Non-claims preserved:** No submission, score, training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or training authorization.

**Remaining blockers:** Submit UI zip constraints OPEN; Kaggle API TBD; no real control candidate; corpus schema not extracted in M05.

---

## 7. Next Actions

| Owner | Action |
| ----- | ------ |
| Owner | Merge PR #6 with express permission |
| Owner | Record Submit UI zip constraints; authorize M06 kickoff + training |
| Cursor | Seed M06 stub per `M05_next_decision.md` (closeout commit) |
