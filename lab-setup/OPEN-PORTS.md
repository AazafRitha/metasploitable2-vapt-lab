# Initial reconnaissance — TCP open-port results

[← Main project README](../README.md) · [Lab instructions](README.md) · [First vulnerability case study](../vulnerabilities/network/VULN-001-vsftpd-backdoor/README.md)

## Scan details

| Field | Observed value |
| --- | --- |
| Date/time (scanner local) | 2026-11-27, 18:12 +0530 |
| Attacker (Kali) | `192.168.95.128` |
| Target (Metasploitable 2) | `192.168.95.131` |
| Tool | Nmap 7.99 |
| Command | `sudo nmap -sS -sV -sC -p- --open -oA ~/Desktop/Metasploitable2/Scans/01-Full-Port-Scan 192.168.95.131` |
| Scan coverage | All 65,535 TCP ports |
| Open | **29 TCP ports** |
| Closed | **65,506 TCP ports** |
| Target state | Up (reported latency 0.0019s) |
| Elapsed time | 279.67 seconds |
| Source | Results supplied from the Kali terminal by the lab owner; this Markdown is a **transcription/summary**, not the original Nmap output file |

## All 29 open TCP ports

| Port/TCP | Service | Detected version / fingerprint | Observation |
| ---: | --- | --- | --- |
| 21 | ftp | vsftpd 2.3.4 | FTP anonymous login allowed; candidate VULN-001 |
| 22 | ssh | OpenSSH 4.7p1 Debian 8ubuntu1 | Host keys reported |
| 23 | telnet | Linux telnetd | Unencrypted protocol |
| 25 | smtp | Postfix smtpd | VRFY advertised; verify separately |
| 53 | domain | ISC BIND 9.4.2 | DNS server |
| 80 | http | Apache httpd 2.2.8 (Ubuntu) DAV/2 | Metasploitable2 web page |
| 111 | rpcbind | RPCbind v2 | RPC services listed |
| 139 | netbios-ssn | Samba smbd 3.X–4.X | SMB service |
| 445 | netbios-ssn | Samba smbd 3.0.20-Debian | SMB message signing disabled |
| 512 | exec | netkit-rsh rexecd | Legacy remote execution protocol |
| 513 | login | rlogind (OpenBSD or Solaris fingerprint) | Legacy remote login |
| 514 | tcpwrapped | Service not identified | Further service checks needed |
| 1099 | java-rmi | GNU Classpath grmiregistry | RMI registry |
| 1524 | bindshell | Metasploitable root shell (Nmap identification) | Possible exposed shell; not yet interacted with |
| 2049 | nfs | NFS v2–v4 | Check exports later |
| 2121 | ftp | ProFTPD 1.3.1 | Second FTP service |
| 3306 | mysql | MySQL 5.0.51a-3ubuntu5 | Database service |
| 3632 | distccd | distccd v1 / GNU 4.2.4 | RCE candidate; not tested |
| 5432 | postgresql | PostgreSQL 8.3.0–8.3.7 | Historical SSL certificate expired |
| 5900 | vnc | VNC protocol 3.3 | VNC authentication offered |
| 6000 | X11 | X11 | Access denied in scan |
| 6667 | irc | UnrealIRCd | Potential backdoor candidate; not tested |
| 6697 | irc | UnrealIRCd | Additional IRC port |
| 8180 | unknown | Unknown (Nmap could not identify) | Do not assume Tomcat without verification |
| 8787 | drb | Ruby DRb RMI (Ruby 1.8) | Ruby remote-object service |
| 40543 | status | RPC status v1 | RPC dynamic port |
| 41662 | mountd | RPC mountd v1–v3 | RPC dynamic port |
| 54420 | java-rmi | GNU Classpath grmiregistry | Additional RMI endpoint |
| 57382 | nlockmgr | RPC nlockmgr v1–v4 | RPC dynamic port |

## Relevant NSE observations

- `ftp-anon`: Anonymous FTP login **allowed** (FTP code 230).
- `ftp-syst`: Service reports **vsFTPd 2.3.4**, plain-text control/data connections, connected client `192.168.95.128`.
- `smb-security-mode`: Guest context used for enumeration; SMB message signing **disabled**.
- `smb-os-discovery`: Samba 3.0.20-Debian; computer name `metasploitable`; workgroup `WORKGROUP`.
- `ssh-hostkey`: DSA and RSA host keys offered; this is **not evidence of a compromised key**.
- `ssl-cert` on PostgreSQL port 5432: reported certificate validity 2010-03-17 to 2010-04-16 (expired relative to scan date).
- `vnc-info`: VNC protocol 3.3 with VNC authentication.
- `X11/6000`: Nmap reports **access denied**, so do not claim unauthorized X11 access.
- `8180/tcp`: Nmap lists **unknown** — further HTTP/service checks required before identifying Tomcat.
- Nmap reports port 1524 as a **Metasploitable root shell**, but root access is not yet independently verified in this assessment.

## Evidence location and screenshot

Actual Nmap output was saved on the **Kali Desktop** via `-oA`:

```text
~/Desktop/Metasploitable2/Scans/01-Full-Port-Scan.nmap
~/Desktop/Metasploitable2/Scans/01-Full-Port-Scan.gnmap
~/Desktop/Metasploitable2/Scans/01-Full-Port-Scan.xml
```

For GitHub, copy the raw `.nmap`, `.gnmap`, and `.xml` files from Kali into this repository's `lab-setup/scans/` directory. Upload a **real screenshot** to `lab-setup/screenshots/01-all-open-ports.png`, then embed it in the project README. **No screenshot has been received or uploaded at the time of this summary.**

## Assessment interpretation

**Confirmed by enumeration:** host reachable; TCP port state and reported service/version fingerprints; anonymous FTP login allowed.

**Not established:** successful exploitation of CVE-2011-2523, root access via port 6200, weakness of any account password, exploitation of Samba/DistCC/UnrealIRCd, or actual impact on the target.

**Next:** Begin [VULN-001](../vulnerabilities/network/VULN-001-vsftpd-backdoor/README.md): specifically investigate TCP 21 and validate whether the backdoor behavior is present using the isolated lab.

## Reporting note

This is a scan summary, not a penetration-test finding. A service banner or a matching version is insufficient to mark CVEs as confirmed.
