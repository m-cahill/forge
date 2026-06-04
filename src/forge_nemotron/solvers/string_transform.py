"""String and symbol transformation solver (structured problems only)."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from forge_nemotron.solvers.base import SOLVER_VERSION_STRING_TRANSFORM, SolverResult

CATEGORY_STRING = "string_symbol_transform"

_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def _apply_substitution(text: str, mapping: Mapping[str, str]) -> tuple[str, str]:
    lines: list[str] = []
    out_chars: list[str] = []
    for ch in text:
        if ch in mapping:
            mapped = mapping[ch]
            lines.append(f"{ch} maps to {mapped}.")
            out_chars.append(mapped)
        else:
            out_chars.append(ch)
            lines.append(f"{ch} is unchanged.")
    return "".join(out_chars), "\n".join(lines)


def _reverse(text: str) -> tuple[str, str]:
    result = text[::-1]
    reasoning = f"Reverse the string character by character to get {result}."
    return result, reasoning


def _rotate_left(text: str, k: int) -> tuple[str, str]:
    if not text:
        return "", "Empty string remains empty."
    k = k % len(text)
    result = text[k:] + text[:k]
    reasoning = f"Rotate left by {k}: {result}."
    return result, reasoning


def _rotate_right(text: str, k: int) -> tuple[str, str]:
    if not text:
        return "", "Empty string remains empty."
    k = k % len(text)
    result = text[-k:] + text[:-k]
    reasoning = f"Rotate right by {k}: {result}."
    return result, reasoning


class StringTransformSolver:
    """Solver for reverse, rotate, and substitution transforms."""

    category = CATEGORY_STRING

    def solve(self, problem: Mapping[str, Any]) -> SolverResult:
        operation = str(problem.get("operation", ""))
        try:
            text = str(problem["text"])
            if operation == "reverse":
                result, reasoning = _reverse(text)
            elif operation == "rotate_left":
                result, reasoning = _rotate_left(text, int(problem["k"]))
            elif operation == "rotate_right":
                result, reasoning = _rotate_right(text, int(problem["k"]))
            elif operation == "substitution":
                raw_map = problem["mapping"]
                if not isinstance(raw_map, Mapping):
                    raise ValueError("mapping must be a mapping")
                mapping = {str(k): str(v) for k, v in raw_map.items()}
                result, reasoning = _apply_substitution(text, mapping)
            else:
                raise ValueError(f"unsupported transform: {operation}")
        except (KeyError, TypeError, ValueError) as exc:
            return SolverResult(
                answer="",
                reasoning="",
                verified=False,
                category=self.category,
                metadata={
                    "solver_version": SOLVER_VERSION_STRING_TRANSFORM,
                    "error": str(exc),
                },
            )

        return SolverResult(
            answer=result,
            reasoning=reasoning,
            verified=True,
            category=self.category,
            metadata={
                "solver_version": SOLVER_VERSION_STRING_TRANSFORM,
                "operation": operation,
            },
        )
