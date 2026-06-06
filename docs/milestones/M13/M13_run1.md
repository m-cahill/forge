# M13 CI Run 1 — Workflow Analysis

**Milestone:** M13 — Local Training Feasibility Dry Run  
**Mode:** DELTA AUDIT / consumer-certification (PR CI on feature branch)  
**Analysis date:** 2026-06-06

---

## 1. Workflow Identity

| Field | Value |
| ----- | ----- |
| Workflow name | CI |
| Run ID | [27048718537](https://github.com/m-cahill/forge/actions/runs/27048718537) |
| Trigger | `pull_request` |
| Branch | `forge/M13-local-training-feasibility-dry-run` |
| Commit SHA (PR head) | `9326041` |
| PR | [#14](https://github.com/m-cahill/forge/pull/14) |
| Overall conclusion | **success** |

**Prior failed run:** [27048688808](https://github.com/m-cahill/forge/actions/runs/27048688808) — pytest failed on CI (no torch); fixed in `9326041`.

---

## 2. Change Context

**Declared intent:** M13 local CUDA training feasibility dry run — toy MLP forward/backward/update in `.venv_cuda`, memory/timing evidence, readiness manifest with `cuda_training_feasibility_pass`, governance updates. No real model training, inference, model loading, adapters, submission, or credentials.

**Run type:** PR certification on `forge/M13-local-training-feasibility-dry-run` (baseline `main` at `fc5040d`).

**Baseline reference:** M12 post-merge CI [27043969691](https://github.com/m-cahill/forge/actions/runs/27043969691) green.

---

## 3. Job Inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
| ----------- | --------- | ------- | --------- | ----- |
| test (3.10) | Yes | Matrix Python 3.10 | Pass | ~22s |
| test (3.11) | Yes | Matrix Python 3.11 | Pass | ~18s |
| test (3.12) | Yes | Matrix Python 3.12 | Pass | ~20s |

Each job: checkout, setup-python, editable install, Ruff lint/format, MyPy, Pytest.

---

## 4. Signal vs Noise

**Signal:**

- `cuda_training_feasibility.py` + `run_cuda_training_feasibility.py` with unit tests (classification, memory snapshots, no-torch path).
- M13 feasibility evidence JSON and human report committed (telemetry only).
- `public_control_repro_plan_local_training_feasibility_v1` manifest; local validation pass.
- `local_training_feasibility_status` validator rules + tests.

**Noise / limitations:**

- CI runs on CPU-only GitHub runners — does not execute CUDA dry run (correct).
- Torch-dependent loop tests skipped on CI when PyTorch not installed.
- `validate_reproduction_plan.py` not invoked in CI workflow (verified locally).
- CUDA dry run evidence from owner machine only; `.venv_cuda` not committed.
- Node.js deprecation annotations on checkout/setup-python (informational).

---

## 5. Local Verification Summary

| Check | Result |
| ----- | ------ |
| `ruff check .` | Pass |
| `ruff format --check .` | Pass |
| `mypy src tests` | Pass |
| `pytest -q` | Pass (194 collected) |
| `compileall src` | Pass |
| `validate_reproduction_plan.py` (local_training_feasibility) | Pass |
| `.venv_cuda` dry run (local) | Pass — `cuda_training_feasibility_pass` |

---

## 6. Feasibility Evidence Summary (local only)

| Field | Value |
| ----- | ----- |
| Classification | `cuda_training_feasibility_pass` |
| GPU | NVIDIA GeForce RTX 5090 |
| PyTorch | 2.11.0+cu128 |
| Steps | 3 |
| Peak allocated | ~18.2 MiB |
| Model artifacts | none |

---

## 7. Verdict

**CI truth signal:** Green on all matrix jobs after CI fix. Safe to merge pending owner permission.

**Not certified by CI:** CUDA dry run, training feasibility on GPU, manifest CLI in workflow.

**Recommendation:** Merge PR #14; proceed to M14 adapter feasibility planning only (not implementation) per `M13_next_decision.md`.
