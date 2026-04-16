# 🔍 Network Reconnaissance Tool

A multi-threaded network reconnaissance tool built using Python that performs **ARP-based device discovery** and **TCP port scanning** with **service detection** and **banner grabbing**.

<br>

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

<br>

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

<br>

## 🛠️ Tech Stack

- Python 3
- Socket Programming
- Threading
- Scapy (for ARP scanning)
- argparse (CLI interface)
- tqdm (progress bar)
- logging

<br>

## ▶️ Usage

🔹 Scan a Single Target
python main.py --target scanme.nmap.org --start 20 --end 1000

🔹 Scan Local Network (requires root)
sudo venv/bin/python main.py --network 192.168.1.0/24 --start 20 --end 1000

<br>

##  📄 Sample Output

-{
-   "target": "192.168.X.X",
-   "mac": "12:34:56:78:90:11",
-   "port": 80,
-   "status": "open",
-   "service": "HTTP",
-   "banner": "HTTP/1.1 200 OK..."
-}

<br> 

##  📁 Output Files

- results/<target>.json → Scan results
- scanner.log → Logging information

<br>

##  ⚠️ Disclaimer

This tool is intended for educational and authorized testing purposes only.
Do not use it on networks or systems without proper permission.
