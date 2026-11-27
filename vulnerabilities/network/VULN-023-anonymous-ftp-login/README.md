# VULN-023: Anonymous FTP login

> **Not tested** — pre-created report template; no vulnerability confirmed.
>
> [← Master finding index](../../../FINDINGS-INDEX.md#net-023) · [Project home](../../../README.md) · [Lab setup](../../../lab-setup/README.md)

## Finding details

| Field | Value |
| --- | --- |
| Finding ID | `VULN-023` |
| Research catalog ID | `NET-023` |
| Vulnerability candidate | Anonymous FTP login |
| Service / endpoint | FTP / 21 |
| CVE reference | N/A — add matching CWE after analysis |
| CWE reference | TBD — see [MITRE CWE](https://cwe.mitre.org/) |
| Categories | `AUTH` `FILE` `MIS` |
| Validation status | Not tested |
| Metasploit result | Not attempted |
| Manual result | Not attempted |
| Severity | Not rated |
| Tested date / target IP | TBD |

## 1. Vulnerability overview

Describe the vulnerability, affected service, how it works, prerequisites and references. Do not infer that a local service is vulnerable from its version banner alone.

## 2. Reconnaissance and enumeration

**Commands used:** Pending.

**Actual output and explanation:** Pending.

**Evidence:** Save original sanitized outputs in [`scans/`](scans/), images in [`screenshots/`](screenshots/).

## 3. Vulnerability identification and validation

Document the checks performed, exact results, configuration or version prerequisites, false positives and source references.

**Result:** Not tested.

## 4. Metasploit Framework approach (if applicable)

Record module name, `show options`, settings, commands, output, observed impact, troubleshooting and screenshots.

**Result:** Not attempted.

## 5. Manual testing approach (if applicable)

Record direct service or HTTP interactions, tools, exact requests, command output, and evidence.

**Result:** Not attempted.

## 6. Proof of concept and impact

Verify any access minimally and non-destructively. Distinguish *potential* impact from *observed* impact.

**Result:** Not tested.

## 7. Remediation and retesting

Explain the root cause, specific mitigation, safe alternatives and how to verify a fix.

## 8. References

- N/A — add matching CWE after analysis
- [Rapid7 Metasploitable 2 exploitability guide](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)
- Add specific vendor / CWE / Metasploit documentation actually used

## 9. Conclusion and limitations

No test has been run or documented in this folder. Record the actual outcome, remaining gaps and snapshot restoration after the exercise.

---

**Evidence names:** `scans/01-discovery.nmap`, `screenshots/01-enumeration.png`, `screenshots/02-validation.png`. Never publish passwords, tokens, private keys, or fictional successes.
