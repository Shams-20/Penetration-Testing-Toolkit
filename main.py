from modules import port_scanner, brute_forcer, web_scanner
from utils.helper_funcs import validate_ip

def print_menu():
    print("\n=== PENETRATION TESTING TOOLKIT ===")
    print("1. Port Scanner")
    print("2. Brute-Forcer")
    print("3. Web Scanner")
    print("4. Exit")

def main():
    while True:
        print_menu()
        choice = input("Select module: ").strip()

        if choice == "1":
            ip = input("Enter target IP: ")
            if validate_ip(ip):
                port_scanner.run(ip)
            else:
                print("❌ Invalid IP")
        elif choice == "2":
            ip = input("Enter target IP: ")
            port = int(input("Enter target port: "))
            wordlist = input("Enter path to wordlist: ")
            brute_forcer.run(ip, port, wordlist)
        elif choice == "3":
            url = input("Enter target URL: ")
            web_scanner.run(url)
        elif choice == "4":
            print("👋 Exiting Toolkit...")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
