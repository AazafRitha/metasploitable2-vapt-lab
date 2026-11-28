# Vulnerability catalog & finding index

> **89 research scenarios; one confirmed through both manual and Metasploit testing (VULN-001).** This is a checklist of **89 scenarios** gathered from historical Metasploitable 2 research: 48 network/OS, 9 DVWA, and 32 Mutillidae. Some overlap or require special configuration; **89 is not an official or verified vulnerability count**.

[← Project home](README.md) · [Lab guide](lab-setup/README.md) · [First report](vulnerabilities/network/VULN-001-vsftpd-backdoor/README.md)

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
| <a id="net-001"></a>**NET-001** | vsftpd 2.3.4 backdoor | FTP / 21 | [CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523) | `BD` `RCE` | Confirmed — manual + Metasploit root RCE | [VULN-001](vulnerabilities/network/VULN-001-vsftpd-backdoor/README.md) |
| <a id="net-002"></a>**NET-002** | UnrealIRCd 3.2.8.1 backdoor | IRC / 6667 | [CVE-2010-2075](https://nvd.nist.gov/vuln/detail/CVE-2010-2075) | `BD` `RCE` | Not tested | [VULN-002](vulnerabilities/network/VULN-002-unrealircd-3-2-8-1-backdoor/README.md) |
| <a id="net-003"></a>**NET-003** | Ingreslock root bind shell | TCP / 1524 | — | `BD` `RCE` `AUTH` | Not tested | [VULN-003](vulnerabilities/network/VULN-003-ingreslock-root-bind-shell/README.md) |
| <a id="net-004"></a>**NET-004** | DistCC remote command execution | DistCC / 3632 | [CVE-2004-2687](https://nvd.nist.gov/vuln/detail/CVE-2004-2687) | `RCE` `MIS` | Not tested | [VULN-004](vulnerabilities/network/VULN-004-distcc-remote-command-execution/README.md) |
| <a id="net-005"></a>**NET-005** | Samba username-map script command injection | SMB / 139,445 | [CVE-2007-2447](https://nvd.nist.gov/vuln/detail/CVE-2007-2447) | `RCE` `INJ` `MIS` | Not tested | [VULN-005](vulnerabilities/network/VULN-005-samba-username-map-script-command-injection/README.md) |
| <a id="net-006"></a>**NET-006** | Java RMI insecure remote execution candidate | RMI / 1099 | — | `RCE` `MIS` | Not tested | [VULN-006](vulnerabilities/network/VULN-006-java-rmi-insecure-remote-execution-candidate/README.md) |
| <a id="net-007"></a>**NET-007** | Ruby DRb exposed remote object execution candidate | DRb / 8787 | — | `RCE` `MIS` | Not tested | [VULN-007](vulnerabilities/network/VULN-007-ruby-drb-exposed-remote-object-execution-candidate/README.md) |
| <a id="net-008"></a>**NET-008** | Legacy wiki command-injection candidate (identify product first) | HTTP / 80 | — | `RCE` `WEB` `INJ` `EOL` | Not tested | [VULN-008](vulnerabilities/network/VULN-008-legacy-wiki-command-injection-candidate/README.md) |
| <a id="net-009"></a>**NET-009** | PHP-CGI argument injection (only if CGI mode is used) | HTTP / 80 | [CVE-2012-1823](https://nvd.nist.gov/vuln/detail/CVE-2012-1823) | `RCE` `WEB` `INJ` | Not tested | [VULN-009](vulnerabilities/network/VULN-009-php-cgi-argument-injection/README.md) |
| <a id="net-010"></a>**NET-010** | Tomcat Manager authenticated WAR deployment | Tomcat / 8180 | — | `AUTH` `WEB` `RCE` `MIS` | Not tested | [VULN-010](vulnerabilities/network/VULN-010-tomcat-manager-authenticated-war-deployment/README.md) |
| <a id="net-011"></a>**NET-011** | ProFTPD mod_sql SQL injection (if mod_sql enabled) | FTP / 2121 | [CVE-2009-0542](https://nvd.nist.gov/vuln/detail/CVE-2009-0542) | `INJ` `DB` `AUTH` | Not tested | [VULN-011](vulnerabilities/network/VULN-011-proftpd-mod-sql-sql-injection/README.md) |
| <a id="net-012"></a>**NET-012** | Default SSH credentials | SSH / 22 | — | `AUTH` `MIS` | Not tested | [VULN-012](vulnerabilities/network/VULN-012-default-ssh-credentials/README.md) |
| <a id="net-013"></a>**NET-013** | Additional weak local account passwords | Linux accounts | — | `AUTH` `MIS` | Not tested | [VULN-013](vulnerabilities/network/VULN-013-additional-weak-local-account-passwords/README.md) |
| <a id="net-014"></a>**NET-014** | Default/weak Telnet credentials | Telnet / 23 | — | `AUTH` `PROTO` | Not tested | [VULN-014](vulnerabilities/network/VULN-014-default-weak-telnet-credentials/README.md) |
| <a id="net-015"></a>**NET-015** | Trust-based Rexec access | Rexec / 512 | — | `AUTH` `MIS` `PROTO` | Not tested | [VULN-015](vulnerabilities/network/VULN-015-trust-based-rexec-access/README.md) |
| <a id="net-016"></a>**NET-016** | Trust-based Rlogin access | Rlogin / 513 | — | `AUTH` `MIS` `PROTO` | Not tested | [VULN-016](vulnerabilities/network/VULN-016-trust-based-rlogin-access/README.md) |
| <a id="net-017"></a>**NET-017** | Trust-based Rsh access | Rsh / 514 | — | `AUTH` `MIS` `PROTO` | Not tested | [VULN-017](vulnerabilities/network/VULN-017-trust-based-rsh-access/README.md) |
| <a id="net-018"></a>**NET-018** | MySQL root access with empty password | MySQL / 3306 | — | `DB` `AUTH` `MIS` | Not tested | [VULN-018](vulnerabilities/network/VULN-018-mysql-root-access-with-empty-password/README.md) |
| <a id="net-019"></a>**NET-019** | PostgreSQL default credentials | PostgreSQL / 5432 | — | `DB` `AUTH` `MIS` | Not tested | [VULN-019](vulnerabilities/network/VULN-019-postgresql-default-credentials/README.md) |
| <a id="net-020"></a>**NET-020** | Weak/default VNC password | VNC / 5900 | — | `AUTH` `MIS` `PROTO` | Not tested | [VULN-020](vulnerabilities/network/VULN-020-weak-default-vnc-password/README.md) |
| <a id="net-021"></a>**NET-021** | Tomcat Manager weak/default credentials | Tomcat / 8180 | — | `AUTH` `WEB` `MIS` | Not tested | [VULN-021](vulnerabilities/network/VULN-021-tomcat-manager-weak-default-credentials/README.md) |
| <a id="net-022"></a>**NET-022** | Predictable Debian/Ubuntu-generated SSH keys (if present) | SSH / 22 | [CVE-2008-0166](https://nvd.nist.gov/vuln/detail/CVE-2008-0166) | `AUTH` `PROTO` | Not tested | [VULN-022](vulnerabilities/network/VULN-022-predictable-debian-ubuntu-generated-ssh-keys/README.md) |
| <a id="net-023"></a>**NET-023** | Anonymous FTP login | FTP / 21 | — | `AUTH` `FILE` `MIS` | Not tested | [VULN-023](vulnerabilities/network/VULN-023-anonymous-ftp-login/README.md) |
| <a id="net-024"></a>**NET-024** | Anonymous ProFTPD access | FTP / 2121 | — | `AUTH` `FILE` `MIS` | Not tested | [VULN-024](vulnerabilities/network/VULN-024-anonymous-proftpd-access/README.md) |
| <a id="net-025"></a>**NET-025** | Anonymous SMB shares | SMB / 139,445 | — | `FILE` `AUTH` `MIS` | Not tested | [VULN-025](vulnerabilities/network/VULN-025-anonymous-smb-shares/README.md) |
| <a id="net-026"></a>**NET-026** | Samba symlink traversal / wide links | SMB / 139,445 | — | `FILE` `MIS` `AUTH` | Not tested | [VULN-026](vulnerabilities/network/VULN-026-samba-symlink-traversal-wide-links/README.md) |
| <a id="net-027"></a>**NET-027** | NFS export of root filesystem to all clients | NFS / 2049 | — | `FILE` `MIS` `AUTH` | Not tested | [VULN-027](vulnerabilities/network/VULN-027-nfs-export-of-root-filesystem-to-all-clients/README.md) |
| <a id="net-028"></a>**NET-028** | Writable NFS export | NFS / 2049 | — | `FILE` `MIS` `AUTH` | Not tested | [VULN-028](vulnerabilities/network/VULN-028-writable-nfs-export/README.md) |
| <a id="net-029"></a>**NET-029** | WebDAV unrestricted PUT/upload | WebDAV / 80 | — | `FILE` `WEB` `MIS` | Not tested | [VULN-029](vulnerabilities/network/VULN-029-webdav-unrestricted-put-upload/README.md) |
| <a id="net-030"></a>**NET-030** | Unauthenticated X11 display access | X11 / 6000 | — | `AUTH` `MIS` `INFO` | Not tested | [VULN-030](vulnerabilities/network/VULN-030-unauthenticated-x11-display-access/README.md) |
| <a id="net-031"></a>**NET-031** | SMTP user enumeration | SMTP / 25 | — | `INFO` `MIS` | Not tested | [VULN-031](vulnerabilities/network/VULN-031-smtp-user-enumeration/README.md) |
| <a id="net-032"></a>**NET-032** | SMTP open relay | SMTP / 25 | — | `MIS` `AUTH` | Not tested | [VULN-032](vulnerabilities/network/VULN-032-smtp-open-relay/README.md) |
| <a id="net-033"></a>**NET-033** | DNS zone transfer | DNS / 53 | — | `INFO` `MIS` | Not tested | [VULN-033](vulnerabilities/network/VULN-033-dns-zone-transfer/README.md) |
| <a id="net-034"></a>**NET-034** | Exposed AJP connector | AJP / 8009 | — | `MIS` `WEB` | Not tested | [VULN-034](vulnerabilities/network/VULN-034-exposed-ajp-connector/README.md) |
| <a id="net-035"></a>**NET-035** | Excessive RPC service disclosure | RPC / 111 | — | `INFO` `MIS` | Not tested | [VULN-035](vulnerabilities/network/VULN-035-excessive-rpc-service-disclosure/README.md) |
| <a id="net-036"></a>**NET-036** | PHP configuration disclosure | HTTP / 80 | — | `INFO` `WEB` `MIS` | Not tested | [VULN-036](vulnerabilities/network/VULN-036-php-configuration-disclosure/README.md) |
| <a id="net-037"></a>**NET-037** | Exposed phpMyAdmin interface | HTTP / 80 | — | `WEB` `DB` `AUTH` `MIS` | Not tested | [VULN-037](vulnerabilities/network/VULN-037-exposed-phpmyadmin-interface/README.md) |
| <a id="net-038"></a>**NET-038** | Cleartext FTP authentication | FTP / 21,2121 | — | `PROTO` `AUTH` | Not tested | [VULN-038](vulnerabilities/network/VULN-038-cleartext-ftp-authentication/README.md) |
| <a id="net-039"></a>**NET-039** | Cleartext Telnet authentication | Telnet / 23 | — | `PROTO` `AUTH` | Not tested | [VULN-039](vulnerabilities/network/VULN-039-cleartext-telnet-authentication/README.md) |
| <a id="net-040"></a>**NET-040** | Legacy SMB protocol/security configurations | SMB / 139,445 | — | `PROTO` `EOL` `MIS` | Not tested | [VULN-040](vulnerabilities/network/VULN-040-legacy-smb-protocol-security-configurations/README.md) |
| <a id="net-041"></a>**NET-041** | Outdated Apache HTTP Server 2.2.8 | HTTP / 80 | — | `EOL` `WEB` | Not tested | [VULN-041](vulnerabilities/network/VULN-041-outdated-apache-http-server-2-2-8/README.md) |
| <a id="net-042"></a>**NET-042** | Outdated Apache Tomcat 5.5 | Tomcat / 8180 | — | `EOL` `WEB` | Not tested | [VULN-042](vulnerabilities/network/VULN-042-outdated-apache-tomcat-5-5/README.md) |
| <a id="net-043"></a>**NET-043** | Outdated PHP 5.2.x | Web stack | — | `EOL` `WEB` | Not tested | [VULN-043](vulnerabilities/network/VULN-043-outdated-php-5-2-x/README.md) |
| <a id="net-044"></a>**NET-044** | Unsupported Ubuntu 8.04 | Operating system | — | `EOL` `MIS` | Not tested | [VULN-044](vulnerabilities/network/VULN-044-unsupported-ubuntu-8-04/README.md) |
| <a id="net-045"></a>**NET-045** | Historical kernel local privilege-escalation candidates | Linux kernel | — | `LPE` `EOL` | Not tested | [VULN-045](vulnerabilities/network/VULN-045-historical-kernel-local-privilege-escalation-candid/README.md) |
| <a id="net-046"></a>**NET-046** | Unsafe privileged SUID executable configuration | Local filesystem | — | `LPE` `MIS` `FILE` | Not tested | [VULN-046](vulnerabilities/network/VULN-046-unsafe-privileged-suid-executable-configuration/README.md) |
| <a id="net-047"></a>**NET-047** | Missing browser security headers | HTTP / 80 | — | `WEB` `MIS` | Not tested | [VULN-047](vulnerabilities/network/VULN-047-missing-browser-security-headers/README.md) |
| <a id="net-048"></a>**NET-048** | Weak TLS/SSL configurations (if a TLS service is running) | TLS services | — | `PROTO` `MIS` | Not tested | [VULN-048](vulnerabilities/network/VULN-048-weak-tls-ssl-configurations/README.md) |

### B. DVWA application exercises (9)

| ID | Candidate | Service / endpoint | CVE | Categories | Lab status | Report |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="dvwa-001"></a>**DVWA-001** | Brute force / weak login protection | Login | — | `WEB` `AUTH` | Not tested | [VULN-049](vulnerabilities/dvwa/VULN-049-brute-force-weak-login-protection/README.md) |
| <a id="dvwa-002"></a>**DVWA-002** | OS command injection | Command execution | — | `WEB` `INJ` `RCE` | Not tested | [VULN-050](vulnerabilities/dvwa/VULN-050-os-command-injection/README.md) |
| <a id="dvwa-003"></a>**DVWA-003** | Cross-Site Request Forgery (CSRF) | CSRF | — | `WEB` `AUTH` | Not tested | [VULN-051](vulnerabilities/dvwa/VULN-051-cross-site-request-forgery/README.md) |
| <a id="dvwa-004"></a>**DVWA-004** | Local/remote file inclusion | File inclusion | — | `WEB` `FILE` | Not tested | [VULN-052](vulnerabilities/dvwa/VULN-052-local-remote-file-inclusion/README.md) |
| <a id="dvwa-005"></a>**DVWA-005** | SQL injection | SQL injection | — | `WEB` `INJ` `DB` | Not tested | [VULN-053](vulnerabilities/dvwa/VULN-053-sql-injection/README.md) |
| <a id="dvwa-006"></a>**DVWA-006** | Blind SQL injection | Blind SQL injection | — | `WEB` `INJ` `DB` | Not tested | [VULN-054](vulnerabilities/dvwa/VULN-054-blind-sql-injection/README.md) |
| <a id="dvwa-007"></a>**DVWA-007** | Unrestricted file upload | File upload | — | `WEB` `FILE` `RCE` | Not tested | [VULN-055](vulnerabilities/dvwa/VULN-055-unrestricted-file-upload/README.md) |
| <a id="dvwa-008"></a>**DVWA-008** | Reflected cross-site scripting | Reflected XSS | — | `WEB` `INJ` | Not tested | [VULN-056](vulnerabilities/dvwa/VULN-056-reflected-cross-site-scripting/README.md) |
| <a id="dvwa-009"></a>**DVWA-009** | Stored cross-site scripting | Stored XSS | — | `WEB` `INJ` | Not tested | [VULN-057](vulnerabilities/dvwa/VULN-057-stored-cross-site-scripting/README.md) |

### C. Mutillidae application exercises (32)

| ID | Candidate | Service / endpoint | CVE | Categories | Lab status | Report |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="mut-001"></a>**MUT-001** | Blog-entry SQL injection | add-to-your-blog.php | — | `WEB` `INJ` `DB` | Not tested | [VULN-058](vulnerabilities/mutillidae/VULN-058-blog-entry-sql-injection/README.md) |
| <a id="mut-002"></a>**MUT-002** | Login SQL injection / authentication bypass | login.php | — | `WEB` `INJ` `DB` `AUTH` | Not tested | [VULN-059](vulnerabilities/mutillidae/VULN-059-login-sql-injection-authentication-bypass/README.md) |
| <a id="mut-003"></a>**MUT-003** | Registration SQL injection | register.php | — | `WEB` `INJ` `DB` | Not tested | [VULN-060](vulnerabilities/mutillidae/VULN-060-registration-sql-injection/README.md) |
| <a id="mut-004"></a>**MUT-004** | User-info SQL injection | user-info.php | — | `WEB` `INJ` `DB` `INFO` | Not tested | [VULN-061](vulnerabilities/mutillidae/VULN-061-user-info-sql-injection/README.md) |
| <a id="mut-005"></a>**MUT-005** | UID-cookie SQL injection | index.php | — | `WEB` `INJ` `DB` | Not tested | [VULN-062](vulnerabilities/mutillidae/VULN-062-uid-cookie-sql-injection/README.md) |
| <a id="mut-006"></a>**MUT-006** | SQL injection via logged HTTP headers | log-visit.php | — | `WEB` `INJ` `DB` | Not tested | [VULN-063](vulnerabilities/mutillidae/VULN-063-sql-injection-via-logged-http-headers/README.md) |
| <a id="mut-007"></a>**MUT-007** | Reflected XSS in login fields | login.php | — | `WEB` `INJ` | Not tested | [VULN-064](vulnerabilities/mutillidae/VULN-064-reflected-xss-in-login-fields/README.md) |
| <a id="mut-008"></a>**MUT-008** | Stored XSS in blog entries | add-to-your-blog.php | — | `WEB` `INJ` | Not tested | [VULN-065](vulnerabilities/mutillidae/VULN-065-stored-xss-in-blog-entries/README.md) |
| <a id="mut-009"></a>**MUT-009** | Header-based XSS (User-Agent / Referer) | browser-info.php | — | `WEB` `INJ` | Not tested | [VULN-066](vulnerabilities/mutillidae/VULN-066-header-based-xss/README.md) |
| <a id="mut-010"></a>**MUT-010** | XSS from displayed log entries | show-log.php | — | `WEB` `INJ` | Not tested | [VULN-067](vulnerabilities/mutillidae/VULN-067-xss-from-displayed-log-entries/README.md) |
| <a id="mut-011"></a>**MUT-011** | XSS through GET/POST/cookies | captured-data.php | — | `WEB` `INJ` | Not tested | [VULN-068](vulnerabilities/mutillidae/VULN-068-xss-through-get-post-cookies/README.md) |
| <a id="mut-012"></a>**MUT-012** | DOM injection via HTML5 storage | html5-storage.php | — | `WEB` `INJ` | Not tested | [VULN-069](vulnerabilities/mutillidae/VULN-069-dom-injection-via-html5-storage/README.md) |
| <a id="mut-013"></a>**MUT-013** | OS command injection | dns-lookup.php | — | `WEB` `INJ` `RCE` | Not tested | [VULN-070](vulnerabilities/mutillidae/VULN-070-os-command-injection/README.md) |
| <a id="mut-014"></a>**MUT-014** | Arbitrary file inclusion | arbitrary-file-inclusion.php | — | `WEB` `FILE` | Not tested | [VULN-071](vulnerabilities/mutillidae/VULN-071-arbitrary-file-inclusion/README.md) |
| <a id="mut-015"></a>**MUT-015** | Arbitrary file read / path traversal | source-viewer.php | — | `WEB` `FILE` `INFO` | Not tested | [VULN-072](vulnerabilities/mutillidae/VULN-072-arbitrary-file-read-path-traversal/README.md) |
| <a id="mut-016"></a>**MUT-016** | Local/remote file or URL loading | text-file-viewer.php | — | `WEB` `FILE` `INFO` | Not tested | [VULN-073](vulnerabilities/mutillidae/VULN-073-local-remote-file-or-url-loading/README.md) |
| <a id="mut-017"></a>**MUT-017** | Privilege manipulation through UID cookie | index.php | — | `WEB` `AUTH` | Not tested | [VULN-074](vulnerabilities/mutillidae/VULN-074-privilege-manipulation-through-uid-cookie/README.md) |
| <a id="mut-018"></a>**MUT-018** | CSRF in blog functionality | add-to-your-blog.php | — | `WEB` `AUTH` | Not tested | [VULN-075](vulnerabilities/mutillidae/VULN-075-csrf-in-blog-functionality/README.md) |
| <a id="mut-019"></a>**MUT-019** | CSRF in polling | user-poll.php | — | `WEB` `AUTH` | Not tested | [VULN-076](vulnerabilities/mutillidae/VULN-076-csrf-in-polling/README.md) |
| <a id="mut-020"></a>**MUT-020** | Clickjacking via framed content | framing.php | — | `WEB` `AUTH` | Not tested | [VULN-077](vulnerabilities/mutillidae/VULN-077-clickjacking-via-framed-content/README.md) |
| <a id="mut-021"></a>**MUT-021** | Clickjacking in art page | rene-magritte.php | — | `WEB` `AUTH` | Not tested | [VULN-078](vulnerabilities/mutillidae/VULN-078-clickjacking-in-art-page/README.md) |
| <a id="mut-022"></a>**MUT-022** | Open redirect on credits | credits.php | — | `WEB` `AUTH` | Not tested | [VULN-079](vulnerabilities/mutillidae/VULN-079-open-redirect-on-credits/README.md) |
| <a id="mut-023"></a>**MUT-023** | Open redirect in redirect/logger | redirectandlog.php | — | `WEB` `AUTH` | Not tested | [VULN-080](vulnerabilities/mutillidae/VULN-080-open-redirect-in-redirect-logger/README.md) |
| <a id="mut-024"></a>**MUT-024** | HTTP response splitting | index.php | — | `WEB` `INJ` | Not tested | [VULN-081](vulnerabilities/mutillidae/VULN-081-http-response-splitting/README.md) |
| <a id="mut-025"></a>**MUT-025** | HTTP parameter pollution | user-poll.php | — | `WEB` `INJ` | Not tested | [VULN-082](vulnerabilities/mutillidae/VULN-082-http-parameter-pollution/README.md) |
| <a id="mut-026"></a>**MUT-026** | HTTP method validation bypass | user-poll.php | — | `WEB` `AUTH` | Not tested | [VULN-083](vulnerabilities/mutillidae/VULN-083-http-method-validation-bypass/README.md) |
| <a id="mut-027"></a>**MUT-027** | Client-side JavaScript validation bypass | login.php | — | `WEB` `AUTH` | Not tested | [VULN-084](vulnerabilities/mutillidae/VULN-084-client-side-javascript-validation-bypass/README.md) |
| <a id="mut-028"></a>**MUT-028** | Cookies missing HttpOnly | process-commands.php | — | `WEB` `MIS` `AUTH` | Not tested | [VULN-085](vulnerabilities/mutillidae/VULN-085-cookies-missing-httponly/README.md) |
| <a id="mut-029"></a>**MUT-029** | Unencrypted database credentials in config | config.inc | — | `INFO` `DB` `MIS` | Not tested | [VULN-086](vulnerabilities/mutillidae/VULN-086-unencrypted-database-credentials-in-config/README.md) |
| <a id="mut-030"></a>**MUT-030** | PHP configuration and path disclosure | phpinfo.php | — | `INFO` `WEB` `MIS` | Not tested | [VULN-087](vulnerabilities/mutillidae/VULN-087-php-configuration-and-path-disclosure/README.md) |
| <a id="mut-031"></a>**MUT-031** | CSS injection | set-background-color.php | — | `WEB` `INJ` | Not tested | [VULN-088](vulnerabilities/mutillidae/VULN-088-css-injection/README.md) |
| <a id="mut-032"></a>**MUT-032** | JSON injection | pen-test-tool-lookup.php | — | `WEB` `INJ` | Not tested | [VULN-089](vulnerabilities/mutillidae/VULN-089-json-injection/README.md) |

## 4. Turning a candidate into a real finding

1. Confirm the affected service exists on your **isolated** Metasploitable 2 VM.
2. Test it using the [lab guide](lab-setup/README.md).
3. Open the pre-created `vulnerabilities/network/`, `vulnerabilities/dvwa/`, or `vulnerabilities/mutillidae/` case folder and fill its report using the [report template](templates/VULNERABILITY-README-TEMPLATE.md).
4. Record the catalog ID, CVE if applicable, CWE, **all matching category tags**, actual commands, raw scan output, and real screenshots.
5. Update this row's status only after evidence-based testing, and add confirmed findings to a consolidated report later.

**Research checks:** TWiki and TikiWiki are different products; do not attach a TWiki CVE to a TikiWiki service. ProFTPD `mod_sql`, PHP-CGI, SSH predictable keys, RMI and other conditional scenarios must be validated for the installed version and configuration.

## 5. References

- [Rapid7 — Metasploitable 2 Exploitability Guide](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)
- [Rapid7 — Metasploitable 2](https://docs.rapid7.com/metasploit/metasploitable-2/)
- [OWASP — Metasploitable 2](https://vwad.owasp.org/app/metasploitable-2/)
- [NVD — CVE database](https://nvd.nist.gov/)
- [MITRE — CWE database](https://cwe.mitre.org/)

All 89 report folders are **prepared**. **VULN-001 is confirmed by independent manual and Metasploit root-shell evidence**; the other 88 scenarios remain untested. A folder alone is not proof of a vulnerability.
