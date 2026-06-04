# FORGE

**FORGE** — Kaggle [NVIDIA Nemotron Model Reasoning Challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge) entry.

Solver-guided, artifact-first LoRA engineering for `NVIDIA-Nemotron-3-Nano-30B`: verified synthetic traces, specialist adapters, legal rank-≤32 merge/compression, and prize-eligible documentation.

## Current milestone

**M03** — Solver and synthetic trace factory (**active** on branch `forge/M03-solver-factory`).

M00–M02 are merged to `main`. M03 builds deterministic solvers, verified synthetic traces, dataset manifests, and local factory self-check eval. No Kaggle submission, public score, model training, or reproduced control baseline yet.

## Local evaluation (M02)

```bash
python scripts/eval_predictions.py \
  --examples tests/fixtures/eval/examples.jsonl \
  --predictions tests/fixtures/eval/predictions_mixed.jsonl \
  --out artifacts/runs/m02_fixture_eval/local_eval.json \
  --by-category artifacts/runs/m02_fixture_eval/local_eval_by_category.csv \
  --failures artifacts/runs/m02_fixture_eval/examples_failed.jsonl \
  --manifest artifacts/runs/m02_fixture_eval/run_manifest.json \
  --run-id m02_fixture_eval \
  --candidate-id fixture_candidate
```

Outputs under `artifacts/runs/` are gitignored; committed fixture evidence lives under `docs/milestones/M02/evidence/fixture_eval/`.

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
scripts/          CLI wrappers (eval, validate submission, …)
src/forge_nemotron/  metric, eval, artifacts, reports, packaging, …
tests/            unit, integration, e2e, fixtures/eval
artifacts/runs/   Run manifests and eval outputs (large files gitignored)
submissions/      Candidate zips and evidence (contents gitignored)
```

## Hard gates (summary)

- Submit only `submission.zip` with valid LoRA adapter; rank ≤ 32.
- Never submit without package validation.
- Never train on holdout data.

See `.cursorrules` and `docs/FORGE_ANCHOR.md` for full rules.
