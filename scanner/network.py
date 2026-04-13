import scapy.all as scapy


def scan_network_once(ip_range, timeout=5):
    """
    Performs a single ARP scan
    """
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(
        arp_request_broadcast,
        timeout=timeout,
        verbose=False
    )[0]

    devices = []

    for element in answered_list:
        device_info = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }
        devices.append(device_info)

    return devices


def scan_network(ip_range, attempts=3):
    """
    Performs multiple scans and merges results
    """
    all_devices = {}

    for i in range(attempts):
        print(f"[+] Scan attempt {i+1}/{attempts}...")
        devices = scan_network_once(ip_range)

        for d in devices:
            all_devices[d["ip"]] = d  # remove duplicates by IP

    final_devices = list(all_devices.values())

    print(f"\n[+] Found {len(final_devices)} unique devices\n")

    return final_devices
