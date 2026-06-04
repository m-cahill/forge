"""Tests for string transform solver."""

from __future__ import annotations

from forge_nemotron.solvers.string_transform import StringTransformSolver


def test_reverse() -> None:
    solver = StringTransformSolver()
    result = solver.solve({"operation": "reverse", "text": "ABCA"})
    assert result.verified
    assert result.answer == "ACBA"


def test_rotate_left() -> None:
    solver = StringTransformSolver()
    result = solver.solve({"operation": "rotate_left", "text": "ABCD", "k": 1})
    assert result.verified
    assert result.answer == "BCDA"


def test_rotate_right() -> None:
    solver = StringTransformSolver()
    result = solver.solve({"operation": "rotate_right", "text": "ABCD", "k": 1})
    assert result.verified
    assert result.answer == "DABC"


def test_substitution() -> None:
    solver = StringTransformSolver()
    mapping = {"A": "C", "B": "A", "C": "B"}
    result = solver.solve({"operation": "substitution", "text": "ABCA", "mapping": mapping})
    assert result.verified
    assert result.answer == "CABC"
