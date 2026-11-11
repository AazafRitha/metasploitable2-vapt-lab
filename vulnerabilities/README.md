# Vulnerability case studies

Every tested issue receives **one self-contained folder** named `VULN-###-short-description/`.

## Required structure

```text
VULN-###-short-description/
├── README.md       # Complete technical finding: all steps, observations, impact, remediation
├── scans/          # Service-specific raw scan/enum output
├── screenshots/    # Numbered evidence files
└── scripts/        # Optional original, annotated manual PoC
```

Copy [the vulnerability template](../templates/VULNERABILITY-README-TEMPLATE.md), and retain only the sections relevant to the tested issue.

## Current case studies

| ID | Candidate | Status | Report |
| --- | --- | --- | --- |
| VULN-001 | vsftpd backdoor | Not tested | [VULN-001](VULN-001-vsftpd-backdoor/README.md) |

**Reminder:** A named exercise is not an evidence-backed finding until actual lab testing is recorded. Do not copy example tool output or screenshots and label them as observed.
