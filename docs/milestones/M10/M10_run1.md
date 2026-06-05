# M10 CI Run 1 — Workflow Analysis

**Milestone:** M10 — Local 5090 Feasibility Probe  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-05

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [27027762042](https://github.com/m-cahill/forge/actions/runs/27027762042) |
| Trigger | `pull_request` |
| Branch | `forge/M10-local-5090-feasibility-probe` |
| Commit SHA (PR head) | `84529d1` |
| PR | [#11](https://github.com/m-cahill/forge/pull/11) |
| Overall conclusion | **success** |

---

## 2. Change Context

**Declared intent:** M10 local 5090 feasibility probe — run authorized safe hardware/environment probe; record sanitized JSON evidence and human-readable report; extend readiness manifest with `local_5090_probe_status`; update governance and competition rules archive. No training, inference, submission, model load, adapters, or credentials.

**Run type:** PR certification on `forge/M10-local-5090-feasibility-probe` (baseline `main` at `4fad43c`).

**Baseline reference:** M09 post-merge CI [26991673323](https://github.com/m-cahill/forge/actions/runs/26991673323) green. M10 extends test count 166 → 171.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~18s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~16s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~18s |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- Probe evidence JSON committed (hardware/environment only).
- `public_control_repro_plan_local_5090_probe_v1` manifest; `local_5090_probe_status` validation in `reproduction_plan.py`.
- +5 unit tests for M10 manifest and probe status rules.
- Competition rules archived at `docs/competition_rules.md`.

**Noise / limitations:**

- `validate_reproduction_plan.py` not invoked in CI workflow (verified locally).
- `probe_local_5090.py` not run in CI (hardware-dependent; correct).
- Node.js 20 deprecation annotation on checkout/setup-python (informational).

---

## 5. Verdict

| Question | Answer |
| -------- | ------ |
| CI truth signal trustworthy? | **Yes** — all matrix jobs green |
| Regression vs M09 baseline? | **No** — 171 tests pass |
| Release/milestone gate? | **Pass** for M10 PR certification |
| Blocking issues? | **None** |

**Recommendation:** Merge PR #11 with owner permission after review. Probe classification `visible_no_torch_cuda` is evidence-only — not training readiness.

---

## 6. Non-claims

No training, inference, Kaggle submission, public/private score, reproduced baseline, adapters, or credentials validated by CI.
