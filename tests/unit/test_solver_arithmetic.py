"""Tests for arithmetic solver."""

from __future__ import annotations

import ast
from pathlib import Path

from forge_nemotron.solvers.arithmetic import ArithmeticSolver


def test_addition() -> None:
    solver = ArithmeticSolver()
    result = solver.solve({"operation": "add", "a": 7, "b": 5})
    assert result.verified
    assert result.answer == "12"


def test_two_step_expression() -> None:
    solver = ArithmeticSolver()
    result = solver.solve({"operation": "two_step_add_mul", "a": 7, "b": 5, "c": 3})
    assert result.verified
    assert result.answer == "36"
    assert "7 + 5 = 12" in result.reasoning


def test_division_exact() -> None:
    solver = ArithmeticSolver()
    result = solver.solve({"operation": "div", "a": 24, "b": 6})
    assert result.verified
    assert result.answer == "4"


def test_division_by_zero_unverified() -> None:
    solver = ArithmeticSolver()
    result = solver.solve({"operation": "div", "a": 1, "b": 0})
    assert not result.verified


def test_no_eval_in_solver_module() -> None:
    import forge_nemotron.solvers.arithmetic as arith_mod

    path = arith_mod.__file__
    assert path is not None
    source = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(source)
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    assert "eval" not in names
    assert "exec" not in names
    assert "literal_eval" not in names
