# Project progress

[← Project home](README.md) · [Lab instructions](lab-setup/README.md)

## Phase 1 — Prepare
- [x] Create GitHub repository and simple folder structure
- [x] Add candidate index with categories and CVE references
- [x] Prepare 89 individual vulnerability report folders (48 Network, 9 DVWA, 32 Mutillidae)
- [ ] Check isolated Kali and Metasploitable 2 networking
- [ ] Take VM snapshots
- [x] Record VM IP addresses (Kali `192.168.95.128`; target `192.168.95.131`)

## Phase 2 — Discover
- [x] Run initial full TCP Nmap scan (29 ports reported)
- [ ] Copy original Nmap output from Kali into `lab-setup/scans/` and upload real screenshot
- [x] Choose first candidate based on real scan results (VULN-001 vsftpd 2.3.4)

## Phase 3 — Document first finding
- [ ] Enumerate the service
- [ ] Test using Metasploit (if applicable)
- [ ] Test manually (if applicable)
- [ ] Add real screenshots and scan results to `VULN-001`
- [ ] Explain observed impact and remediation
- [ ] Update catalog verification status and push to GitHub

## Phase 4 — Build portfolio
- [ ] Document further verified cases one by one
- [ ] Prepare the final consolidated report using the template

**Rule:** Do not mark testing completed until supported by actual evidence.
