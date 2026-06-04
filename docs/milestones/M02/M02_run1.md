# M02 CI Run 1 — Workflow Analysis

**Milestone:** M02 — Exact Local Evaluation and Artifact Discipline  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-04

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID (implementation) | [26973038855](https://github.com/m-cahill/forge/actions/runs/26973038855) |
| Run ID (final / closeout) | [26973101474](https://github.com/m-cahill/forge/actions/runs/26973101474) |
| Trigger | `pull_request` |
| Branch | `forge/M02-local-eval` |
| Commit SHA (implementation) | `c8dc65be9a930b8b4f11ec0d5dfc56464cf47167` |
| Commit SHA (PR head, closeout) | `4d014c45b526e2588ae42e74c5d0d79af1ffe9a5` |
| PR | [#3](https://github.com/m-cahill/forge/pull/3) |
| Event time (UTC) | 2026-06-04T18:59:18Z → ~2026-06-04T18:59:42Z |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** Add M02 local evaluation — eval contracts, scorer, CLI, hashing, run manifests, fixture holdouts, committed fixture evidence, governance updates.

**Run type:** PR certification after six implementation commits on `forge/M02-local-eval` (baseline `main` at `ce9dc7f`).

**Baseline reference:** M01 merged `d59d97b`; post-merge CI [26935381116](https://github.com/m-cahill/forge/actions/runs/26935381116) green. M02 extends test count 91 → 106.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~20s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~18s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~24s |

Each job runs identical steps:

| Step | Pass/Fail |
| ---- | --------- |
| checkout@v4 | Pass |
| setup-python@v5 (pip cache) | Pass |
| `pip install -e . -r requirements-dev.txt` | Pass |
| Ruff lint | Pass |
| Ruff format check | Pass |
| MyPy (`src tests`) | Pass |
| Pytest | Pass |
| Summary | Pass |

**Informational annotations:** Node.js 20 deprecation warnings on `actions/checkout@v4` and `actions/setup-python@v5` (not merge-blocking).

---

## 4. Signal vs Noise

**Signal (meaningful for M02):**

- New `eval/`, `artifacts/`, `reports/` modules type-check and test on all matrix Python versions.
- 106 unit tests (15 new: eval scorer, hashing, manifest).
- Lint/format gates cover new CLI and fixture JSONL paths.
- No weakening of M01 gates.

**Noise / limitations:**

- Fixture eval CLI not executed in CI (smoke verified locally and via committed evidence).
- No integration test invoking `git` in manifest builder on CI runners (local smoke uses git when available).
- No GPU, training, or Kaggle notebook execution.

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass (local + CI) |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | 106 passed |
| `python -m compileall src` | Pass |
| `eval_predictions.py` smoke (`predictions_mixed.jsonl`) | Pass — **6/8 = 0.75** fixture/local only |

---

## 6. Verdict

| Question | Answer |
| -------- | ------ |
| Did CI prove M02’s stated gates? | **Yes** — lint, format, types, expanded unit tests |
| Is green trustworthy? | **Yes** — all matrix jobs pass on PR head |
| Blocking issues? | **None** |
| Merge recommendation | PR #3 is **CI-green** on head `4d014c4` (run 26973101474); merge only with express owner permission |

---

## 7. Evidence Links

- Workflow run: https://github.com/m-cahill/forge/actions/runs/26973038855
- PR checks: https://github.com/m-cahill/forge/pull/3/checks
- PR head (final): `4d014c45b526e2588ae42e74c5d0d79af1ffe9a5`
- Final workflow run: https://github.com/m-cahill/forge/actions/runs/26973101474

---

## 8. Non-Claims

This CI run does **not** prove:

- Kaggle submission readiness or public/private leaderboard score
- Model training, inference, or reproduced `tonghuikang/nemotron` baseline
- Kaggle-ready adapter validity
- That fixture local score **0.75** predicts competition performance (fixture smoke only)
