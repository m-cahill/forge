# M12 CI Run 1 — Workflow Analysis

**Milestone:** M12 — Local CUDA PyTorch Environment Enablement  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-05

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [27043336258](https://github.com/m-cahill/forge/actions/runs/27043336258) |
| Trigger | `pull_request` |
| Branch | `forge/M12-local-cuda-pytorch-enablement` |
| Commit SHA (PR head) | `21c60e4` |
| PR | [#13](https://github.com/m-cahill/forge/pull/13) |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** M12 local CUDA PyTorch environment enablement — isolated `.venv_cuda` setup plan, CUDA verification script, sanitized CUDA environment evidence, readiness manifest with `cuda_ready_probe_only`, governance updates. No training, inference, model loading, adapters, submission, or credentials.

**Run type:** PR certification on `forge/M12-local-cuda-pytorch-enablement` (baseline `main` at `c4176a9`).

**Baseline reference:** M11 post-merge CI [27038312607](https://github.com/m-cahill/forge/actions/runs/27038312607) green. M12 extends test count 174 → 183.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~20s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~17s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~16s |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- `cuda_torch_verify.py` + `verify_cuda_torch.py` with +9 unit tests (classification, parsing, report structure).
- M12 CUDA evidence JSON and environment report committed (environment-only).
- `public_control_repro_plan_local_cuda_env_v1` manifest; local validation pass.
- `.gitignore` extended for CUDA venv paths.

**Noise / limitations:**

- CI runs on CPU-only GitHub runners — does not execute CUDA smoke tests (correct; GPU not required in CI).
- `validate_reproduction_plan.py` not invoked in CI workflow (verified locally).
- CUDA install evidence from owner machine only; `.venv_cuda` not committed.
- Node.js deprecation annotations on checkout/setup-python (informational).

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | **183** pass |
| `compileall src` | Pass |
| `validate_reproduction_plan.py` (local_cuda_env) | Pass |
| `.venv_cuda` CUDA recheck (local) | Pass — `cuda_ready_probe_only` |

---

## 6. CUDA Evidence Summary (local only)

| Field | Value |
| ----- | ----- |
| Environment | `.venv_cuda` (gitignored) |
| Python | 3.11.9 |
| PyTorch | 2.11.0+cu128 |
| `torch.cuda.is_available()` | **true** |
| GPU | RTX 5090, 32607 MiB, driver 591.86 |
| Tiny smoke | passed |
| Classification | `cuda_ready_probe_only` |

**Authorization:** `M12_LOCAL_CUDA_SETUP_AUTHORIZED = yes`; training/inference/submission **no**.

---

## 7. Verdict

| Question | Answer |
| -------- | ------ |
| CI truth signal trustworthy? | **Yes** — all matrix jobs green |
| Regression vs M11 baseline? | **No** — 183 tests pass |
| Release/milestone gate? | **Pass** for M12 PR certification |
| Blocking issues? | **None** |

**Recommendation:** Merge PR #13 with owner permission after review. `cuda_ready_probe_only` is **not** training readiness.

---

## 8. Non-claims

No training, inference, model loading, Kaggle submission, public/private score, reproduced baseline, adapters, credentials, or committed `.venv_cuda` validated by CI.
