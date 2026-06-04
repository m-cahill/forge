"""Synthetic example records and JSONL writer with verification gates."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from forge_nemotron.eval.records import EvaluationExample, EvaluationPrediction
from forge_nemotron.generators._trace import FINAL_ANSWER_PREFIX, strip_final_answer_lines
from forge_nemotron.metric.boxed import extract_final_boxed_answer

EVAL_SPLIT_SYNTHETIC_SMOKE = "synthetic_smoke"


@dataclass(frozen=True)
class SyntheticExample:
    """One verified synthetic training-style example."""

    example_id: str
    category: str
    prompt: str
    completion: str
    expected: str
    source: str
    generator_version: str
    solver_version: str
    seed: int
    verified: bool
    metadata: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "example_id": self.example_id,
            "category": self.category,
            "prompt": self.prompt,
            "completion": self.completion,
            "expected": self.expected,
            "source": self.source,
            "generator_version": self.generator_version,
            "solver_version": self.solver_version,
            "seed": self.seed,
            "verified": self.verified,
            "metadata": self.metadata,
        }

    @classmethod
    def from_pre_writer_dict(cls, data: dict[str, Any]) -> SyntheticExample:
        completion = build_completion(
            reasoning=str(data.get("reasoning", "")),
            answer=str(data["expected"]),
        )
        return cls(
            example_id=str(data["example_id"]),
            category=str(data["category"]),
            prompt=str(data["prompt"]),
            completion=completion,
            expected=str(data["expected"]),
            source=str(data.get("source", "m03_synthetic")),
            generator_version=str(data.get("generator_version", "unknown")),
            solver_version=str(data.get("solver_version", "unknown")),
            seed=int(data["seed"]),
            verified=bool(data.get("verified", False)),
            metadata=dict(data.get("metadata", {})),
        )


def build_completion(*, reasoning: str, answer: str) -> str:
    """Assemble a completion trace with a single final boxed answer line."""
    body = strip_final_answer_lines(reasoning)
    parts: list[str] = []
    if body:
        parts.append(f"Reasoning:\n{body}")
    parts.append(f"{FINAL_ANSWER_PREFIX}\\boxed{{{answer}}}")
    return "\n\n".join(parts)


def _validate_example_dict(data: dict[str, Any]) -> None:
    if not data.get("verified"):
        raise ValueError(f"{data.get('example_id')}: unverified example rejected")
    completion = build_completion(
        reasoning=str(data.get("reasoning", "")),
        answer=str(data["expected"]),
    )
    if extract_final_boxed_answer(completion) is None:
        raise ValueError(f"{data.get('example_id')}: missing final boxed answer")


@dataclass
class WriteResult:
    """Outcome of writing a synthetic dataset."""

    examples: tuple[SyntheticExample, ...]
    category_counts: dict[str, int]
    rejected_count: int


def write_synthetic_jsonl(
    path: Path,
    raw_examples: list[dict[str, Any]],
    *,
    reject_duplicates: bool = True,
) -> WriteResult:
    """Write verified examples to JSONL in stable sorted order."""
    seen_ids: set[str] = set()
    accepted: list[SyntheticExample] = []
    rejected = 0

    sorted_raw = sorted(raw_examples, key=lambda d: str(d["example_id"]))

    for data in sorted_raw:
        example_id = str(data["example_id"])
        try:
            if reject_duplicates and example_id in seen_ids:
                raise ValueError(f"duplicate example_id: {example_id}")
            _validate_example_dict(data)
            ex = SyntheticExample.from_pre_writer_dict(data)
            seen_ids.add(example_id)
            accepted.append(ex)
        except ValueError:
            rejected += 1

    if rejected > 0:
        raise ValueError(f"rejected {rejected} examples; refusing to write partial dataset")

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for ex in accepted:
            f.write(json.dumps(ex.to_dict(), sort_keys=True) + "\n")

    counts: dict[str, int] = {}
    for ex in accepted:
        counts[ex.category] = counts.get(ex.category, 0) + 1

    return WriteResult(
        examples=tuple(accepted),
        category_counts=counts,
        rejected_count=rejected,
    )


def to_eval_examples(
    examples: list[SyntheticExample],
    *,
    split: str = EVAL_SPLIT_SYNTHETIC_SMOKE,
) -> list[EvaluationExample]:
    """Convert synthetic examples to local eval example records."""
    return [
        EvaluationExample(
            example_id=ex.example_id,
            expected=ex.expected,
            category=ex.category,
            source=ex.source,
            split=split,
            prompt=ex.prompt,
        )
        for ex in examples
    ]


def to_eval_predictions(
    examples: list[SyntheticExample],
    *,
    candidate_id: str = "m03_generated_traces",
) -> list[EvaluationPrediction]:
    """Use generated completions as predictions for factory self-check."""
    return [
        EvaluationPrediction(
            example_id=ex.example_id,
            completion=ex.completion,
            candidate_id=candidate_id,
        )
        for ex in examples
    ]


def write_eval_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    """Write evaluation JSONL rows."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in sorted(rows, key=lambda r: str(r["example_id"])):
            f.write(json.dumps(row, sort_keys=True) + "\n")
