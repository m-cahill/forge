"""Shared trace formatting helpers for generators."""

from __future__ import annotations

FINAL_ANSWER_PREFIX = "Final answer: "


def build_prompt(question: str) -> str:
    """Format a question line for synthetic prompts."""
    return f"Question: {question}"


def strip_final_answer_lines(reasoning: str) -> str:
    """Remove trailing final-answer lines from reasoning (writer owns boxing)."""
    lines = reasoning.splitlines()
    while lines and lines[-1].strip().lower().startswith("final answer"):
        lines.pop()
    return "\n".join(lines).strip()
