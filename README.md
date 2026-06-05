# FORGE

**FORGE** — Kaggle [NVIDIA Nemotron Model Reasoning Challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge) entry.

Solver-guided, artifact-first LoRA engineering for `NVIDIA-Nemotron-3-Nano-30B`: verified synthetic traces, specialist adapters, legal rank-≤32 merge/compression, and prize-eligible documentation.

## Current milestone

**M11** — Credential and cost closure continuation (stub; see `docs/milestones/M11/M11_plan.md`).

M00–M10 merged to `main` (`dc45813`). Post-merge CI **green** [27032692673](https://github.com/m-cahill/forge/actions/runs/27032692673). M10 probe: RTX 5090 visible; `torch.cuda` **false** (`visible_no_torch_cuda`). Training **NO-GO**.

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M10/evidence/readiness/public_control_repro_plan.local_5090_probe.json
```

Prior M09 manifest:

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M09/evidence/readiness/public_control_repro_plan.modal_tinker_gate.json
```

M08 readiness manifest (prior):

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M08/evidence/readiness/public_control_repro_plan.readiness.json
```

M07 training-blocked manifest (still valid):

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M07/evidence/training_gate/public_control_repro_plan.training_blocked.json
```

## Synthetic dataset (M03)

```bash
python scripts/make_dataset.py \
  --dataset-id m03_synthetic_smoke_v1 \
  --seed 123 \
  --count-arithmetic 20 \
  --count-string 20 \
  --count-formatting 10 \
  --out data/generated/m03_synthetic_smoke_v1/examples.jsonl \
  --manifest data/manifests/m03_synthetic_smoke_v1.json
```

Committed smoke evidence: `docs/milestones/M03/evidence/synthetic_smoke/` (synthetic factory self-check only).

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
