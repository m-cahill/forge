#!/usr/bin/env python3
"""Generate a verified synthetic dataset and dataset manifest.

Usage:
    python scripts/make_dataset.py \\
        --dataset-id m03_synthetic_smoke_v1 \\
        --seed 123 \\
        --count-arithmetic 20 \\
        --count-string 20 \\
        --count-formatting 10 \\
        --out data/generated/m03_synthetic_smoke_v1/examples.jsonl \\
        --manifest data/manifests/m03_synthetic_smoke_v1.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from forge_nemotron.artifacts.hashing import write_json
from forge_nemotron.data.manifest import build_dataset_manifest
from forge_nemotron.data.synthetic import (
    SyntheticExample,
    to_eval_examples,
    to_eval_predictions,
    write_eval_jsonl,
    write_synthetic_jsonl,
)
from forge_nemotron.eval.records import EvaluationExample, EvaluationPrediction
from forge_nemotron.generators.arithmetic import generate_arithmetic_batch
from forge_nemotron.generators.formatting_stress import generate_formatting_stress_batch
from forge_nemotron.generators.string_transform import generate_string_transform_batch


def _example_to_eval_dict(ex: EvaluationExample) -> dict:
    row = {
        "example_id": ex.example_id,
        "expected": ex.expected,
        "category": ex.category,
        "source": ex.source,
        "split": ex.split,
    }
    if ex.prompt is not None:
        row["prompt"] = ex.prompt
    return row


def _prediction_to_dict(pred: EvaluationPrediction) -> dict:
    row = {
        "example_id": pred.example_id,
        "completion": pred.completion,
    }
    if pred.candidate_id:
        row["candidate_id"] = pred.candidate_id
    return row


def _collect_versions(examples: list[SyntheticExample]) -> tuple[dict[str, str], dict[str, str]]:
    gen: dict[str, str] = {}
    sol: dict[str, str] = {}
    for ex in examples:
        gen[ex.category] = ex.generator_version
        sol[ex.category] = ex.solver_version
    return gen, sol


def _write_sample(path: Path, examples: list[SyntheticExample], max_per_category: int = 3) -> None:
    """Write a small preview JSONL (up to max_per_category per category)."""
    by_cat: dict[str, list[SyntheticExample]] = {}
    for ex in examples:
        by_cat.setdefault(ex.category, []).append(ex)
    preview: list[SyntheticExample] = []
    for cat in sorted(by_cat):
        preview.extend(by_cat[cat][:max_per_category])
    preview.sort(key=lambda e: e.example_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for ex in preview:
            f.write(json.dumps(ex.to_dict(), sort_keys=True) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate verified synthetic dataset JSONL.")
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--count-arithmetic", type=int, default=20)
    parser.add_argument("--count-string", type=int, default=20)
    parser.add_argument("--count-formatting", type=int, default=10)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--eval-examples", type=Path, default=None)
    parser.add_argument("--eval-predictions", type=Path, default=None)
    parser.add_argument("--sample-out", type=Path, default=None)
    parser.add_argument(
        "--created-at-utc",
        default=None,
        help="Inject timestamp for deterministic manifest tests",
    )
    args = parser.parse_args(argv)

    raw: list[dict] = []
    raw.extend(generate_arithmetic_batch(seed=args.seed, count=args.count_arithmetic))
    raw.extend(generate_string_transform_batch(seed=args.seed, count=args.count_string))
    raw.extend(generate_formatting_stress_batch(seed=args.seed, count=args.count_formatting))

    expected_total = args.count_arithmetic + args.count_string + args.count_formatting
    if len(raw) != expected_total:
        print(
            f"error: expected {expected_total} raw examples, got {len(raw)}",
            file=sys.stderr,
        )
        return 2

    try:
        result = write_synthetic_jsonl(args.out, raw)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    examples = list(result.examples)
    gen_versions, sol_versions = _collect_versions(examples)

    manifest = build_dataset_manifest(
        dataset_id=args.dataset_id,
        dataset_path=args.out,
        seed=args.seed,
        example_count=len(examples),
        category_counts=result.category_counts,
        generator_versions=gen_versions,
        solver_versions=sol_versions,
        verified_count=len(examples),
        rejected_count=result.rejected_count,
        created_at_utc=args.created_at_utc,
        notes="m03 synthetic smoke; not for leaderboard; solver-verified only",
    )
    write_json(args.manifest, manifest)

    if args.sample_out:
        _write_sample(args.sample_out, examples)

    if args.eval_examples:
        eval_rows = [_example_to_eval_dict(ex) for ex in to_eval_examples(examples)]
        write_eval_jsonl(args.eval_examples, eval_rows)

    if args.eval_predictions:
        pred_rows = [_prediction_to_dict(p) for p in to_eval_predictions(examples)]
        write_eval_jsonl(args.eval_predictions, pred_rows)

    print(f"dataset_id={args.dataset_id}")
    print(f"example_count={len(examples)}")
    print(f"category_counts={result.category_counts}")
    print(f"dataset_sha256={manifest['dataset_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
