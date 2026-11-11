# Lab setup and initial reconnaissance

## Architecture

| Component | Role | Network | Actual IP | Status |
| --- | --- | --- | --- | --- |
| Kali Linux | Tester | Isolated VM network | TBD | To verify |
| Metasploitable 2 | Training target | Same isolated VM network | TBD | To verify |

Use the same **Internal Network** (recommended) for both VMs. A correctly configured **Host-Only** network also works. Do not use Bridged Adapter for the vulnerable target or port-forward any of its services.

> Do not copy example IPs into the report as if they were real. Record actual address values only when you configure the VMs.

## Before starting
1. Power off both VMs.
2. In VirtualBox, open each VM → **Settings → Network**.
3. Connect both to the same named **Internal Network** (for example `vapt-lab`). An Internal Network often requires manual IP assignment if you have no lab DHCP server. Alternatively, configure Host-Only with suitable isolation and DHCP.
4. Keep Metasploitable 2 disconnected from any Bridged or NAT adapter while you are testing. If Kali needs internet for package updates, isolate that connectivity from the target and disable it during lab testing.
5. Take VM snapshots before exploitation.

## Identify target interfaces

On **Metasploitable 2**:

```bash
ifconfig
ip route
```

On **Kali Linux**:

```bash
ip -4 addr
ip route
```

Confirm both machines use reachable addresses on the same isolated subnet. If your Internal Network has no DHCP service, give each lab interface a unique static IP on the same subnet.

## Connectivity test

From Kali, after replacing the placeholder with the **actual isolated target IP**:

```bash
ping -c 3 <TARGET_IP>
```

Only continue when you have confirmed the target IP belongs to your own Metasploitable 2 VM.

## First baseline scan

```bash
mkdir -p lab-setup/scans
sudo nmap -sC -sV -oA lab-setup/scans/initial-service-scan <TARGET_IP>
```

**Note:** Run from a local clone of this repo in Kali; or save scans locally and copy sanitized results into this folder. The command creates `.nmap`, `.gnmap`, and `.xml` files.

### Optional full TCP discovery after baseline

```bash
sudo nmap -sS -p- --reason -oA lab-setup/scans/full-tcp-discovery <TARGET_IP>
```

These are **single-host scans** against the isolated VM. Do not scan unrelated networks.

## Scan documentation

| Date | Tool/version | Target | Filename | Key observations |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | Not yet scanned |

## Evidence policy
Sanitize before publishing; keep unmodified originals privately if they contain sensitive information. Record what was observed, not what was expected. Store screenshots and service-level results within the relevant vulnerability folder.
