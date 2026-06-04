# M01_toolcalls.md

## Purpose

Record notable Cursor/tool actions for M01 (control baseline preflight and validation harness).

## Entries

| Time UTC | Actor | Action | Evidence / Notes |
| -------- | ----- | ------ | ---------------- |
| 2026-06-04T06:10:00Z | Cursor | M01 kickoff planning | Branch `forge/M01-control-baseline` from merged `main` |
| 2026-06-04T06:10:00Z | Cursor | Expanded M01_plan.md | Implementation-ready plan; stop before code until authorized |
| 2026-06-04T06:10:00Z | Cursor | — | CI Option A vs B: **owner decision required** |
| 2026-06-04T06:07:00Z | Cursor | Owner authorized M01 | Option A (CI in M01), inspect live repo, notebook repo-only |
| 2026-06-04T06:08:00Z | Cursor | Begin Phase A | Expanding M01_plan.md with full plan |
| 2026-06-04T06:09:00Z | Cursor | Phase A complete | M01_plan.md updated |
| 2026-06-04T06:10:00Z | Cursor | Phase B | pyproject.toml, requirements-dev.txt, CI workflow, test_import.py |
| 2026-06-04T06:12:00Z | Cursor | Phase B verified | pip install -e ., pytest, ruff, mypy all pass |
| 2026-06-04T06:13:00Z | Cursor | Phase C | boxed.py metric, test_metric_boxed.py |
| 2026-06-04T06:15:00Z | Cursor | Phase C verified | 61 tests pass |
| 2026-06-04T06:16:00Z | Cursor | Phase D | validate_submission.py, scripts/validate_submission.py, test_package_validator.py |
| 2026-06-04T06:18:00Z | Cursor | Phase D verified | 27 validator tests pass, 91 total tests pass |
| 2026-06-04T06:19:00Z | Cursor | Phase E | Inspected tonghuikang/nemotron, created public_baseline_intake.md |
| 2026-06-04T06:22:00Z | Cursor | Phase F | Created forge_m01_kaggle_debug_probe.ipynb, updated notebooks/README.md |
| 2026-06-04T06:25:00Z | Cursor | Phase G | Final verification, all checks pass (91 tests, ruff, mypy, compileall) |
| 2026-06-04T06:30:00Z | Cursor | M01 commit/PR | Pre-commit hygiene, re-verify, commit, push, PR, CI monitor, closeout |
