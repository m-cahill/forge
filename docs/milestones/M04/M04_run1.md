# M04 CI Run 1 — Workflow Analysis

**Milestone:** M04 — Public Control Adapter Reproduction Preflight  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-04

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26977971068](https://github.com/m-cahill/forge/actions/runs/26977971068) |
| Trigger | `pull_request` |
| Branch | `forge/M04-control-preflight` |
| Commit SHA (PR head) | `26861ffbbb526ad313bdd299e26c1de1b7d5d7e8` |
| PR | [#5](https://github.com/m-cahill/forge/pull/5) |
| Event time (UTC) | 2026-06-04T20:34:50Z → ~2026-06-04T20:35:15Z |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** Public control reproduction preflight — baseline dossier, format mapping, adapter candidate manifest contract, mock preflight evidence, promotion gates, M05 recommendation. No training, submission, or baseline reproduction.

**Run type:** PR certification after five commits on `forge/M04-control-preflight` (baseline `main` at `fe2a7dd` / governance `7334b4f`).

**Baseline reference:** M03 merged `fe2a7dd`; post-merge CI [26976448338](https://github.com/m-cahill/forge/actions/runs/26976448338) green. M04 extends test count 127 → 138.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26977971068/job/79609705361) |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26977971068/job/79609705391) |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26977971068/job/79609705404) |

Each job runs: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- New `adapters/candidate_manifest.py` type-checks and tests on Python 3.10–3.12.
- 138 unit tests (+11): rank >32 rejection, status rules, JSON roundtrip.
- Docs-only baseline mapping; no vendored baseline code.

**Noise / limitations:**

- `validate_candidate_manifest.py` not executed in CI (verified locally on mock manifest).
- No GPU, training, Kaggle, Modal/Tinker, or baseline reproduction.

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass (local + CI) |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | 138 passed |
| `python -m compileall src` | Pass |
| `validate_candidate_manifest.py` (mock preflight) | Pass |

---

## 6. Verdict

**CI truth signal:** Green on PR #5 head `26861ff`. Safe to close M04 governance artifacts; **merge** requires separate owner permission.

**Non-claims preserved:** No submission, score, training, inference, reproduced baseline, Kaggle-ready adapter, or copied baseline code.

**Remaining blockers:** Submit UI zip constraints OPEN; Kaggle API TBD; no real control candidate.
