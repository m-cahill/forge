"""Formatting stress generator for final \\boxed{} trace conventions."""

from __future__ import annotations

import random
from typing import Any

from forge_nemotron.generators._trace import build_prompt, strip_final_answer_lines
from forge_nemotron.generators.arithmetic import _problem_to_question as arith_question
from forge_nemotron.generators.arithmetic import _sample_problem as sample_arith
from forge_nemotron.generators.string_transform import _problem_to_question as str_question
from forge_nemotron.generators.string_transform import _sample_problem as sample_string
from forge_nemotron.solvers.arithmetic import ArithmeticSolver
from forge_nemotron.solvers.string_transform import StringTransformSolver

GENERATOR_VERSION = "formatting_stress_v1"
CATEGORY_FORMATTING = "formatting_stress"

_TEMPLATES = (
    "early_unboxed",
    "multiple_boxed",
    "whitespace_answer",
    "string_answer",
    "numeric_answer",
)


def _wrap_reasoning(template: str, reasoning: str, answer: str) -> str:
    base = strip_final_answer_lines(reasoning)
    if template == "early_unboxed":
        return f"A draft value might be {answer}, but we verify below.\n{base}"
    if template == "multiple_boxed":
        return f"Intermediate \\boxed{{wrong}}.\n{base}\nAnother \\boxed{{also_wrong}}."
    if template == "whitespace_answer":
        return f"{base}\n(The final value has surrounding spaces in the prompt only.)"
    if template == "string_answer":
        return base
    return base


def generate_formatting_stress_batch(
    *,
    seed: int,
    count: int,
    id_start: int = 1,
) -> list[dict[str, Any]]:
    """Generate formatting-stress examples using verified arithmetic/string solves."""
    rng = random.Random(seed + 20_000)
    arith_solver = ArithmeticSolver()
    str_solver = StringTransformSolver()
    batch: list[dict[str, Any]] = []

    for i in range(count):
        template = _TEMPLATES[i % len(_TEMPLATES)]
        use_arith = rng.random() < 0.5
        if use_arith:
            problem = sample_arith(rng)
            result = arith_solver.solve(problem)
            question = arith_question(problem)
            solver_version = "arithmetic_v1"
        else:
            problem = sample_string(rng)
            result = str_solver.solve(problem)
            question = str_question(problem)
            solver_version = "string_transform_v1"

        if not result.verified:
            continue

        reasoning = _wrap_reasoning(template, result.reasoning, result.answer)
        example_id = f"m03_formatting_stress_{id_start + i:06d}"
        batch.append(
            {
                "example_id": example_id,
                "category": CATEGORY_FORMATTING,
                "prompt": build_prompt(question),
                "reasoning": reasoning,
                "expected": result.answer,
                "problem": problem,
                "source": "m03_synthetic",
                "generator_version": GENERATOR_VERSION,
                "solver_version": solver_version,
                "seed": seed,
                "verified": True,
                "metadata": {
                    "template": template,
                    "solver_version": solver_version,
                },
            }
        )

    return batch
