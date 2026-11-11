# VULN-001: vsftpd 2.3.4 Backdoor — Initial case study

> **Status:** Not tested. This is a planned exercise, not a confirmed vulnerability on the current VM.

## 1. Candidate information

| Field | Value |
| --- | --- |
| Finding ID | VULN-001 |
| Candidate | Backdoored vsftpd 2.3.4 distribution |
| CVE | CVE-2011-2523 |
| Target | Metasploitable 2 (actual IP to be recorded) |
| Service / port | FTP / TCP 21 (to verify) |
| Severity | Not rated; requires validation and context |
| Assessment date | TBD |
| Metasploit approach | Not attempted |
| Manual approach | Not attempted |
| Observed impact | None reported yet |

## 2. Background
The historical vsftpd 2.3.4 backdoor case concerns a compromised distribution that could trigger unauthorized remote command execution. **A service version alone does not demonstrate that the backdoored build is present.** Verify service behavior and collect primary evidence.

## 3. Discovery

**Objective:** Check whether FTP is exposed on the authorized Metasploitable 2 VM.

```bash
nmap -sV -p 21 -oN scans/01-ftp-version.nmap <TARGET_IP>
```

**Actual output:** Pending.  
**Evidence:** [scans/README.md](scans/README.md)  
**Interpretation:** Complete after scan, including actual banner/version and confidence.

## 4. Enumeration
Document how you confirmed FTP availability, gathered banner information, and considered alternative explanations. Include commands and observed output.

**Status:** Not attempted.

## 5. Validation
Confirm if the issue exists in your VM. Link authoritative descriptions and explain the difference between vulnerable-version identification and an actual successful backdoor trigger.

**Status:** Not attempted.

## 6. Metasploit method
If validation is appropriate, record the matching module, `show options` output, chosen parameters, executed commands, raw output, any framework-version limitations, and whether controlled access was demonstrated.

**Status:** Not attempted.  
**Evidence:** No screenshots yet.

## 7. Manual method
Document the equivalent manual service interaction using locally authorized tools (for example, Netcat) when practical, and identify any differences from the framework approach.

**Status:** Not attempted.  
**Evidence:** No screenshots yet.

## 8. Proof and impact
Once tested, record harmless proof (such as user identity or environment information), actual privileges, whether access was obtained, and exact evidence references.

**Observed result:** Not tested. Do not infer success.

## 9. Risk and remediation
If confirmed, discuss unauthorized command execution potential and corrective controls. Recommended mitigation in real systems includes removing compromised packages, reinstalling trusted and supported software, restricting FTP exposure, preferring secure transfer protocols, and checking for compromise.

## 10. Limitations
No live test results have been added. The CVE identifies a historical issue, not proof for this specific target.

## 11. References
- [NVD: CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523)
- [Rapid7 Metasploit modules](https://www.rapid7.com/db/)

## 12. Conclusion
This directory provides the reporting structure for the first training scenario. Update the status and sections only after actual lab verification.
