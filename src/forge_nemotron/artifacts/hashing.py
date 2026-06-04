"""Deterministic hashing utilities for evaluation artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    """Return hex SHA256 of file contents (streamed)."""
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    """Return hex SHA256 of UTF-8 text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_json_dumps(obj: Any) -> str:
    """Serialize JSON with stable key order and separators."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(obj: Any) -> str:
    """Return hex SHA256 of canonical JSON representation."""
    return sha256_text(canonical_json_dumps(obj))


def write_json(path: Path, obj: Any) -> None:
    """Write JSON with stable formatting."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json_dumps(obj) + "\n", encoding="utf-8")
