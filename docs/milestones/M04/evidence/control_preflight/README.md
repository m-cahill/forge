# M04 Control Preflight Evidence

**Milestone:** M04  
**Purpose:** Validate adapter candidate manifest schema and promotion preflight gates.

---

## What this is

| Item | Value |
| ---- | ----- |
| File | `control_candidate_manifest.preflight.json` |
| Status | `preflight` |
| Candidate ID | `control_public_repro_preflight` |

---

## What this is NOT

- **Not** a trained adapter
- **Not** a `submission.zip` package
- **Not** a Kaggle-ready candidate
- **Not** submitted to Kaggle
- **Not** a public or private leaderboard score
- **Not** evidence of public baseline reproduction

This manifest exists only to exercise `validate_candidate_manifest` and document required fields for future real candidates.

---

## Validation

```bash
python scripts/validate_candidate_manifest.py docs/milestones/M04/evidence/control_preflight/control_candidate_manifest.preflight.json
```

Expected: exit code 0, no errors.
