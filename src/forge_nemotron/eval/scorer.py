"""Local evaluation engine for fixture and holdout predictions."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from forge_nemotron.eval.records import (
    CategoryScore,
    EvaluationExample,
    EvaluationPrediction,
    EvaluationResult,
    validate_unique_example_ids,
)
from forge_nemotron.metric.boxed import extract_final_boxed_answer, score_prediction

METRIC_VERSION = "boxed_v1@forge_nemotron-0.1.0"


@dataclass(frozen=True)
class EvalReport:
    """Aggregate local evaluation report."""

    total: int
    correct: int
    accuracy: float
    category_scores: tuple[CategoryScore, ...]
    missing_prediction_count: int
    extra_prediction_count: int
    failed_examples: tuple[EvaluationResult, ...]
    warnings: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "total": self.total,
            "correct": self.correct,
            "accuracy": self.accuracy,
            "missing_prediction_count": self.missing_prediction_count,
            "extra_prediction_count": self.extra_prediction_count,
            "category_scores": [c.to_dict() for c in self.category_scores],
            "metric_version": METRIC_VERSION,
            "warnings": list(self.warnings),
        }


def _classify_failure(completion: str | None, matched: bool) -> str | None:
    if matched:
        return None
    if completion is None:
        return "missing_prediction"
    if extract_final_boxed_answer(completion) is None:
        return "no_boxed"
    return "wrong_answer"


def score_examples(
    examples: list[EvaluationExample],
    predictions: list[EvaluationPrediction],
    *,
    strict_extra_predictions: bool = False,
) -> EvalReport:
    """Score predictions against examples using the boxed metric."""
    validate_unique_example_ids(examples)

    pred_by_id: dict[str, EvaluationPrediction] = {}
    duplicate_ids: list[str] = []
    for pred in predictions:
        if pred.example_id in pred_by_id:
            duplicate_ids.append(pred.example_id)
        pred_by_id[pred.example_id] = pred

    warnings: list[str] = []
    if duplicate_ids:
        warnings.append(f"duplicate prediction example_ids: {sorted(set(duplicate_ids))}")

    example_ids = {ex.example_id for ex in examples}
    extra_ids = sorted(set(pred_by_id) - example_ids)
    extra_count = len(extra_ids)
    if extra_ids:
        msg = f"extra predictions for unknown example_ids: {extra_ids}"
        if strict_extra_predictions:
            raise ValueError(msg)
        warnings.append(msg)

    results: list[EvaluationResult] = []
    correct = 0

    for ex in sorted(examples, key=lambda e: e.example_id):
        pred_entry = pred_by_id.get(ex.example_id)
        if pred_entry is None:
            matched = False
            predicted: str | None = None
            completion: str | None = None
        else:
            completion = pred_entry.completion
            matched = score_prediction(pred_entry.completion, ex.expected)
            predicted = extract_final_boxed_answer(pred_entry.completion)

        if matched:
            correct += 1
        else:
            results.append(
                EvaluationResult(
                    example_id=ex.example_id,
                    expected=ex.expected,
                    predicted=predicted,
                    matched=False,
                    category=ex.category,
                    error_type=_classify_failure(completion, matched),
                )
            )

    missing_count = sum(1 for ex in examples if ex.example_id not in pred_by_id)

    category_totals: dict[str, list[int]] = {}
    for ex in examples:
        pred_entry = pred_by_id.get(ex.example_id)
        if pred_entry is None:
            is_correct = False
        else:
            is_correct = score_prediction(pred_entry.completion, ex.expected)
        bucket = category_totals.setdefault(ex.category, [0, 0])
        bucket[0] += 1
        if is_correct:
            bucket[1] += 1

    category_scores = tuple(
        CategoryScore(category=cat, total=totals[0], correct=totals[1])
        for cat, totals in sorted(category_totals.items())
    )

    total = len(examples)
    accuracy = correct / total if total else 0.0

    failed_sorted = tuple(sorted(results, key=lambda r: r.example_id))

    return EvalReport(
        total=total,
        correct=correct,
        accuracy=accuracy,
        category_scores=category_scores,
        missing_prediction_count=missing_count,
        extra_prediction_count=extra_count,
        failed_examples=failed_sorted,
        warnings=tuple(warnings),
    )


def load_examples_jsonl(path: Path) -> list[EvaluationExample]:
    """Load examples from a JSONL file."""
    examples: list[EvaluationExample] = []
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON") from exc
            examples.append(EvaluationExample.from_dict(data))
    validate_unique_example_ids(examples)
    return examples


def load_predictions_jsonl(path: Path) -> list[EvaluationPrediction]:
    """Load predictions from a JSONL file."""
    predictions: list[EvaluationPrediction] = []
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON") from exc
            predictions.append(EvaluationPrediction.from_dict(data))
    return predictions


def write_category_csv(path: Path, report: EvalReport) -> None:
    """Write per-category scores as CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["category,total,correct,accuracy"]
    for cs in report.category_scores:
        lines.append(f"{cs.category},{cs.total},{cs.correct},{cs.accuracy:.6f}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_failures_jsonl(path: Path, report: EvalReport) -> None:
    """Write failed examples as JSONL."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for result in report.failed_examples:
            f.write(json.dumps(result.to_dict(), sort_keys=True) + "\n")


def filter_examples_by_category(
    examples: list[EvaluationExample],
    categories: set[str] | None,
) -> list[EvaluationExample]:
    """Return examples restricted to the given categories."""
    if not categories:
        return examples
    return [ex for ex in examples if ex.category in categories]


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for local prediction evaluation."""
    import argparse
    import subprocess
    import sys
    from datetime import datetime, timezone

    from forge_nemotron.artifacts.hashing import sha256_file, write_json
    from forge_nemotron.reports.run_manifest import build_run_manifest

    parser = argparse.ArgumentParser(description="Score local predictions against examples.")
    parser.add_argument("--examples", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--by-category", type=Path, required=True)
    parser.add_argument("--failures", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--run-id", default="local_eval")
    parser.add_argument("--candidate-id", default="unknown")
    parser.add_argument("--strict-extra-predictions", action="store_true")
    parser.add_argument(
        "--category-filter",
        action="append",
        default=None,
        help="Repeatable category filter (omit to score all categories)",
    )
    args = parser.parse_args(argv)

    examples = load_examples_jsonl(args.examples)
    categories = set(args.category_filter) if args.category_filter else None
    examples = filter_examples_by_category(examples, categories)

    predictions = load_predictions_jsonl(args.predictions)
    if categories:
        allowed = {ex.example_id for ex in examples}
        predictions = [p for p in predictions if p.example_id in allowed]

    try:
        report = score_examples(
            examples,
            predictions,
            strict_extra_predictions=args.strict_extra_predictions,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    for warning in report.warnings:
        print(f"warning: {warning}", file=sys.stderr)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    write_json(args.out, report.to_dict())
    write_category_csv(args.by_category, report)
    write_failures_jsonl(args.failures, report)

    input_hashes = {
        "examples_sha256": sha256_file(args.examples),
        "predictions_sha256": sha256_file(args.predictions),
    }
    hashes_path = args.manifest.parent / "input_hashes.json"
    write_json(hashes_path, input_hashes)

    git_commit = "unknown"
    branch = "unknown"
    try:
        git_commit = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip() or "unknown"
        )
        branch = (
            subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
            or "unknown"
        )
    except (subprocess.SubprocessError, FileNotFoundError):
        print("warning: could not determine git metadata", file=sys.stderr)

    manifest = build_run_manifest(
        run_id=args.run_id,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        git_commit=git_commit,
        branch=branch,
        run_type="local_eval",
        candidate_id=args.candidate_id,
        examples_path=str(args.examples),
        predictions_path=str(args.predictions),
        examples_sha256=input_hashes["examples_sha256"],
        predictions_sha256=input_hashes["predictions_sha256"],
        metric_version=METRIC_VERSION,
        local_score=report.accuracy,
        local_score_by_category={cs.category: cs.accuracy for cs in report.category_scores},
        artifact_paths=[
            str(args.out),
            str(args.by_category),
            str(args.failures),
            str(hashes_path),
        ],
        notes="fixture/local eval only; not leaderboard relevant",
    )
    write_json(args.manifest, manifest)

    if args.strict_extra_predictions and report.extra_prediction_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
