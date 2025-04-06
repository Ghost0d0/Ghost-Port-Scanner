import nmap
from scapy.all import *
import os

# Dictionary of vulnerable ports
vulnerabilities = {
    21: "FTP (Check for Anonymous Login)",
    22: "SSH (Check for weak passwords)",
    23: "Telnet (Unencrypted, very vulnerable)",
    80: "HTTP (Check for outdated web servers)",
    139: "NetBIOS (Can be exploited for SMB attacks)",
    445: "SMB (Check for EternalBlue exploit)",
    3306: "MySQL (Check for weak database passwords)"
}

# Function to detect OS
def detect_os(target_ip):
    nm = nmap.PortScanner()
    try:
        nm.scan(target_ip, arguments="-O")
        os_info = nm[target_ip]['osmatch'][0]['name']
        return os_info
    except:
        return "Unknown OS"

# Function to check for vulnerabilities
def check_vulnerabilities(open_ports):
    warnings = []
    for port in open_ports:
        if port in vulnerabilities:
            warnings.append(f"Port {port}: {vulnerabilities[port]}")
    return warnings

# Function for stealth port scanning
def stealth_scan(target_ip, ports):
    open_ports = []
    for port in ports:
        src_port = RandShort()
        syn_packet = IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=0)
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
            rst_packet = IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="R")
            send(rst_packet, verbose=0)
    return open_ports

# Function to save results
def save_results(target_ip, open_ports, os_detected, vulnerabilities_found):
    if not os.path.exists("results"):
        os.makedirs("results")

    with open(f"results/{target_ip}_scan.txt", "w") as file:
        file.write(f"Target: {target_ip}\n")
        file.write(f"OS Detected: {os_detected}\n")
        file.write(f"Open Ports: {', '.join(map(str, open_ports))}\n")
        if vulnerabilities_found:
            file.write("Vulnerabilities:\n" + "\n".join(vulnerabilities_found))
        else:
            file.write("No known vulnerabilities detected.\n")
