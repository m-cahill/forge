# M07 CI Run 1 — Workflow Analysis

**Milestone:** M07 — Controlled Public Baseline Training Authorization Gate  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-05

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [26986703969](https://github.com/m-cahill/forge/actions/runs/26986703969) |
| Trigger | `pull_request` |
| Branch | `forge/M07-training-authorization-gate` |
| Commit SHA (PR head at analysis) | `ce1d258` |
| Final PR head (closeout) | `1ec70eb` |
| PR | [#8](https://github.com/m-cahill/forge/pull/8) |
| Overall conclusion | **success** |
| Final CI run (closeout push) | [26986736831](https://github.com/m-cahill/forge/actions/runs/26986736831) **success** |

---

## 2. Change Context

**Declared intent:** M07 training authorization gate (Path A blocked) — gate docs, training-blocked reproduction manifest, training config draft, dry-run command plan, +3 unit tests. No training, inference, submission, or baseline reproduction.

**Run type:** PR certification on `forge/M07-training-authorization-gate` (baseline `main` at `a7de356`).

**Baseline reference:** M06 post-merge CI [26985969954](https://github.com/m-cahill/forge/actions/runs/26985969954) green. M07 extends test count 151 → 154.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~18s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~18s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~21s |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- Docs-only + small test delta; training-blocked manifest path tested in unit suite.
- `reproduction_plan.py` ready-for-training gate tests (+3) pass on 3.10–3.12.
- No corpora, adapters, or baseline clone in repo.

**Noise / limitations:**

- `validate_reproduction_plan.py` not in CI workflow (verified locally).
- Node.js 20 deprecation annotation on checkout/setup-python (informational).

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | **154** passed |
| `compileall src` | Pass |
| `validate_reproduction_plan.py` (training_blocked) | Pass |

---

## 6. Authorization State (M07)

| Field | Value |
| ----- | ----- |
| `M07_TRAINING_AUTHORIZED` | **no** |
| `training_authorized` | **false** |
| `ready_for_training` | **false** |
| Training go/no-go | **NO-GO** |
| Gate documentation | **GO** |

---

## 7. Verdict

| Question | Answer |
| -------- | ------ |
| Safe to merge for M07 scope? | **Yes** — pending owner merge permission |
| Regressions detected? | **No** |
| Certification of training/reproduction? | **No** — by design |

---

## 8. Non-claims

This CI run does **not** certify model training, inference, baseline reproduction, Kaggle submission, public/private score, Kaggle-ready adapter, real adapter package, or compute/credential readiness beyond documented TBD fields.
