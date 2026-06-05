# M08 CI Run 1 — Workflow Analysis

**Milestone:** M08 — Compute and Credential Readiness Closure  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-05

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26988802789](https://github.com/m-cahill/forge/actions/runs/26988802789) |
| Trigger | `pull_request` |
| Branch | `forge/M08-compute-credential-readiness` |
| Commit SHA (PR head) | `5138594` (`5138594966fe47fd6c08041c4c0279c0150c3336`) |
| PR | [#9](https://github.com/m-cahill/forge/pull/9) |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** M08 readiness closure — compute/credential/cost/submit docs, safe local 5090 probe script (not executed), readiness manifest + validator extensions, M08 next decision. No training, inference, submission, probe execution, or baseline vendoring.

**Run type:** PR certification on `forge/M08-compute-credential-readiness` (baseline `main` at `06ada17`).

**Baseline reference:** M07 post-merge CI [26988100314](https://github.com/m-cahill/forge/actions/runs/26988100314) green. M08 extends test count 154 → 163.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~17s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~19s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~21s |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- Readiness docs + manifest; `reproduction_plan.py` extensions for `cost_accepted`, nullable `compute_path`, `ready_for_training` consistency.
- `gpu_probe.py` parsing tests; no GPU required in CI.
- Readiness manifest file tested in unit suite.

**Noise / limitations:**

- `validate_reproduction_plan.py` and `probe_local_5090.py` not invoked in CI workflow (verified locally).
- Node.js 20 deprecation annotation on checkout/setup-python (informational).

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | **163** passed |
| `compileall src` | Pass |
| `validate_reproduction_plan.py` (readiness) | Pass |
| `probe_local_5090.py --help` | Pass (not executed) |

---

## 6. Authorization State (M08)

| Field | Value |
| ----- | ----- |
| `M08_LOCAL_5090_PROBE_AUTHORIZED` | **no** |
| `M08_TRAINING_AUTHORIZED` | **no** |
| `credentials_ready` | **false** |
| `cost_accepted` | **false** |
| Probe executed | **no** |
| Training go/no-go | **NO-GO** |
| Readiness documentation | **GO** |

---

## 7. Verdict

| Question | Answer |
| -------- | ------ |
| Safe to merge for M08 scope? | **Yes** — pending owner merge permission |
| Regressions detected? | **No** |
| Certification of training/hardware probe? | **No** — by design |

---

## 8. Non-claims

This CI run does **not** certify local 5090 probe execution, CUDA/VRAM verification, model training, inference, baseline reproduction, Kaggle submission, public/private score, Kaggle-ready adapter, real adapter package, credential functionality, or copied baseline code/data.
