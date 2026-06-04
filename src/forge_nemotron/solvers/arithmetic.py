"""Arithmetic numeric solver using structured problem dicts (no eval)."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from forge_nemotron.solvers.base import SOLVER_VERSION_ARITHMETIC, SolverResult

CATEGORY_ARITHMETIC = "arithmetic_numeric"


def _solve_add(a: int, b: int) -> tuple[int, str]:
    result = a + b
    reasoning = f"{a} + {b} = {result}."
    return result, reasoning


def _solve_sub(a: int, b: int) -> tuple[int, str]:
    result = a - b
    reasoning = f"{a} - {b} = {result}."
    return result, reasoning


def _solve_mul(a: int, b: int) -> tuple[int, str]:
    result = a * b
    reasoning = f"{a} * {b} = {result}."
    return result, reasoning


def _solve_div(a: int, b: int) -> tuple[int, str]:
    if b == 0:
        raise ValueError("division by zero")
    if a % b != 0:
        raise ValueError("division must yield an integer result")
    result = a // b
    reasoning = f"{a} / {b} = {result}."
    return result, reasoning


def _solve_two_step_add_mul(a: int, b: int, c: int) -> tuple[int, str]:
    inner = a + b
    result = inner * c
    reasoning = f"{a} + {b} = {inner}.\n{inner} * {c} = {result}."
    return result, reasoning


def _compute(operation: str, problem: Mapping[str, Any]) -> tuple[int, str]:
    if operation == "add":
        return _solve_add(int(problem["a"]), int(problem["b"]))
    if operation == "sub":
        return _solve_sub(int(problem["a"]), int(problem["b"]))
    if operation == "mul":
        return _solve_mul(int(problem["a"]), int(problem["b"]))
    if operation == "div":
        return _solve_div(int(problem["a"]), int(problem["b"]))
    if operation == "two_step_add_mul":
        return _solve_two_step_add_mul(
            int(problem["a"]),
            int(problem["b"]),
            int(problem["c"]),
        )
    raise ValueError(f"unsupported arithmetic operation: {operation}")


class ArithmeticSolver:
    """Deterministic solver for bounded integer arithmetic problems."""

    category = CATEGORY_ARITHMETIC

    def solve(self, problem: Mapping[str, Any]) -> SolverResult:
        operation = str(problem.get("operation", ""))
        try:
            result, reasoning = _compute(operation, problem)
        except (KeyError, TypeError, ValueError) as exc:
            return SolverResult(
                answer="",
                reasoning="",
                verified=False,
                category=self.category,
                metadata={
                    "solver_version": SOLVER_VERSION_ARITHMETIC,
                    "error": str(exc),
                },
            )

        return SolverResult(
            answer=str(result),
            reasoning=reasoning,
            verified=True,
            category=self.category,
            metadata={"solver_version": SOLVER_VERSION_ARITHMETIC, "operation": operation},
        )
