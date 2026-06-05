# Credential Readiness Evidence — M08

**Milestone:** M08  
**Storage policy:** Never commit tokens, `.env`, or secrets  
**Does not authorize training**

---

## Credential matrix

| Credential / account | Needed for | Status | Evidence | Storage policy |
| -------------------- | ---------- | ------ | -------- | -------------- |
| Modal | baseline-compatible training/upload | **TBD** | Owner statement not supplied in M08 | never commit |
| Tinker | baseline-compatible training | **TBD** | Owner statement not supplied in M08 | never commit |
| Kaggle API | possible submission automation | **TBD** | Owner statement not supplied in M08 | never commit |
| Cloud GPU | fallback training | **TBD** | Owner statement not supplied in M08 | never commit |

**Aggregate:** `credentials_ready: false` (manifest and M07 carry-forward)

---

## Required credential names (manifest)

Per reproduction plan contract: `modal`, `tinker` when `requires_external_credentials: true`.

---

## Owner actions (not performed in M08)

1. Confirm whether Modal account exists and is usable for baseline-compatible workflows.
2. Confirm whether Tinker account exists and is usable.
3. Confirm Kaggle API token availability (submission automation only — separate from rules/team eligibility).
4. Record readiness as `ready` / `blocked` / **TBD** with date — **no secrets**.

---

## Non-claims

- FORGE does not claim any external account exists or works.
- M08 does not store, print, or request credential material in the repo.
