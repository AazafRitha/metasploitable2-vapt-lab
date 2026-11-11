# VAPT methodology

This repository follows a clear technical reporting process aligned conceptually with standard penetration testing phases. It does not represent a formally accredited assessment.

## 1. Preparation and scope
Confirm authorization, target identity, network isolation, lab snapshots, tools, and assessment dates.

## 2. Discovery and enumeration
Discover ports and services with scoped Nmap commands; enumerate a specific service only after verifying it belongs to the target. Keep **original scan evidence**, not just screenshots.

## 3. Vulnerability identification
Review service banners/configuration and authoritative references. A version match is a **candidate**, not proof of a flaw. Record prerequisites and false-positive considerations.

## 4. Controlled validation and exploitation
Document both approaches **when applicable**:
- **Metasploit:** module name, parameters, why the module was chosen, output, success/failure, and version limitations.
- **Manual:** direct service interaction or original script, conditions, command/output, interpretation, success/failure.

Use only your own lab host. Prefer read-only/non-destructive verification. No persistence or lateral movement.

## 5. Evidence and impact
Record exact steps, command output, target context, observed access level, limitations, and numbered screenshots. Distinguish **proven impact** from possible impact.

## 6. Risk and remediation
Explain affected component, root cause, what an attacker could do, environmental constraints, and prioritized mitigation. Severity should be assigned with justification (e.g. CVSS) only after validation.

## 7. Reporting and repository hygiene
Each finding receives its own numbered directory, with:
- `README.md`
- `scans/`
- `screenshots/`
- `scripts/` when needed

Use relative links, include dates/tool versions, and omit secrets. Summarize findings in the root README and consolidated report.

## Suggested evidence sequence
1. `01-discovery.png`
2. `02-enumeration.png`
3. `03-metasploit-module.png` (if tested)
4. `04-metasploit-validation.png` (if tested)
5. `05-manual-validation.png` (if tested)
6. `06-impact-verification.png`

Never fabricate images, transcripts, CVSS values, or success claims. Mark steps as **not attempted** when appropriate.
