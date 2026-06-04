"""Tests for solver base types."""

from __future__ import annotations

import pytest

from forge_nemotron.solvers.base import SolverResult


def test_solver_result_immutable() -> None:
    result = SolverResult(
        answer="42",
        reasoning="step",
        verified=True,
        category="arithmetic_numeric",
        metadata={"solver_version": "arithmetic_v1"},
    )
    with pytest.raises(AttributeError):
        result.answer = "0"  # type: ignore[misc]


def test_solver_result_requires_category() -> None:
    with pytest.raises(ValueError, match="category"):
        SolverResult(
            answer="x",
            reasoning="",
            verified=True,
            category="",
            metadata={},
        )
