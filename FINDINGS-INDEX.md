# Vulnerability catalog & finding index

> **Research only — not confirmed on my VM.** This is a checklist of **89 scenarios** gathered from historical Metasploitable 2 research: 48 network/OS, 9 DVWA, and 32 Mutillidae. Some overlap or require special configuration; **89 is not an official or verified vulnerability count**.

[← Project home](README.md) · [Lab guide](lab-setup/README.md) · [First report](vulnerabilities/VULN-001-vsftpd-backdoor/README.md)

## 1. Vulnerability categories (explained)

Each candidate can have **multiple tags**. For example, vsftpd backdoor = `BD` + `RCE`; SQL injection = `WEB` + `INJ` + `DB`.

| Tag | Category | Meaning |
| --- | --- | --- |
| `BD` | **Backdoors** | Hidden or deliberately exposed access paths that bypass normal security controls. |
| `RCE` | **Remote Code Execution** | A remote user can cause the target to run operating-system or application commands. |
| `AUTH` | **Authentication & access control** | Weak credentials, login bypasses, authorization failures, or excessive privileges. |
| `MIS` | **Security misconfiguration** | Unsafe default settings, unintended service exposure, insecure trust or permissions. |
| `FILE` | **File access & sharing** | Unsafe shares, uploads, traversal, local/remote file inclusion, or filesystem access. |
| `WEB` | **Web application security** | Weaknesses in HTTP applications, web input handling, sessions, and request processing. |
| `DB` | **Database security** | Weak database authentication, unsafe database access, or injection affecting stored data. |
| `INFO` | **Information disclosure** | Exposure of protected data, internal configuration, user information, or environment details. |
| `EOL` | **Legacy & outdated components** | Unsupported systems or old software requiring patch/version-specific review; version age alone is not proof. |
| `LPE` | **Local privilege escalation** | A user with some local access may gain higher permissions on the host. |
| `PROTO` | **Protocol & cryptographic weakness** | Cleartext credentials, legacy protocols, weak encryption, or predictable key material. |
| `INJ` | **Injection flaws** | Untrusted input changes the meaning of SQL, OS commands, JavaScript, HTML, CSS, or another interpreter. |

## 2. How to read the index

- **Research IDs:** `NET-001`, `DVWA-001`, `MUT-001` are entries to investigate, **not** completed findings.
- **Finding IDs:** `VULN-001`, `VULN-002`, etc. are folders for technical reports when testing starts.
- **CVE:** Click the published vulnerability reference when available. `—` means no verified individual CVE; add relevant **CWE** references to the actual report.
- **Status:** Every entry starts as **Not tested**. Only update to **Investigating**, **Confirmed**, **Not confirmed**, or **Unable to validate** based on your own evidence.
- **Tags:** A finding may belong to more than one category. Never infer exploitability or severity from tags or a version banner alone.

## 3. Research and findings index

### A. Network and Linux services (48)

| ID | Candidate | Service / endpoint | CVE | Categories | Lab status | Report |
| --- | --- | --- | --- | --- | --- | --- |
| **NET-001** | vsftpd 2.3.4 backdoor | FTP / 21 | [CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523) | `BD` `RCE` | Not tested | [VULN-001](vulnerabilities/VULN-001-vsftpd-backdoor/README.md) |
| **NET-002** | UnrealIRCd 3.2.8.1 backdoor | IRC / 6667 | [CVE-2010-2075](https://nvd.nist.gov/vuln/detail/CVE-2010-2075) | `BD` `RCE` | Not tested | — |
| **NET-003** | Ingreslock root bind shell | TCP / 1524 | — | `BD` `RCE` `AUTH` | Not tested | — |
| **NET-004** | DistCC remote command execution | DistCC / 3632 | [CVE-2004-2687](https://nvd.nist.gov/vuln/detail/CVE-2004-2687) | `RCE` `MIS` | Not tested | — |
| **NET-005** | Samba username-map script command injection | SMB / 139,445 | [CVE-2007-2447](https://nvd.nist.gov/vuln/detail/CVE-2007-2447) | `RCE` `INJ` `MIS` | Not tested | — |
| **NET-006** | Java RMI insecure remote execution candidate | RMI / 1099 | — | `RCE` `MIS` | Not tested | — |
| **NET-007** | Ruby DRb exposed remote object execution candidate | DRb / 8787 | — | `RCE` `MIS` | Not tested | — |
| **NET-008** | Legacy wiki command-injection candidate (identify product first) | HTTP / 80 | — | `RCE` `WEB` `INJ` `EOL` | Not tested | — |
| **NET-009** | PHP-CGI argument injection (only if CGI mode is used) | HTTP / 80 | [CVE-2012-1823](https://nvd.nist.gov/vuln/detail/CVE-2012-1823) | `RCE` `WEB` `INJ` | Not tested | — |
| **NET-010** | Tomcat Manager authenticated WAR deployment | Tomcat / 8180 | — | `AUTH` `WEB` `RCE` `MIS` | Not tested | — |
| **NET-011** | ProFTPD mod_sql SQL injection (if mod_sql enabled) | FTP / 2121 | [CVE-2009-0542](https://nvd.nist.gov/vuln/detail/CVE-2009-0542) | `INJ` `DB` `AUTH` | Not tested | — |
| **NET-012** | Default SSH credentials | SSH / 22 | — | `AUTH` `MIS` | Not tested | — |
| **NET-013** | Additional weak local account passwords | Linux accounts | — | `AUTH` `MIS` | Not tested | — |
| **NET-014** | Default/weak Telnet credentials | Telnet / 23 | — | `AUTH` `PROTO` | Not tested | — |
| **NET-015** | Trust-based Rexec access | Rexec / 512 | — | `AUTH` `MIS` `PROTO` | Not tested | — |
| **NET-016** | Trust-based Rlogin access | Rlogin / 513 | — | `AUTH` `MIS` `PROTO` | Not tested | — |
| **NET-017** | Trust-based Rsh access | Rsh / 514 | — | `AUTH` `MIS` `PROTO` | Not tested | — |
| **NET-018** | MySQL root access with empty password | MySQL / 3306 | — | `DB` `AUTH` `MIS` | Not tested | — |
| **NET-019** | PostgreSQL default credentials | PostgreSQL / 5432 | — | `DB` `AUTH` `MIS` | Not tested | — |
| **NET-020** | Weak/default VNC password | VNC / 5900 | — | `AUTH` `MIS` `PROTO` | Not tested | — |
| **NET-021** | Tomcat Manager weak/default credentials | Tomcat / 8180 | — | `AUTH` `WEB` `MIS` | Not tested | — |
| **NET-022** | Predictable Debian/Ubuntu-generated SSH keys (if present) | SSH / 22 | [CVE-2008-0166](https://nvd.nist.gov/vuln/detail/CVE-2008-0166) | `AUTH` `PROTO` | Not tested | — |
| **NET-023** | Anonymous FTP login | FTP / 21 | — | `AUTH` `FILE` `MIS` | Not tested | — |
| **NET-024** | Anonymous ProFTPD access | FTP / 2121 | — | `AUTH` `FILE` `MIS` | Not tested | — |
| **NET-025** | Anonymous SMB shares | SMB / 139,445 | — | `FILE` `AUTH` `MIS` | Not tested | — |
| **NET-026** | Samba symlink traversal / wide links | SMB / 139,445 | — | `FILE` `MIS` `AUTH` | Not tested | — |
| **NET-027** | NFS export of root filesystem to all clients | NFS / 2049 | — | `FILE` `MIS` `AUTH` | Not tested | — |
| **NET-028** | Writable NFS export | NFS / 2049 | — | `FILE` `MIS` `AUTH` | Not tested | — |
| **NET-029** | WebDAV unrestricted PUT/upload | WebDAV / 80 | — | `FILE` `WEB` `MIS` | Not tested | — |
| **NET-030** | Unauthenticated X11 display access | X11 / 6000 | — | `AUTH` `MIS` `INFO` | Not tested | — |
| **NET-031** | SMTP user enumeration | SMTP / 25 | — | `INFO` `MIS` | Not tested | — |
| **NET-032** | SMTP open relay | SMTP / 25 | — | `MIS` `AUTH` | Not tested | — |
| **NET-033** | DNS zone transfer | DNS / 53 | — | `INFO` `MIS` | Not tested | — |
| **NET-034** | Exposed AJP connector | AJP / 8009 | — | `MIS` `WEB` | Not tested | — |
| **NET-035** | Excessive RPC service disclosure | RPC / 111 | — | `INFO` `MIS` | Not tested | — |
| **NET-036** | PHP configuration disclosure | HTTP / 80 | — | `INFO` `WEB` `MIS` | Not tested | — |
| **NET-037** | Exposed phpMyAdmin interface | HTTP / 80 | — | `WEB` `DB` `AUTH` `MIS` | Not tested | — |
| **NET-038** | Cleartext FTP authentication | FTP / 21,2121 | — | `PROTO` `AUTH` | Not tested | — |
| **NET-039** | Cleartext Telnet authentication | Telnet / 23 | — | `PROTO` `AUTH` | Not tested | — |
| **NET-040** | Legacy SMB protocol/security configurations | SMB / 139,445 | — | `PROTO` `EOL` `MIS` | Not tested | — |
| **NET-041** | Outdated Apache HTTP Server 2.2.8 | HTTP / 80 | — | `EOL` `WEB` | Not tested | — |
| **NET-042** | Outdated Apache Tomcat 5.5 | Tomcat / 8180 | — | `EOL` `WEB` | Not tested | — |
| **NET-043** | Outdated PHP 5.2.x | Web stack | — | `EOL` `WEB` | Not tested | — |
| **NET-044** | Unsupported Ubuntu 8.04 | Operating system | — | `EOL` `MIS` | Not tested | — |
| **NET-045** | Historical kernel local privilege-escalation candidates | Linux kernel | — | `LPE` `EOL` | Not tested | — |
| **NET-046** | Unsafe privileged SUID executable configuration | Local filesystem | — | `LPE` `MIS` `FILE` | Not tested | — |
| **NET-047** | Missing browser security headers | HTTP / 80 | — | `WEB` `MIS` | Not tested | — |
| **NET-048** | Weak TLS/SSL configurations (if a TLS service is running) | TLS services | — | `PROTO` `MIS` | Not tested | — |

### B. DVWA application exercises (9)

| ID | Candidate | Service / endpoint | CVE | Categories | Lab status | Report |
| --- | --- | --- | --- | --- | --- | --- |
| **DVWA-001** | Brute force / weak login protection | Login | — | `WEB` `AUTH` | Not tested | — |
| **DVWA-002** | OS command injection | Command execution | — | `WEB` `INJ` `RCE` | Not tested | — |
| **DVWA-003** | Cross-Site Request Forgery (CSRF) | CSRF | — | `WEB` `AUTH` | Not tested | — |
| **DVWA-004** | Local/remote file inclusion | File inclusion | — | `WEB` `FILE` | Not tested | — |
| **DVWA-005** | SQL injection | SQL injection | — | `WEB` `INJ` `DB` | Not tested | — |
| **DVWA-006** | Blind SQL injection | Blind SQL injection | — | `WEB` `INJ` `DB` | Not tested | — |
| **DVWA-007** | Unrestricted file upload | File upload | — | `WEB` `FILE` `RCE` | Not tested | — |
| **DVWA-008** | Reflected cross-site scripting | Reflected XSS | — | `WEB` `INJ` | Not tested | — |
| **DVWA-009** | Stored cross-site scripting | Stored XSS | — | `WEB` `INJ` | Not tested | — |

### C. Mutillidae application exercises (32)

| ID | Candidate | Service / endpoint | CVE | Categories | Lab status | Report |
| --- | --- | --- | --- | --- | --- | --- |
| **MUT-001** | Blog-entry SQL injection | add-to-your-blog.php | — | `WEB` `INJ` `DB` | Not tested | — |
| **MUT-002** | Login SQL injection / authentication bypass | login.php | — | `WEB` `INJ` `DB` `AUTH` | Not tested | — |
| **MUT-003** | Registration SQL injection | register.php | — | `WEB` `INJ` `DB` | Not tested | — |
| **MUT-004** | User-info SQL injection | user-info.php | — | `WEB` `INJ` `DB` `INFO` | Not tested | — |
| **MUT-005** | UID-cookie SQL injection | index.php | — | `WEB` `INJ` `DB` | Not tested | — |
| **MUT-006** | SQL injection via logged HTTP headers | log-visit.php | — | `WEB` `INJ` `DB` | Not tested | — |
| **MUT-007** | Reflected XSS in login fields | login.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-008** | Stored XSS in blog entries | add-to-your-blog.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-009** | Header-based XSS (User-Agent / Referer) | browser-info.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-010** | XSS from displayed log entries | show-log.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-011** | XSS through GET/POST/cookies | captured-data.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-012** | DOM injection via HTML5 storage | html5-storage.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-013** | OS command injection | dns-lookup.php | — | `WEB` `INJ` `RCE` | Not tested | — |
| **MUT-014** | Arbitrary file inclusion | arbitrary-file-inclusion.php | — | `WEB` `FILE` | Not tested | — |
| **MUT-015** | Arbitrary file read / path traversal | source-viewer.php | — | `WEB` `FILE` `INFO` | Not tested | — |
| **MUT-016** | Local/remote file or URL loading | text-file-viewer.php | — | `WEB` `FILE` `INFO` | Not tested | — |
| **MUT-017** | Privilege manipulation through UID cookie | index.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-018** | CSRF in blog functionality | add-to-your-blog.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-019** | CSRF in polling | user-poll.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-020** | Clickjacking via framed content | framing.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-021** | Clickjacking in art page | rene-magritte.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-022** | Open redirect on credits | credits.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-023** | Open redirect in redirect/logger | redirectandlog.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-024** | HTTP response splitting | index.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-025** | HTTP parameter pollution | user-poll.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-026** | HTTP method validation bypass | user-poll.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-027** | Client-side JavaScript validation bypass | login.php | — | `WEB` `AUTH` | Not tested | — |
| **MUT-028** | Cookies missing HttpOnly | process-commands.php | — | `WEB` `MIS` `AUTH` | Not tested | — |
| **MUT-029** | Unencrypted database credentials in config | config.inc | — | `INFO` `DB` `MIS` | Not tested | — |
| **MUT-030** | PHP configuration and path disclosure | phpinfo.php | — | `INFO` `WEB` `MIS` | Not tested | — |
| **MUT-031** | CSS injection | set-background-color.php | — | `WEB` `INJ` | Not tested | — |
| **MUT-032** | JSON injection | pen-test-tool-lookup.php | — | `WEB` `INJ` | Not tested | — |

## 4. Turning a candidate into a real finding

1. Confirm the affected service exists on your **isolated** Metasploitable 2 VM.
2. Test it using the [lab guide](lab-setup/README.md).
3. Create one `vulnerabilities/VULN-###-name/` folder using the [report template](templates/VULNERABILITY-README-TEMPLATE.md).
4. Record the catalog ID, CVE if applicable, CWE, **all matching category tags**, actual commands, raw scan output, and real screenshots.
5. Update this row's status and link to your report. Add confirmed findings to a consolidated report later.

**Research checks:** TWiki and TikiWiki are different products; do not attach a TWiki CVE to a TikiWiki service. ProFTPD `mod_sql`, PHP-CGI, SSH predictable keys, RMI and other conditional scenarios must be validated for the installed version and configuration.

## 5. References

- [Rapid7 — Metasploitable 2 Exploitability Guide](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)
- [Rapid7 — Metasploitable 2](https://docs.rapid7.com/metasploit/metasploitable-2/)
- [OWASP — Metasploitable 2](https://vwad.owasp.org/app/metasploitable-2/)
- [NVD — CVE database](https://nvd.nist.gov/)
- [MITRE — CWE database](https://cwe.mitre.org/)

The catalog is a research starting point; no local exploitation has been verified or recorded yet.
