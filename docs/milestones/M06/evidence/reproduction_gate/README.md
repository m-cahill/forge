# M06 Reproduction Gate Evidence

**Plan ID:** `public_control_repro_plan_schema_gate_v1`  
**Status:** Schema gate only — **not** training authorization

| File | Purpose |
| ---- | ------- |
| `public_control_repro_plan.schema_gate.json` | M06 schema-inspected reproduction gate manifest |

**Non-claims:** `not_trained`, `not_submitted`, `not_reproduced`. No baseline reproduction or adapter package.

Validate:

```bash
python scripts/validate_reproduction_plan.py \
  docs/milestones/M06/evidence/reproduction_gate/public_control_repro_plan.schema_gate.json
```
