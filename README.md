# Ghost Scanner - Advanced Port Scanner

## Description

Ghost Scanner is an advanced, customizable Python-based port scanner with a graphical user interface (GUI) built using `customtkinter`. This tool is designed to scan open ports on a target IP address, detect the operating system (OS), and check for vulnerabilities based on the open ports detected. The application utilizes `nmap` for OS detection and performs vulnerability checks based on known port services like FTP and SMB.

This project is suitable for anyone interested in cybersecurity and penetration testing, offering a quick way to scan and assess the security of networks.

## Features

- **Port Scanning:** Detects open ports on the target IP.
- **OS Detection:** Identifies the operating system running on the target.
- **Vulnerability Checking:** Checks known vulnerabilities for open ports.
- **Progress Bar:** Displays the status of the scan.
- **Threaded Scanning:** Runs the scan in a separate thread to keep the GUI responsive.
- **Customizable Ports List:** The port list can be expanded or modified as needed.
- **GUI with CustomTkinter:** A user-friendly interface with dark mode and a "ghost" theme.

## Technologies Used

- **Python:** The primary language used to write the script.
- **CustomTkinter:** For building the GUI interface.
- **Nmap:** For OS detection and port scanning.
- **Scapy:** For low-level network scanning.
- **Threading:** For handling background processes.

## Prerequisites

Before running Ghost Scanner, ensure you have the following:

1. **Python 3.x** installed on your system.
2. **Pip** (Python’s package installer) installed.

### Required Python Libraries

This project uses the following Python libraries:

- `customtkinter`: For creating the GUI.
- `scapy`: For crafting and sending network packets.
- `nmap`: For OS detection and port scanning.
- `threading`: For handling background processes.

You can install these libraries by running the following commands in your terminal or command prompt:

```bash
pip install customtkinter scapy python-nmap threading
