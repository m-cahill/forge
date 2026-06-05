# Cost Acceptance Gate — M08

**Milestone:** M08  
**Purpose:** Record owner cost acceptance before paid external training  
**Does not assume acceptance**

---

## Cost matrix

| Compute path | Cost accepted? | Limit / notes | Owner evidence |
| ------------ | -------------- | ------------- | -------------- |
| local_5090 | **n/a** (local electricity/hardware only) | No cloud meter | Ledger only — not probed |
| Modal/Tinker | **TBD** | Budget/limit not recorded | Owner not supplied in M08 |
| cloud GPU | **TBD** | Budget/limit not recorded | Owner not supplied in M08 |

**Manifest field:** `cost_accepted: false`

---

## Gate rule

Training on paid external paths must not proceed until owner records **yes** with limit/notes in this document (or successor manifest) and updates reproduction plan fields accordingly.

Waivers are **not** applied in M08.

---

## Non-claims

- Cost acceptance is **not** implied by hardware availability or milestone completion.
- No cloud spend occurred in M08.
