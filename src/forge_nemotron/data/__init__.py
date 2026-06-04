"""Dataset writing, manifests, and synthetic example contracts."""

from forge_nemotron.data.manifest import build_dataset_manifest
from forge_nemotron.data.synthetic import (
    SyntheticExample,
    build_completion,
    to_eval_examples,
    to_eval_predictions,
    write_synthetic_jsonl,
)

__all__ = [
    "SyntheticExample",
    "build_completion",
    "build_dataset_manifest",
    "to_eval_examples",
    "to_eval_predictions",
    "write_synthetic_jsonl",
]
