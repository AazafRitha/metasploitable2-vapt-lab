# Lab setup and first scan

[← Project home](../README.md) · [Vulnerability catalog](../FINDINGS-INDEX.md)

## 1. Set up a safe virtual network

You need **Kali Linux (attacker)** and **Metasploitable 2 (target)** on the same isolated VirtualBox network.

1. Power off both VMs.
2. VirtualBox → each VM → **Settings → Network**.
3. Set both VMs to the same **Internal Network** (recommended), e.g., `vapt-lab`. If there is no DHCP server, set unique static addresses on the same subnet. A correctly isolated **Host-Only** network also works.
4. **Never** bridge Metasploitable 2 to your real LAN, port-forward its services, or expose it through a tunnel.
5. Create a **VM snapshot** before testing.

| VM | Purpose | IP (fill after setup) |
| --- | --- | --- |
| Kali Linux | Attacker and reporting | TBD |
| Metasploitable 2 | Intentionally vulnerable target | TBD |

## 2. Find the IP addresses

On **Metasploitable 2**:

```bash
ifconfig
```

On **Kali**:

```bash
ip -4 addr
```

Verify the IP of your target belongs to **your own isolated VM**. On Kali:

```bash
ping -c 3 <TARGET_IP>
```

## 3. Save the first scan

In Kali, clone the project and run a single-host service scan:

```bash
git clone https://github.com/AazafRitha/metasploitable2-vapt-lab.git
cd metasploitable2-vapt-lab
sudo nmap -sC -sV -oA lab-setup/scans/initial-service-scan <TARGET_IP>
```

This saves `.nmap`, `.gnmap`, and `.xml` evidence files in `lab-setup/scans/`.

**Optional full TCP discovery** (only on the authorized target):

```bash
sudo nmap -sS -p- -oA lab-setup/scans/full-tcp-scan <TARGET_IP>
```

**Do not invent scan output.** Replace `<TARGET_IP>` with the target VM's actual isolated address.

## 4. Test and document one vulnerability at a time

1. **Discover:** Check the running service and version in Nmap output.
2. **Enumerate:** Investigate the service further and save logs.
3. **Validate:** Check CVE/advisory prerequisites; a version match alone is not proof.
4. **Demonstrate:** Test with Metasploit and manually when appropriate; avoid persistence and destructive payloads.
5. **Record evidence:** Store service-specific logs in `vulnerabilities/<group>/VULN-###-name/scans/` and numbered screenshots in `screenshots/`.
6. **Report:** Document actual commands, results, CVE/CWE, categories, impact, remediation, references, and failures.
7. **Update GitHub:** Commit sanitized evidence and mark the [index](../FINDINGS-INDEX.md) with the actual verification status.

## 5. Save changes to GitHub

From the repository directory in Kali:

```bash
git status
git add README.md FINDINGS-INDEX.md lab-setup/ vulnerabilities/
git commit -m "docs: document first lab findings"
git push
```

Only commit files you intentionally reviewed. Never upload credentials, private keys, session data, or unrelated sensitive content.

**Next:** Open [VULN-001 vsftpd case study](../vulnerabilities/network/VULN-001-vsftpd-backdoor/README.md) if your scan confirms an applicable FTP service.
