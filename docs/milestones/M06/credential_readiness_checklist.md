# Credential Readiness Checklist — M06

**Milestone:** M06  
**Purpose:** Track credential types needed for future training/submit paths  
**No secrets are recorded or committed**

---

| Credential | Needed for | Status | Storage policy |
| ---------- | ---------- | ------ | -------------- |
| Kaggle token | API submission if used | **TBD** | Never commit; Kaggle UI or `~/.kaggle/kaggle.json` |
| Modal token | Baseline upload/training path | **TBD** | Secret manager / local env |
| Tinker key | Tinker training path | **TBD** | Secret manager / local env |
| Cloud GPU creds | Fallback training | **TBD** | Provider vault / local env |

---

## Manifest alignment

| Field | M06 value |
| ----- | --------- |
| `requires_external_credentials` | `true` |
| `required_credentials` | `["modal", "tinker"]` |
| `credentials_ready` | `false` |

---

## Non-claims

- No credentials were committed to the repository in M06.
- Credential **TBD** does not block schema inspection or M06 gate documentation.
