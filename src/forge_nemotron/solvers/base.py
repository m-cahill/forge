"""Solver protocol and result types for verified synthetic examples."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Protocol, runtime_checkable

SOLVER_VERSION_ARITHMETIC = "arithmetic_v1"
SOLVER_VERSION_STRING_TRANSFORM = "string_transform_v1"


@dataclass(frozen=True)
class SolverResult:
    """Outcome of solving a structured problem dict."""

    answer: str
    reasoning: str
    verified: bool
    category: str
    metadata: dict[str, str | int | float | bool]

    def __post_init__(self) -> None:
        if not self.category:
            raise ValueError("category is required")


@runtime_checkable
class Solver(Protocol):
    """Protocol for category-specific deterministic solvers."""

    category: str

    def solve(self, problem: Mapping[str, Any]) -> SolverResult:
        """Return verified answer and reasoning steps (without final boxing)."""
        ...
