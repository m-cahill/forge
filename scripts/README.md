# FORGE Scripts

CLI entry points for dataset generation, training, evaluation, packaging, and submission validation.

## Available

| Script | Purpose |
| ------ | ------- |
| `validate_submission.py` | Structural LoRA `submission.zip` validation (M01) |
| `eval_predictions.py` | Local prediction scoring vs JSONL examples (M02) |
| `make_dataset.py` | Verified synthetic dataset + manifest generation (M03) |
| `validate_candidate_manifest.py` | Adapter candidate manifest JSON validation (M04) |
| `validate_reproduction_plan.py` | Reproduction plan manifest JSON validation (M05) |

### Local evaluation (M02)

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

Options:

- `--strict-extra-predictions` — fail (exit 1) when predictions reference unknown `example_id`s
- `--category-filter CATEGORY` — repeat to score a subset of categories

Module equivalent: `python -m forge_nemotron.eval.scorer --help`

### Synthetic dataset (M03)

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

Optional: `--eval-examples` and `--eval-predictions` for local factory self-check JSONL.

Evidence copy: `docs/milestones/M03/evidence/synthetic_smoke/`

### Candidate manifest (M04)

```bash
python scripts/validate_candidate_manifest.py \
  docs/milestones/M04/evidence/control_preflight/control_candidate_manifest.preflight.json
```

Mock evidence: `docs/milestones/M04/evidence/control_preflight/` (preflight only — not an adapter).

### Reproduction plan (M05)

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M05/evidence/reproduction_plan/public_control_repro_plan.preflight.json
```

Mock evidence: `docs/milestones/M05/evidence/reproduction_plan/` (preflight only — not training authorization).

## Planned

- `train_sft.py`
- `package_adapter.py`
- `merge_adapters.py`
- `submit_notes.py`

See `docs/FORGE_ANCHOR.md` for the full script map.
