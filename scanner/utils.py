def get_service(port):
    common_ports = {
        21: "FTP",
        22: "SSH",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        8080: "HTTP-ALT"
    }

    return common_ports.get(port, "Unknown")
