# 👻 Ghost Scanner - Advanced Port Scanner

![Hacker Theme](https://img.shields.io/badge/Theme-Hacker-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

Ghost Scanner is a port scanning tool with stealth capabilities, OS detection, and vulnerability assessment features. Designed for cybersecurity professionals and ethical hackers, this tool provides a clean GUI interface for conducting network reconnaissance.

**Disclaimer**: This project is strictly for **educational** and **authorized cybersecurity research** purposes.  
> **Do not deploy this tool on systems you do not own or have written permission to test. Unauthorized use is illegal.**

## Features

- 🕵️‍♂️ **Stealth Scanning**: Uses SYN scanning technique for low-detection port scanning
- 💻 **OS Detection**: Identifies target operating systems using Nmap fingerprinting
- 🔍 **Vulnerability Assessment**: Checks for common vulnerabilities on open ports
- 📊 **GUI Interface**: User-friendly interface with progress tracking
- 📂 **Report Generation**: Automatically saves scan results to files
- 🎨 **Hacker Theme**: Sleek dark interface with terminal-style aesthetics

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ghost-scanner.git
   cd ghost-scanner
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Enter the target IP address in the input field
2. Click "Start Scan" to begin the scanning process
3. View results in the GUI or check the `results/` directory for saved reports

The scanner checks these ports by default:
- 21 (FTP)
- 22 (SSH)
- 80 (HTTP)
- 445 (SMB)
- 3306 (MySQL)

## Technical Details

- Uses Scapy for low-level packet manipulation
- Integrates Nmap for OS detection
- Implements threading for responsive GUI during scans
- Follows ethical scanning practices with proper connection termination

## Legal Notice

This tool is provided for educational purposes only. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use this tool on systems you own or have explicit permission to test.

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## License

MIT License - See LICENSE file for details.
> Buy me a coffee - _0xf89c84554c78B3194A56042bd803CcA62EA423E9_

👻 Ghost - Because even ghosts leave traces.
