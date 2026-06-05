# Cost Acceptance Update — M11

**Milestone:** M11  
**Prior evidence:** [M08 cost_acceptance_gate.md](../M08/cost_acceptance_gate.md)  
**Policy:** Cost acceptance is owner-declared only — never inferred  
**Does not authorize training**

---

## Cost table

| Compute path | Cost accepted? | Budget / limit | Notes |
| ------------ | -------------- | -------------- | ----- |
| local_5090 | n/a (local hardware) | local electricity/hardware | GPU visible; CUDA PyTorch **unavailable** in active env |
| Modal/Tinker | **TBD** | not recorded | No owner cost acceptance statement |
| Cloud GPU | **TBD** | not recorded | No owner cost acceptance statement |

**Aggregate:** `cost_accepted: false` in readiness manifest.

---

## Owner statement (M11 kickoff)

```text
Paid external compute cost accepted: TBD
Modal/Tinker cost acceptance: TBD
Cloud GPU cost acceptance: TBD
```

Cost acceptance was **not** inferred from RTX 5090 hardware ownership or M11 kickoff authorization.

---

## Non-claims

- No budget ceiling was recorded.
- Paid-path training remains blocked until owner declares cost acceptance.
