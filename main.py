from modules import port_scanner, brute_forcer, web_scanner
from utils.helper_funcs import validate_ip

def main():
    while True:
        print("\n=== PENETRATION TESTING TOOLKIT ===")
        print("1. Port Scanner")
        print("2. Brute-Forcer")
        print("3. Web Scanner")
        print("4. Exit")

        choice = input("Select module: ")

        if choice == "1":
            target = input("Enter target IP: ")
            if validate_ip(target):
                port_scanner.scan_ports(target)
            else:
                print("Invalid IP, dumbass. Try again!")

        elif choice == "2":
            target = input("Enter target IP: ")
            if not validate_ip(target):
                print("Invalid IP, dumbass. Try again!")
                continue

            port_input = input("Enter SSH port (default 22): ")
            port = int(port_input) if port_input.isdigit() else 22

            wordlist_path = input("Enter path to password wordlist (or leave empty for default): ")
            if not wordlist_path:
                wordlist_path = "default_wordlist.txt"

            brute_forcer.run_brute_force(target, port, wordlist_path)

        elif choice == "3":
            url = input("Enter target URL (e.g. http://example.com): ")
            if url.startswith("http"):
                web_scanner.scan_website(url)
            else:
                print("Invalid URL, dumbass. Try again!")

        elif choice == "4":
            print("Exiting... cya, script kiddie 😎")
            break
        else:
            print("Invalid choice, dumbass. Try again!")
