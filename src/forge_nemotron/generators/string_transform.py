"""Deterministic string/symbol transform generator (three transform types)."""

from __future__ import annotations

import random
from typing import Any

from forge_nemotron.generators._trace import build_prompt
from forge_nemotron.solvers.base import SolverResult
from forge_nemotron.solvers.string_transform import CATEGORY_STRING, StringTransformSolver

GENERATOR_VERSION = "string_transform_v1"

_SUBSTITUTIONS: tuple[dict[str, str], ...] = (
    {"A": "C", "B": "A", "C": "B"},
    {"X": "Z", "Y": "X", "Z": "Y"},
    {"P": "R", "Q": "P", "R": "Q"},
)

_OPERATIONS = ("reverse", "rotate_left", "rotate_right", "substitution")


def _sample_text(rng: random.Random) -> str:
    length = rng.randint(3, 6)
    return "".join(rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(length))


def _sample_problem(rng: random.Random) -> dict[str, Any]:
    op = rng.choice(_OPERATIONS)
    text = _sample_text(rng)
    if op == "reverse":
        return {"operation": op, "text": text}
    if op in ("rotate_left", "rotate_right"):
        k = rng.randint(1, max(1, len(text) - 1))
        return {"operation": op, "text": text, "k": k}
    mapping = rng.choice(_SUBSTITUTIONS)
    # Use characters present in mapping keys where possible
    chars = [c for c in text if c in mapping] or list(mapping.keys())[: len(text)]
    if len(chars) < 3:
        chars = list(mapping.keys())[:3]
    text = "".join(chars[: rng.randint(3, min(5, len(chars)))])
    return {"operation": "substitution", "text": text, "mapping": dict(mapping)}


def _mapping_description(mapping: dict[str, str]) -> str:
    pairs = ", ".join(f"{k}→{v}" for k, v in sorted(mapping.items()))
    return pairs


def _problem_to_question(problem: dict[str, Any]) -> str:
    op = problem["operation"]
    text = problem["text"]
    if op == "reverse":
        return f"Reverse the string {text}."
    if op == "rotate_left":
        return f"Rotate {text} left by {problem['k']} positions."
    if op == "rotate_right":
        return f"Rotate {text} right by {problem['k']} positions."
    mapping = problem["mapping"]
    return f"Apply the mapping {_mapping_description(mapping)} to {text}."


def generate_string_transform_batch(
    *,
    seed: int,
    count: int,
    id_start: int = 1,
) -> list[dict[str, Any]]:
    """Generate verified string transform example dicts (pre-writer)."""
    rng = random.Random(seed + 10_000)
    solver = StringTransformSolver()
    batch: list[dict[str, Any]] = []

    for i in range(count):
        problem = _sample_problem(rng)
        result: SolverResult = solver.solve(problem)
        if not result.verified:
            continue
        example_id = f"m03_string_symbol_transform_{id_start + i:06d}"
        prompt = build_prompt(_problem_to_question(problem))
        batch.append(
            {
                "example_id": example_id,
                "category": CATEGORY_STRING,
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
