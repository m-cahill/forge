# FORGE

**FORGE** — Kaggle [NVIDIA Nemotron Model Reasoning Challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge) entry.

Solver-guided, artifact-first LoRA engineering for `NVIDIA-Nemotron-3-Nano-30B`: verified synthetic traces, specialist adapters, legal rank-≤32 merge/compression, and prize-eligible documentation.

## Current milestone

**M00** — Anchor, competition intake, and Kaggle submission bible (`forge/M00-anchor-intake`).

No Kaggle submission, public score, or reproduced control adapter yet.

## Source of truth

| Document | Role |
| -------- | ---- |
| [`docs/forge.md`](docs/forge.md) | **Ultimate Truth** — milestones, submissions, runs, risks |
| [`docs/FORGE_ANCHOR.md`](docs/FORGE_ANCHOR.md) | Strategic doctrine and milestone sequence |
| [`docs/kaggle_submission_bible.md`](docs/kaggle_submission_bible.md) | Kaggle notebook/submission operational reference |

## Notebook workflow

1. Cursor updates notebooks in this repo.
2. Commit changes.
3. Operator reuploads/resyncs to Kaggle.

Emergency Kaggle-only edits must be backported before they count as truth.

## Layout (initial scaffold)

```text
configs/          Training, data, merge, eval configs
data/             Raw, external, generated data + manifests
docs/             Governance, Kaggle runbooks, milestones
notebooks/        Kaggle/local notebooks
scripts/          CLI wrappers (M01+)
src/forge_nemotron/  metric, solvers, generators, training, packaging, eval
tests/            unit, integration, e2e
artifacts/runs/   Run manifests and eval outputs (large files gitignored)
submissions/      Candidate zips and evidence (contents gitignored)
```

## Hard gates (summary)

- Submit only `submission.zip` with valid LoRA adapter; rank ≤ 32.
- Never submit without package validation.
- Never train on holdout data.

See `.cursorrules` and `docs/FORGE_ANCHOR.md` for full rules.
