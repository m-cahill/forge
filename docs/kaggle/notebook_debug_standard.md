# Notebook Debug Standard — FORGE

**Authority:** Subordinate to [`docs/kaggle_submission_bible.md`](../kaggle_submission_bible.md).

Every FORGE Kaggle notebook (debug, smoke, or submission path) should include explicit diagnostic cells **before** any scored or commit-mode claim.

## Required debug cells

Print or log at minimum:

1. **Python** — `sys.version`, `platform.platform()`
2. **Paths** — `os.getcwd()`, first 10 `sys.path` entries
3. **Kaggle env** — `KAGGLE_KERNEL_RUN_TYPE`, `KAGGLE_URL_BASE` (if set)
4. **Filesystem** — existence of `/kaggle`, `/kaggle/input`, `/kaggle/working`; truncated `os.listdir` for each
5. **Inputs** — attached datasets, competition data paths, base model / adapter input paths discovered
6. **Internet** — policy setting; only test network if allowed and not required for scored path
7. **Accelerator** — GPU visibility; `nvidia-smi` when available
8. **ML stack** — `torch` / `cuda` availability and versions if used
9. **Disk** — free space on working volume when practical
10. **Outputs** — exact paths written; file sizes; SHA256 for `submission.zip` and key artifacts
11. **Timing** — wall time for major stages
12. **Errors** — full tracebacks with cell context

## Mode declaration

Each run must state:

| Mode | Use |
| ---- | --- |
| Interactive | Debugging only; does not prove submission |
| Commit | Notebook commit; does not alone prove leaderboard score |
| Submit / scored | Competition scoring path; requires full evidence row |

## FORGE-specific outputs

- Real competition artifact: `/kaggle/working/submission.zip` (or path required by UI)
- Never conflate smoke outputs under `tmp/` with scored submission paths
- Do **not** use `submission.csv` — FORGE is LoRA zip, not CSV

## Evidence

Copy summarized results into [`kaggle_setup_evidence.md`](kaggle_setup_evidence.md) or milestone `MNN_run*.md`.

## Repo-first policy

Notebook source lives in `notebooks/`. Edit in repo → commit → reupload to Kaggle. Kaggle-only edits are emergency-only and must be backported.
