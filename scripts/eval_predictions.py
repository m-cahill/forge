#!/usr/bin/env python3
"""CLI wrapper for local prediction evaluation.

Usage:
    python scripts/eval_predictions.py \\
        --examples tests/fixtures/eval/examples.jsonl \\
        --predictions tests/fixtures/eval/predictions_mixed.jsonl \\
        --out artifacts/runs/m02_fixture_eval/local_eval.json \\
        --by-category artifacts/runs/m02_fixture_eval/local_eval_by_category.csv \\
        --failures artifacts/runs/m02_fixture_eval/examples_failed.jsonl \\
        --manifest artifacts/runs/m02_fixture_eval/run_manifest.json

Or as module:
    python -m forge_nemotron.eval.scorer --help
"""

from __future__ import annotations

import sys

from forge_nemotron.eval.scorer import main

if __name__ == "__main__":
    sys.exit(main())
