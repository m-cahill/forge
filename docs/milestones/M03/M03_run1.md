# M03 CI Run 1 — Workflow Analysis

**Milestone:** M03 — Solver and Synthetic Trace Factory  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-04

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26975703019](https://github.com/m-cahill/forge/actions/runs/26975703019) |
| Trigger | `pull_request` |
| Branch | `forge/M03-solver-factory` |
| Commit SHA (PR head) | `1c7dde268faa55a42ebba0d9f202531e99509334` |
| PR | [#4](https://github.com/m-cahill/forge/pull/4) |
| Event time (UTC) | 2026-06-04T19:50:55Z → ~2026-06-04T19:51:18Z |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** Add solver-verified synthetic trace factory — solvers, generators, synthetic writer, dataset manifest, `make_dataset.py`, committed smoke evidence, governance updates.

**Run type:** PR certification after three commits on `forge/M03-solver-factory` (baseline `main` at `e78dc97`).

**Baseline reference:** M02 merged `e78dc97`; post-merge CI [26973864069](https://github.com/m-cahill/forge/actions/runs/26973864069) green. M03 extends test count 106 → 127.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26975703019/job/79602040610) |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26975703019/job/79602040587) |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | [job](https://github.com/m-cahill/forge/actions/runs/26975703019/job/79602040585) |

Each job runs: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

**Informational:** Node.js 20 deprecation warnings on GitHub Actions (not merge-blocking).

---

## 4. Signal vs Noise

**Signal:**

- New `solvers/`, `generators/`, `data/` modules type-check and test on Python 3.10–3.12.
- 127 unit tests (+21): solver base, arithmetic, string transform, determinism, writer, manifest.
- No weakening of M01/M02 gates.

**Noise / limitations:**

- `make_dataset.py` and `eval_predictions.py` smoke not executed in CI (verified locally and via committed evidence).
- No GPU, training, Kaggle, or baseline reproduction.

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass (local + CI) |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | 127 passed |
| `python -m compileall src` | Pass |
| `make_dataset.py` smoke (seed 123, 50 examples) | Pass — SHA256 `d177d827…` |
| `eval_predictions.py` synthetic self-check | Pass — **50/50 = 1.0** (factory self-check only) |

---

## 6. Verdict

| Question | Answer |
| -------- | ------ |
| Did CI prove M03’s stated gates? | **Yes** |
| Is green trustworthy? | **Yes** — all matrix jobs pass on PR head |
| Blocking issues? | **None** |
| Merge recommendation | PR #4 is **CI-green** on head `1c7dde2` (run 26975703019); merge only with express owner permission |

---

## 7. Non-claims (required)

- No Kaggle submission, public/private score, model training, model inference, reproduced baseline, or Kaggle-ready adapter.
- Synthetic factory self-check 1.0 is **not** leaderboard or model evidence.
