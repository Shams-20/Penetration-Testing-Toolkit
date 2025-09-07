import socket
from threading import Thread

# Top ports to scan
TOP_PORTS = [22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    sock.close()

def scan_ports(target):
    print(f"\n[+] Scanning top ports on {target}...\n")
    threads = []

    for port in TOP_PORTS:
        t = Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Scan complete!")
