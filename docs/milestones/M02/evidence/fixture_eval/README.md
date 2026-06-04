# M02 fixture evaluation evidence

**Fixture only · local evaluation only**

This directory contains a tiny smoke run of `scripts/eval_predictions.py` against `tests/fixtures/eval/`.

**Non-claims:**

- Not a Kaggle submission or leaderboard evaluation
- No public or private score
- No model training or inference
- No reproduced public baseline

**Inputs:** `examples.jsonl`, `predictions_mixed.jsonl` (see repo `tests/fixtures/eval/`).

**Regenerate locally:**

```bash
python scripts/eval_predictions.py \
  --examples tests/fixtures/eval/examples.jsonl \
  --predictions tests/fixtures/eval/predictions_mixed.jsonl \
  --out docs/milestones/M02/evidence/fixture_eval/local_eval.json \
  --by-category docs/milestones/M02/evidence/fixture_eval/local_eval_by_category.csv \
  --failures docs/milestones/M02/evidence/fixture_eval/examples_failed.jsonl \
  --manifest docs/milestones/M02/evidence/fixture_eval/run_manifest.json \
  --run-id m02_fixture_eval \
  --candidate-id fixture_candidate
```
