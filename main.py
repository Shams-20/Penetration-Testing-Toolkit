from modules import port_scanner, brute_forcer
from utils.helper_funcs import validate_ip

def main():
    while True:
        print("\n=== PENETRATION TESTING TOOLKIT ===")
        print("1. Port Scanner")
        print("2. Brute-Forcer")
        print("3. Exit")

        choice = input("Select module: ")

        if choice == "1":
            target = input("Enter target IP: ")
            if validate_ip(target):
                port_scanner.scan_ports(target)
            else:
                print("Invalid IP, dumbass. Try again!")
        elif choice == "2":
            target = input("Enter target IP: ")
            if validate_ip(target):
                brute_forcer.run_brute_force(target)
            else:
                print("Invalid IP, dumbass. Try again!")
        elif choice == "3":
            print("Exiting... cya, script kiddie 😎")
            break
        else:
            print("Invalid choice, dumbass. Try again!")
