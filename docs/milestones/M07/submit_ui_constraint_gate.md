# Submit UI Constraint Gate

**Milestone:** M07  
**Purpose:** Record Kaggle Submit UI constraints affecting `submission.zip` — separate from training authorization

---

## Current status (owner-action)

```text
Submit UI submission.zip constraints/warnings: OPEN — owner-action / not recorded
Kaggle API submission support: TBD
```

No new Submit UI evidence was supplied for M07. **Do not guess** zip size limits, file warnings, or API behavior.

---

## Decision

| Question | Answer |
| -------- | ------ |
| Does open Submit UI constraint block M07 training gate docs? | **No** |
| Does open Submit UI constraint block Kaggle submission? | **Yes** — until recorded and validated |
| Does open Submit UI constraint block Gate C training authorization? | **No** by itself — training blocked for other reasons (`M07_TRAINING_AUTHORIZED = no`) |

---

## Known facts (from prior milestones)

| Fact | Source |
| ---- | ------ |
| Rules accepted / team joined | Owner 2026-06-04 — M01 intake |
| Submit UI accessible | M01 |
| Daily submission limit | **5 per day** — M01 probe |
| Zip constraints / warnings | **not recorded** |

Evidence: [`docs/kaggle/kaggle_setup_evidence.md`](../../kaggle/kaggle_setup_evidence.md)

---

## When owner supplies constraints

Update this document and `docs/kaggle/kaggle_setup_evidence.md` with:

- max zip size (if shown),
- required files / warnings,
- UI text or screenshot reference (no secrets),
- date verified.

---

## Non-claims

- No Kaggle submission attempted in M07.
- No package validity claim without validator pass on a real adapter zip.
