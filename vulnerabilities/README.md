# Vulnerability case studies

> The [main README](../README.md) explains categories before the finding index. The complete **89-entry research catalog**, with CVE references and multiple category tags per scenario, lives in [FINDINGS-INDEX.md](../FINDINGS-INDEX.md).

## Category codes

| Code | Category | Description |
| --- | --- | --- |
| `BD` | Backdoors | Hidden or unauthorized access |
| `RCE` | Remote Code Execution | Remote execution of commands |
| `AUTH` | Authentication & access control | Weak or bypassed identity/permission checks |
| `MIS` | Misconfiguration | Unsafe defaults or security settings |
| `FILE` | File access & sharing | File inclusion, traversal, uploads, shared data |
| `WEB` | Web application | HTTP and application-layer weaknesses |
| `DB` | Database | Database access and unsafe queries |
| `INFO` | Information disclosure | Unwanted release of configuration or data |
| `EOL` | Outdated software | Unsupported or old components needing verification |
| `LPE` | Local privilege escalation | Elevation of local permissions |
| `PROTO` | Weak protocols/cryptography | Cleartext, insecure protocols or keys |
| `INJ` | Injection | Unsafe input influencing a query, command or interpreter |

A finding can have **multiple categories**. For complete descriptions and the full index see [FINDINGS-INDEX.md](../FINDINGS-INDEX.md).

## Dedicated case study index

| Case ID | Research catalog ID | Finding candidate | CVE | Categories | Local status | Case study |
| --- | --- | --- | --- | --- | --- | --- |
| VULN-001 | NET-001 | vsftpd 2.3.4 backdoor | [CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523) | `BD` `RCE` | **Not tested** | [Read case study](VULN-001-vsftpd-backdoor/README.md) |

Only a case being actively investigated needs its own `VULN-###-short-title/` directory. The 89 catalog items are **research candidates, not 89 confirmed findings**.

## Each case study folder

```text
VULN-###-short-name/
├── README.md       # Complete report with catalog ID, CVE/CWE, categories and status
├── scans/          # Raw scan/enum output
├── screenshots/    # Real, numbered supporting evidence
└── scripts/        # Optional original, annotated manual PoC
```

Start from [the vulnerability template](../templates/VULNERABILITY-README-TEMPLATE.md). Record actual dates, commands, output, impact, remediation, and references. Avoid fabricated test results, passwords, tokens, or sensitive content.
