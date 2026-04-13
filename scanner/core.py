import socket

def scan_port(target, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            s.close()
            return True
        s.close()
        return False

    except Exception:
        return False
