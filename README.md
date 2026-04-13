# 🔍 Network Reconnaissance Tool

A multi-threaded network reconnaissance tool built using Python that performs **ARP-based device discovery** and **TCP port scanning** with **service detection** and **banner grabbing**.

---

## 🚀 Features

- 🔎 Discover active devices on a local network (ARP scan)
- 🌐 Scan open ports on single or multiple targets
- ⚡ Multi-threaded scanning for high performance
- 🏷️ Service detection (HTTP, FTP, SMB, etc.)
- 📡 Banner grabbing for deeper inspection
- 📊 Real-time progress tracking with tqdm
- 📝 Logging system for scan activity
- 📄 Export results in structured JSON format
- 🔗 Supports both single-target and full network scanning

---

## 🧠 How It Works

1. **Network Discovery (ARP)**
   - Sends ARP requests to identify active devices
   - Collects IP and MAC addresses

2. **Port Scanning (TCP)**
   - Performs TCP connect scan on each device
   - Identifies open ports

3. **Service Detection & Banner Grabbing**
   - Maps ports to common services
   - Sends protocol-specific requests (HTTP, SMTP, etc.)
   - Extracts banners for service identification

---

## 🛠️ Tech Stack

- Python 3
- Socket Programming
- Threading
- Scapy (for ARP scanning)
- argparse (CLI interface)
- tqdm (progress bar)
- logging

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/network-recon-tool.git
cd network-recon-tool

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt# Network-Reconnaissance-Tool
