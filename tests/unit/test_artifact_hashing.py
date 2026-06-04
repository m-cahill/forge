"""Unit tests for artifact hashing utilities."""

from __future__ import annotations

from pathlib import Path

from forge_nemotron.artifacts.hashing import (
    canonical_json_dumps,
    sha256_file,
    sha256_json,
    sha256_text,
)


class TestArtifactHashing:
    def test_sha256_text_stable(self) -> None:
        a = sha256_text("hello")
        b = sha256_text("hello")
        assert a == b
        assert len(a) == 64

    def test_canonical_json_key_order_independent(self) -> None:
        obj_a = {"b": 2, "a": 1}
        obj_b = {"a": 1, "b": 2}
        assert sha256_json(obj_a) == sha256_json(obj_b)
        assert canonical_json_dumps(obj_a) == canonical_json_dumps(obj_b)

    def test_sha256_file_fixture(self, tmp_path: Path) -> None:
        path = tmp_path / "hash_me.txt"
        path.write_bytes(b"fixture-bytes\n")
        digest = sha256_file(path)
        assert digest == sha256_text("fixture-bytes\n")
