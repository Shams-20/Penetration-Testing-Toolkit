# modules/port_scanner.py
import socket

def scan_ports(target):
    print(f"Scanning ports on {target}...")
    for port in range(20, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    print("Port scanning completed.")   