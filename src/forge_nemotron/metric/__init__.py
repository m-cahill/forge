"""FORGE metric utilities for answer extraction and scoring."""

from forge_nemotron.metric.boxed import (
    answers_match,
    extract_boxed_answers,
    extract_final_boxed_answer,
    is_numeric_close,
    normalize_answer,
    score_prediction,
)

__all__ = [
    "extract_boxed_answers",
    "extract_final_boxed_answer",
    "normalize_answer",
    "is_numeric_close",
    "answers_match",
    "score_prediction",
]
