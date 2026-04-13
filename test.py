from scanner.network import scan_network

devices = scan_network("192.168.1.0/24")

for d in devices:
    print(d)
