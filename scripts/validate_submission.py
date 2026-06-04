#!/usr/bin/env python3
"""CLI wrapper for submission.zip validation.

Usage:
    python scripts/validate_submission.py path/to/submission.zip
    python scripts/validate_submission.py --json path/to/submission.zip
    python scripts/validate_submission.py --lenient path/to/submission.zip

Or as module:
    python -m forge_nemotron.packaging.validate_submission path/to/submission.zip
"""

from __future__ import annotations

import sys

from forge_nemotron.packaging.validate_submission import main

if __name__ == "__main__":
    sys.exit(main())
