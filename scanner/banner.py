import socket
import ssl


def get_payload(target, port):
    """
    Returns protocol-specific payload based on port
    """
    payloads = {
        80: f"GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n".encode(),
        8080: f"GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n".encode(),
        25: b"HELO example.com\r\n",  # SMTP
    }

    return payloads.get(port, b"\r\n")  # fallback


def grab_banner(target, port):
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        # Handle HTTPS separately
        if port == 443:
            context = ssl.create_default_context()
            wrapped_socket = context.wrap_socket(s, server_hostname=target)
            wrapped_socket.connect((target, port))

            payload = f"GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n".encode()
            wrapped_socket.send(payload)

            banner = wrapped_socket.recv(2048)
            wrapped_socket.close()

        else:
            s.connect((target, port))

            payload = get_payload(target, port)
            s.send(payload)

            banner = s.recv(2048)
            s.close()

        return banner.decode(errors="ignore").strip()

    except Exception:
        return None
