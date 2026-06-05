# M08 Readiness Manifest Evidence

**File:** `public_control_repro_plan.readiness.json`  
**Plan ID:** `public_control_repro_plan_readiness_v1`

## Purpose

Documents compute/credential/cost/submission readiness for Gate C evaluation. **Not** training authorization.

## Key fields

| Field | M08 value |
| ----- | --------- |
| `training_authorized` | `false` |
| `ready_for_training` | `false` |
| `credentials_ready` | `false` |
| `cost_accepted` | `false` |
| `compute_path` | `null` |

## Validate

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M08/evidence/readiness/public_control_repro_plan.readiness.json
```

## Non-claims

Not trained, not submitted, not reproduced. No hardware probe evidence in M08 (probe script not executed).
