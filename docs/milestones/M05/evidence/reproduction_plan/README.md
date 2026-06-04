# Reproduction Plan Preflight Evidence

**Milestone:** M05  
**Status:** Preflight plan only — **not training authorization**

---

## Contents

| File | Purpose |
| ---- | ------- |
| `public_control_repro_plan.preflight.json` | Mock reproduction plan for schema and validator testing |

---

## Non-claims

This evidence is **preflight-only**. It does **not** represent:

- Training authorization
- Baseline reproduction
- Adapter or package evidence
- Kaggle-ready submission
- Public or private leaderboard score

Validate with:

```bash
python scripts/validate_reproduction_plan.py docs/milestones/M05/evidence/reproduction_plan/public_control_repro_plan.preflight.json
```

---

## Guardrails

- `training_authorized` is **false**
- `kaggle_submission_authorized` is **false**
- `copying_policy` is **no_code_copy**
- No baseline code or data is committed in this directory
