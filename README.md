# Metasploitable 2 — Vulnerability Assessment & Penetration Testing Lab

> A documented, hands-on penetration testing portfolio project using **Kali Linux**, **Metasploitable 2**, **Metasploit Framework**, and **manual validation** in an isolated virtual lab.

**Project status:** Lab setup / testing not yet documented  
**Target:** Metasploitable 2 (intentionally vulnerable VM)  
**Attacker:** Kali Linux  
**Environment:** VirtualBox isolated Internal Network or Host-Only Adapter  
**Maintainer:** [AazafRitha](https://github.com/AazafRitha)

> [!IMPORTANT]
> This repository documents **authorized training against my own Metasploitable 2 VM only**. No public IP addresses, third-party systems, or production services are in scope. See [SCOPE.md](SCOPE.md).

## Project goals

- Practice the complete VAPT lifecycle: **reconnaissance → enumeration → validation → controlled exploitation → impact verification → reporting**.
- Compare **Metasploit-assisted** exploitation with **manual testing** when appropriate.
- Collect reproducible commands, raw scan outputs, screenshots, and notes.
- Publish **one self-contained folder and technical report per tested vulnerability**.
- Produce a consolidated, professional penetration testing report once testing is complete.

## Lab architecture

```text
              Isolated VirtualBox Lab Network
    ┌────────────────────────┐    ┌────────────────────────┐
    │ Kali Linux             │    │ Metasploitable 2        │
    │ Attacker / test VM     │───▶│ Intentionally vulnerable│
    │ IP: record after setup │    │ IP: record after setup  │
    └────────────────────────┘    └────────────────────────┘
```

Use **Internal Network** for strong VM-to-VM isolation or a carefully configured **Host-Only** network. **Do not bridge Metasploitable 2 to a physical network or expose its ports to the internet.** See [lab setup](lab-setup/README.md).

## Repository layout

```text
metasploitable2-vapt-lab/
├── README.md                          # Project overview and findings index
├── SCOPE.md                           # Authorization, boundaries, rules of engagement
├── CHECKLIST.md                       # Progress tracking
├── .gitignore                         # Excludes secrets and temporary files
├── lab-setup/
│   ├── README.md                      # Network and VM setup
│   └── scans/                         # Initial network/baseline scans
├── methodology/
│   └── README.md                      # Repeatable testing methodology
├── templates/
│   ├── VULNERABILITY-README-TEMPLATE.md
│   └── FINAL-REPORT-TEMPLATE.md
├── vulnerabilities/
│   ├── README.md                      # Vulnerability index / conventions
│   └── VULN-001-vsftpd-backdoor/
│       ├── README.md                  # Case-study report (initially not tested)
│       ├── scans/                     # Service-specific scan results
│       ├── screenshots/               # Screenshots and proof
│       └── scripts/                   # Original/manual PoCs, if needed
└── reports/
    └── README.md                      # Consolidated final report location
```

Create additional `VULN-###-short-name/` folders **only when starting an actual testing case**, using the reusable [finding template](templates/VULNERABILITY-README-TEMPLATE.md).

## Testing workflow

1. **Prepare** — isolate both VMs, verify IP addresses, take a target snapshot.
2. **Discover** — run scoped host/service scans and preserve raw output.
3. **Enumerate** — inspect the affected service and record observations.
4. **Validate** — review advisories and confirm the issue with evidence; never rely only on a version banner.
5. **Exploit safely** — test with Metasploit and/or a documented manual method if suitable.
6. **Verify impact** — use minimal, non-destructive commands and record actual privileges and results.
7. **Report** — explain root cause, prerequisites, risk, remediation, and limits.
8. **Reset** — restore the snapshot if needed, and commit sanitized evidence.

See [methodology](methodology/README.md) for reporting rules and the verification checklist.

## Findings index

The following is a **planned lab exercise, not a confirmed finding**. Its status must change only after testing.

| ID | Candidate scenario | Status | Case study |
| --- | --- | --- | --- |
| VULN-001 | vsftpd 2.3.4 backdoor (CVE-2011-2523) | **Not tested** | [Open](vulnerabilities/VULN-001-vsftpd-backdoor/README.md) |

More rows will be added as testing progresses. Do not assign a severity or claim exploitation until supporting evidence is collected.

## What each vulnerability folder contains

- `README.md` — overview, affected asset, reproduction steps, Metasploit/manual approaches, observed results, impact, remediation, references.
- `scans/` — raw output (for example `nmap` or `nc` logs); remove unrelated or sensitive information.
- `screenshots/` — numbered images that correspond to steps in the report.
- `scripts/` — optional, original PoC scripts with clear purpose and usage notes.

**Evidence naming example:** `01-service-discovery.png`, `02-module-options.png`, `03-impact-verification.png`. Show commands and outputs in the report; link evidence with relative paths.

## Quick start

1. Read [SCOPE.md](SCOPE.md) and [lab-setup/README.md](lab-setup/README.md).
2. Record the actual IPs from both VMs (examples in the guide are placeholders).
3. Confirm Kali can reach only the intended target on the isolated lab network.
4. Run scoped baseline scans and save them under `lab-setup/scans/`.
5. Open the [first candidate case](vulnerabilities/VULN-001-vsftpd-backdoor/README.md) and update it **only with observed results**.
6. Track progress in [CHECKLIST.md](CHECKLIST.md).

## Tools

Kali Linux · VirtualBox · Nmap · Netcat · Metasploit Framework · Burp Suite (web scenarios) · Git/GitHub · Markdown.

Tools are used only when appropriate to a particular finding; the presence of a tool here does not indicate it has been run.

## Reporting deliverables

- [Individual technical case studies](vulnerabilities/README.md)
- [Raw baseline evidence](lab-setup/README.md)
- [Consolidated VAPT report folder](reports/README.md)
- [Final report template](templates/FINAL-REPORT-TEMPLATE.md)

## Ethics and reproducibility

This is an educational lab, not a guide to attack systems without authorization. Use fictional/sample data, avoid destructive payloads and persistence, and never commit credentials, private keys, session tokens, or sensitive files. Screenshots and logs are sanitized before publishing. Actual test dates, target addresses, tool versions, exploit results, and limitations must be recorded at the time of testing.
