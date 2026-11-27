# Metasploitable 2 — VAPT Lab

**Kali Linux + Metasploitable 2 | Metasploit and manual penetration testing | Professional reports**

![Isolated VirtualBox lab: Kali Linux and Metasploitable 2](assets/lab-architecture.svg)

A hands-on cybersecurity project where I discover, validate, and document vulnerabilities in **my own isolated Metasploitable 2 VM**. Each tested vulnerability gets **one folder and one complete README report**, with scan results and screenshots.

> **Current status:** Repository organized. Lab scans and exploits **not yet documented**. The 89 catalog entries are research candidates, **not 89 confirmed vulnerabilities**.

## Start here

| Step | Open | Purpose |
| --- | --- | --- |
| **1** | [Lab setup](lab-setup/README.md) | Connect Kali and Metasploitable 2 safely; run the first scan |
| **2** | [Vulnerability categories & index](FINDINGS-INDEX.md) | Understand 12 categories; browse 89 research candidates with CVE links |
| **3** | [First case study — VULN-001](vulnerabilities/VULN-001-vsftpd-backdoor/README.md) | Document the vsftpd 2.3.4 backdoor test |
| **4** | [Progress checklist](CHECKLIST.md) | Track what is actually finished |

## Repository layout

```text
metasploitable2-vapt-lab/
├── README.md                 ← You are here
├── FINDINGS-INDEX.md         ← Categories + all research candidates
├── CHECKLIST.md              ← Progress
├── SCOPE.md                  ← Safety rules
├── assets/                   ← Simple lab diagram / workflow image
├── lab-setup/
│   ├── README.md             ← VM setup + scan commands + workflow
│   └── scans/                ← Initial Nmap results
├── vulnerabilities/
│   └── VULN-001-vsftpd-backdoor/
│       ├── README.md         ← Individual technical report
│       ├── scans/            ← Actual enumeration output
│       └── screenshots/      ← Actual evidence screenshots
└── templates/
    ├── VULNERABILITY-README-TEMPLATE.md
    └── FINAL-REPORT-TEMPLATE.md
```

**Need a new vulnerability folder?** Copy the [finding template](templates/VULNERABILITY-README-TEMPLATE.md) into `vulnerabilities/VULN-002-short-name/README.md`. Add its `scans/` and `screenshots/` when collecting evidence. Update the [index](FINDINGS-INDEX.md) with the report link.

## What goes in each finding report?

**Overview → CVE/CWE and categories → discovery → enumeration → Metasploit test → manual test → evidence → impact → remediation → references.**

Record the real result of each test—even if exploitation fails. Do not describe untested candidates as confirmed vulnerabilities.

## Testing workflow

![Prepare, discover, enumerate, validate, demonstrate, report, reset](assets/vapt-workflow.svg)

Keep the target on a **VirtualBox Internal Network or properly isolated Host-Only network**; never use Bridged Adapter, port forwarding, or a public tunnel for Metasploitable 2. See [scope and rules](SCOPE.md).

## References

[Rapid7 Metasploitable 2 guide](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/) · [NVD CVE database](https://nvd.nist.gov/) · [MITRE CWE database](https://cwe.mitre.org/)

**Maintained by:** [AazafRitha](https://github.com/AazafRitha)
