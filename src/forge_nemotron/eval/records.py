"""Evaluation data contracts for local scoring."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

VALID_SPLITS = frozenset(
    {
        "fixture",
        "public_train_holdout",
        "synthetic_balanced_holdout",
        "hard_category_holdout",
        "formatting_edge_holdout",
    }
)


@dataclass(frozen=True)
class EvaluationExample:
    """Ground-truth example for local evaluation."""

    example_id: str
    expected: str
    category: str
    source: str
    split: str
    prompt: str | None = None

    def __post_init__(self) -> None:
        if not self.example_id:
            raise ValueError("example_id is required")
        if not self.category:
            raise ValueError("category is required")
        if self.split not in VALID_SPLITS:
            raise ValueError(f"invalid split: {self.split}")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EvaluationExample:
        return cls(
            example_id=str(data["example_id"]),
            expected=str(data["expected"]),
            category=str(data["category"]),
            source=str(data.get("source", "unknown")),
            split=str(data.get("split", "fixture")),
            prompt=data.get("prompt"),
        )


@dataclass(frozen=True)
class EvaluationPrediction:
    """Model completion for one example."""

    example_id: str
    completion: str
    candidate_id: str | None = None

    def __post_init__(self) -> None:
        if not self.example_id:
            raise ValueError("example_id is required")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EvaluationPrediction:
        return cls(
            example_id=str(data["example_id"]),
            completion=str(data.get("completion", "")),
            candidate_id=data.get("candidate_id"),
        )


@dataclass(frozen=True)
class EvaluationResult:
    """Per-example scoring outcome."""

    example_id: str
    expected: str
    predicted: str | None
    matched: bool
    category: str
    error_type: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "example_id": self.example_id,
            "expected": self.expected,
            "predicted": self.predicted,
            "matched": self.matched,
            "category": self.category,
            "error_type": self.error_type,
        }


@dataclass(frozen=True)
class CategoryScore:
    """Aggregated score for one category."""

    category: str
    total: int
    correct: int

    @property
    def accuracy(self) -> float:
        if self.total == 0:
            return 0.0
        return self.correct / self.total

    def to_dict(self) -> dict[str, float | int | str]:
        return {
            "category": self.category,
            "total": self.total,
            "correct": self.correct,
            "accuracy": self.accuracy,
        }


def validate_unique_example_ids(examples: list[EvaluationExample]) -> None:
    """Raise if example_id values are duplicated."""
    seen: set[str] = set()
    for ex in examples:
        if ex.example_id in seen:
            raise ValueError(f"duplicate example_id: {ex.example_id}")
        seen.add(ex.example_id)
