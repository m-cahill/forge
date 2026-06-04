"""Boxed answer extraction and scoring for the Nemotron reasoning challenge.

This module extracts final answers from LaTeX \boxed{...} expressions and
compares them against expected answers using exact string matching or
numeric tolerance.

The competition requires models to emit final answers in \boxed{...} format.
This module provides deterministic extraction without using eval() or
executing arbitrary code.

Behavior notes:
- Multiple \boxed{} occurrences: the LAST valid box is used as the final answer
- Nested braces: basic support for one level of nesting (e.g., \boxed{f(x)})
- Malformed boxes: gracefully handled, return None or empty list
- Whitespace: normalized in answers (stripped, collapsed)
- Numeric comparison: optional tolerance for floating-point answers
"""

from __future__ import annotations

import math
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

# Pattern to match \boxed{...} with basic brace balancing
# This handles simple nesting like \boxed{f(x)} but not arbitrarily deep nesting
_BOXED_PATTERN = re.compile(
    r"\\boxed\s*\{",
    re.DOTALL,
)


def _find_matching_brace(text: str, start: int) -> int | None:
    """Find the position of the closing brace that matches the opening brace.

    Args:
        text: The full text to search
        start: Position of the opening brace

    Returns:
        Position of the matching closing brace, or None if not found
    """
    if start >= len(text) or text[start] != "{":
        return None

    depth = 1
    pos = start + 1

    while pos < len(text) and depth > 0:
        char = text[pos]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "\\" and pos + 1 < len(text):
            # Skip escaped characters
            pos += 1
        pos += 1

    if depth == 0:
        return pos - 1
    return None


def extract_boxed_answers(text: str) -> list[str]:
    """Extract all boxed answers from text.

    Args:
        text: Model output text potentially containing \boxed{...} expressions

    Returns:
        List of answer strings extracted from all \boxed{} occurrences,
        in order of appearance. Empty list if no valid boxes found.

    Examples:
        >>> extract_boxed_answers("The answer is \\boxed{42}")
        ['42']
        >>> extract_boxed_answers("First \\boxed{1}, then \\boxed{2}")
        ['1', '2']
        >>> extract_boxed_answers("No boxes here")
        []
    """
    if not text:
        return []

    answers: list[str] = []

    for match in _BOXED_PATTERN.finditer(text):
        # Find the opening brace position
        brace_start = match.end() - 1
        brace_end = _find_matching_brace(text, brace_start)

        if brace_end is not None:
            # Extract content between braces (exclusive)
            content = text[brace_start + 1 : brace_end]
            answers.append(content)

    return answers


def extract_final_boxed_answer(text: str) -> str | None:
    """Extract the final (last) boxed answer from text.

    Per competition convention, if multiple \boxed{} expressions exist,
    the final one is considered the definitive answer.

    Args:
        text: Model output text potentially containing \boxed{...} expressions

    Returns:
        The content of the last \boxed{} expression, or None if no valid box found.

    Examples:
        >>> extract_final_boxed_answer("First \\boxed{1}, final \\boxed{42}")
        '42'
        >>> extract_final_boxed_answer("No answer here")
        None
    """
    answers = extract_boxed_answers(text)
    return answers[-1] if answers else None


def normalize_answer(answer: str) -> str:
    """Normalize an answer string for comparison.

    Applies the following normalizations:
    - Strip leading/trailing whitespace
    - Collapse multiple internal spaces to single space
    - Convert to lowercase for case-insensitive comparison

    Note: The competition may use exact matching, so this is configurable.
    For numeric comparisons, use is_numeric_close() instead.

    Args:
        answer: Raw answer string

    Returns:
        Normalized answer string
    """
    if not answer:
        return ""

    # Strip and collapse whitespace
    normalized = " ".join(answer.split())
    return normalized


def _try_parse_number(s: str) -> float | None:
    """Attempt to parse a string as a number.

    Handles:
    - Integers: 42, -42
    - Floats: 3.14, -2.5, .5
    - Scientific notation: 1e10, 2.5e-3
    - Fractions written as a/b (simple cases)

    Does NOT use eval() for safety.

    Args:
        s: String to parse

    Returns:
        Parsed float value, or None if not parseable as number
    """
    if not s:
        return None

    s = s.strip()

    # Handle simple fractions like "1/2"
    if "/" in s and s.count("/") == 1:
        parts = s.split("/")
        try:
            num = float(parts[0].strip())
            den = float(parts[1].strip())
            if den != 0:
                return num / den
        except (ValueError, ZeroDivisionError):
            pass
        return None

    # Try direct float parsing
    try:
        return float(s)
    except ValueError:
        return None


def is_numeric_close(
    predicted: str,
    expected: str,
    rel_tol: float = 1e-4,
    abs_tol: float = 1e-8,
) -> bool:
    """Check if two answers are numerically close.

    Both strings must parse as numbers. If either fails to parse,
    returns False (use answers_match for string comparison instead).

    Args:
        predicted: Predicted answer string
        expected: Expected answer string
        rel_tol: Relative tolerance (default 1e-4)
        abs_tol: Absolute tolerance (default 1e-8)

    Returns:
        True if both parse as numbers and are within tolerance

    Examples:
        >>> is_numeric_close("3.14159", "3.1416")
        True
        >>> is_numeric_close("42", "42.0")
        True
        >>> is_numeric_close("1/2", "0.5")
        True
        >>> is_numeric_close("abc", "123")
        False
    """
    pred_num = _try_parse_number(predicted)
    exp_num = _try_parse_number(expected)

    if pred_num is None or exp_num is None:
        return False

    return math.isclose(pred_num, exp_num, rel_tol=rel_tol, abs_tol=abs_tol)


def answers_match(
    predicted: str,
    expected: str,
    *,
    normalize: bool = True,
    try_numeric: bool = True,
    case_sensitive: bool = False,
    rel_tol: float = 1e-4,
    abs_tol: float = 1e-8,
) -> bool:
    """Check if predicted answer matches expected answer.

    Attempts matching in this order:
    1. If try_numeric=True, try numeric comparison first
    2. Fall back to string comparison (with optional normalization)

    Args:
        predicted: Predicted answer string
        expected: Expected answer string
        normalize: Whether to normalize whitespace (default True)
        try_numeric: Whether to try numeric comparison (default True)
        case_sensitive: Whether string comparison is case-sensitive (default False)
        rel_tol: Relative tolerance for numeric comparison
        abs_tol: Absolute tolerance for numeric comparison

    Returns:
        True if answers match

    Examples:
        >>> answers_match("42", "42")
        True
        >>> answers_match("  42  ", "42")
        True
        >>> answers_match("ANSWER", "answer")
        True
        >>> answers_match("3.14159", "3.1416", try_numeric=True)
        True
    """
    # Handle None/empty cases
    if predicted is None or expected is None:
        return predicted == expected
    if not predicted and not expected:
        return True
    if not predicted or not expected:
        return False

    # Try numeric comparison first if enabled
    if try_numeric:
        if is_numeric_close(predicted, expected, rel_tol=rel_tol, abs_tol=abs_tol):
            return True

    # Fall back to string comparison
    pred_str = predicted
    exp_str = expected

    if normalize:
        pred_str = normalize_answer(pred_str)
        exp_str = normalize_answer(exp_str)

    if not case_sensitive:
        pred_str = pred_str.lower()
        exp_str = exp_str.lower()

    return pred_str == exp_str


def score_prediction(
    completion: str,
    expected: str,
    *,
    normalize: bool = True,
    try_numeric: bool = True,
    case_sensitive: bool = False,
    rel_tol: float = 1e-4,
    abs_tol: float = 1e-8,
) -> bool:
    """Score a model completion against an expected answer.

    Extracts the final \boxed{} answer from the completion and compares
    it to the expected answer.

    Args:
        completion: Full model output text
        expected: Expected answer (not boxed)
        normalize: Whether to normalize whitespace
        try_numeric: Whether to try numeric comparison
        case_sensitive: Whether string comparison is case-sensitive
        rel_tol: Relative tolerance for numeric comparison
        abs_tol: Absolute tolerance for numeric comparison

    Returns:
        True if the extracted answer matches expected

    Examples:
        >>> score_prediction("The answer is \\boxed{42}", "42")
        True
        >>> score_prediction("Therefore, \\boxed{3.14159}", "3.1416")
        True
        >>> score_prediction("No box here", "42")
        False
    """
    extracted = extract_final_boxed_answer(completion)

    if extracted is None:
        return False

    return answers_match(
        extracted,
        expected,
        normalize=normalize,
        try_numeric=try_numeric,
        case_sensitive=case_sensitive,
        rel_tol=rel_tol,
        abs_tol=abs_tol,
    )
