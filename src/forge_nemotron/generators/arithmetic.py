"""Deterministic arithmetic problem generator."""

from __future__ import annotations

import random
from typing import Any

from forge_nemotron.generators._trace import build_prompt
from forge_nemotron.solvers.arithmetic import CATEGORY_ARITHMETIC, ArithmeticSolver
from forge_nemotron.solvers.base import SolverResult

GENERATOR_VERSION = "arithmetic_v1"

_OPERATIONS = ("add", "sub", "mul", "div", "two_step_add_mul")


def _sample_problem(rng: random.Random) -> dict[str, Any]:
    op = rng.choice(_OPERATIONS)
    if op == "add":
        a, b = rng.randint(1, 50), rng.randint(1, 50)
        return {"operation": op, "a": a, "b": b}
    if op == "sub":
        a, b = rng.randint(10, 99), rng.randint(1, 49)
        if b > a:
            a, b = b, a
        return {"operation": op, "a": a, "b": b}
    if op == "mul":
        return {"operation": op, "a": rng.randint(2, 12), "b": rng.randint(2, 12)}
    if op == "div":
        b = rng.randint(2, 12)
        quotient = rng.randint(2, 12)
        a = b * quotient
        return {"operation": op, "a": a, "b": b}
    # two_step_add_mul
    a, b, c = rng.randint(1, 20), rng.randint(1, 20), rng.randint(2, 9)
    return {"operation": "two_step_add_mul", "a": a, "b": b, "c": c}


def _problem_to_question(problem: dict[str, Any]) -> str:
    op = problem["operation"]
    if op == "add":
        return f"Compute {problem['a']} + {problem['b']}."
    if op == "sub":
        return f"Compute {problem['a']} - {problem['b']}."
    if op == "mul":
        return f"Compute {problem['a']} * {problem['b']}."
    if op == "div":
        return f"Compute {problem['a']} / {problem['b']}."
    return f"Compute ({problem['a']} + {problem['b']}) * {problem['c']}."


def generate_arithmetic_batch(
    *,
    seed: int,
    count: int,
    id_start: int = 1,
) -> list[dict[str, Any]]:
    """Generate verified arithmetic example dicts (pre-writer)."""
    rng = random.Random(seed)
    solver = ArithmeticSolver()
    batch: list[dict[str, Any]] = []

    for i in range(count):
        problem = _sample_problem(rng)
        result: SolverResult = solver.solve(problem)
        if not result.verified:
            continue
        example_id = f"m03_arithmetic_numeric_{id_start + i:06d}"
        prompt = build_prompt(_problem_to_question(problem))
        batch.append(
            {
                "example_id": example_id,
                "category": CATEGORY_ARITHMETIC,
                "prompt": prompt,
                "reasoning": result.reasoning,
                "expected": result.answer,
                "problem": problem,
                "source": "m03_synthetic",
                "generator_version": GENERATOR_VERSION,
                "solver_version": str(result.metadata.get("solver_version", GENERATOR_VERSION)),
                "seed": seed,
                "verified": True,
                "metadata": dict(result.metadata),
            }
        )

    return batch
