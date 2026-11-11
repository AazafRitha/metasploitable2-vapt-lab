# Scope and Rules of Engagement

## Authorization
The owner of this project is authorized to test **only the locally owned, intentionally vulnerable Metasploitable 2 virtual machine**. Do not target external, campus, workplace, cloud, or third-party systems.

## In scope
- Target: Metasploitable 2, running in an isolated VirtualBox virtual network
- Source: Kali Linux VM in the same isolated network
- Services: Only those found on the target VM
- Methods: Discovery, service enumeration, careful vulnerability validation, controlled Metasploit/manual proof of concept, minimal impact checks, reporting
- Test window: Local offline sessions chosen by the lab operator

## Out of scope
- Any system other than the named Metasploitable 2 VM
- Internet-facing infrastructure, real users, public IP ranges, other LAN devices
- Credential theft from real users, persistence, lateral movement, denial of service, destructive changes, data exfiltration
- Attacks beyond this isolated training environment

## Network safety
- Use an **Internal Network** (preferred) or correctly isolated **Host-Only** adapter for the target.
- Never use a Bridged Adapter or port-forward Metasploitable 2 services.
- Do not attach the vulnerable target to a cloud tunnel, public VPN, or exposed network.
- Snapshot the target before testing, and restore when needed.

## Evidence safety
Keep filenames and findings reproducible, but redact private keys, API tokens, passwords, unrelated host details, and sensitive network metadata from any public commit. Use local-only test data. Do not publish successful session material or credentials.

## Reporting rules
- Use statuses: **Not tested**, **Investigating**, **Confirmed**, **Not confirmed**, or **Unable to validate**.
- Record dates, versions, commands, results, and limitations.
- Never call a vulnerability confirmed based solely on a version scan.
- CVSS/severity requires a stated assessment and evidence; label estimates as provisional.
- Report manual and Metasploit methods separately; do not claim either was run without evidence.
