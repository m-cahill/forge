# M09 CI Run 1 — Workflow Analysis

**Milestone:** M09 — Modal/Tinker Setup Gate  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-05

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26990264400](https://github.com/m-cahill/forge/actions/runs/26990264400) |
| Trigger | `pull_request` |
| Branch | `forge/M09-modal-tinker-setup-gate` |
| Commit SHA (implementation) | `434a7de` |
| Commit SHA (PR head at closeout) | `861fc71` |
| PR | [#10](https://github.com/m-cahill/forge/pull/10) |
| CI run (implementation) | [26990264400](https://github.com/m-cahill/forge/actions/runs/26990264400) **success** |
| CI run (closeout) | [26990298009](https://github.com/m-cahill/forge/actions/runs/26990298009) **success** |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** M09 Modal/Tinker setup gate — readiness evidence for Modal/Tinker/cloud credentials and cost; external compute path decision; credential storage policy; Kaggle API/Submit UI status; local 5090 probe blocked; SQ-CORPUS-001 status; readiness manifest + validator extensions; M09 next decision. No training, inference, submission, probe execution, or baseline vendoring.

**Run type:** PR certification on `forge/M09-modal-tinker-setup-gate` (baseline `main` at `ac7c5f2`).

**Baseline reference:** M08 post-merge CI [26989604207](https://github.com/m-cahill/forge/actions/runs/26989604207) green. M09 extends test count 163 → 166.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~18s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~16s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~22s |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- Modal/Tinker readiness docs; external compute path decision; credential policy check.
- `public_control_repro_plan_modal_tinker_gate_v1` manifest; optional credential status field validation in `reproduction_plan.py`.
- +3 unit tests for M09 manifest and credential status rules.

**Noise / limitations:**

- `validate_reproduction_plan.py` not invoked in CI workflow (verified locally).
- Node.js 20 deprecation annotation on checkout/setup-python (informational).

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | **166** passed |
| `compileall src` | Pass |
| `validate_reproduction_plan.py` (modal_tinker_gate) | Pass |
| Local 5090 probe | **not executed** |

---

## 6. Authorization State (M09)

| Field | Value |
| ----- | ----- |
| `M09_LOCAL_5090_PROBE_AUTHORIZED` | **no** |
| `M09_TRAINING_AUTHORIZED` | **no** |
| Probe executed | **no** |
| `credentials_ready` | **false** |
| `cost_accepted` | **false** |
| Modal/Tinker/cloud | **TBD** |
| Submit UI constraints | **OPEN** |
| Kaggle API | **TBD** |
| Training go/no-go | **NO-GO** |
| Setup gate documentation | **GO** |

---

## 7. Verdict

| Question | Answer |
| -------- | ------ |
| Safe to merge for M09 scope? | **Yes** — pending owner merge permission |
| Regressions detected? | **No** |
| Certification of training/credentials? | **No** — by design |

---

## 8. Non-claims

No local 5090 probe executed; no Kaggle submission; no public/private score; no model training or inference; no reproduced baseline; no Kaggle-ready or real adapter package; no copied/vendored baseline code/data; no committed credentials.
