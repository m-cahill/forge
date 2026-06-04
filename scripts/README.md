# FORGE Scripts

CLI entry points for dataset generation, training, evaluation, packaging, and submission validation.

## Available

| Script | Purpose |
| ------ | ------- |
| `validate_submission.py` | Structural LoRA `submission.zip` validation (M01) |
| `eval_predictions.py` | Local prediction scoring vs JSONL examples (M02) |

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

## Planned

- `make_dataset.py`
- `train_sft.py`
- `package_adapter.py`
- `merge_adapters.py`
- `submit_notes.py`

See `docs/FORGE_ANCHOR.md` for the full script map.
