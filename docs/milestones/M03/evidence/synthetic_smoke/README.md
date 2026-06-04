# M03 synthetic smoke evidence

**Synthetic smoke only · local factory self-check only**

This directory contains a tiny solver-verified synthetic dataset (50 examples) and a local eval run using generated completions as predictions.

**Non-claims:**

- Not a Kaggle submission or leaderboard evaluation
- No public or private score
- No model training or inference
- No reproduced public baseline
- Not a model score — this is **synthetic factory self-check accuracy** (expected 100% when generator, writer, and metric align)

**Dataset:** `examples.jsonl` (full smoke set) · `examples.sample.jsonl` (preview, up to 3 per category) · `dataset_manifest.json`

**Regenerate dataset:**

```bash
python scripts/make_dataset.py \
  --dataset-id m03_synthetic_smoke_v1 \
  --seed 123 \
  --count-arithmetic 20 \
  --count-string 20 \
  --count-formatting 10 \
  --out docs/milestones/M03/evidence/synthetic_smoke/examples.jsonl \
  --manifest docs/milestones/M03/evidence/synthetic_smoke/dataset_manifest.json \
  --eval-examples docs/milestones/M03/evidence/synthetic_smoke/eval_examples.jsonl \
  --eval-predictions docs/milestones/M03/evidence/synthetic_smoke/eval_predictions.jsonl \
  --sample-out docs/milestones/M03/evidence/synthetic_smoke/examples.sample.jsonl \
  --created-at-utc 2026-06-04T20:30:00+00:00
```

**Regenerate local eval (factory self-check):**

```bash
python scripts/eval_predictions.py \
  --examples docs/milestones/M03/evidence/synthetic_smoke/eval_examples.jsonl \
  --predictions docs/milestones/M03/evidence/synthetic_smoke/eval_predictions.jsonl \
  --out docs/milestones/M03/evidence/synthetic_smoke/local_eval.json \
  --by-category docs/milestones/M03/evidence/synthetic_smoke/local_eval_by_category.csv \
  --failures docs/milestones/M03/evidence/synthetic_smoke/examples_failed.jsonl \
  --manifest docs/milestones/M03/evidence/synthetic_smoke/run_manifest.json \
  --run-id m03_synthetic_smoke_eval \
  --candidate-id m03_generated_traces
```

Expected result: **50/50 (1.0)** synthetic factory self-check accuracy — not a model or leaderboard score.
