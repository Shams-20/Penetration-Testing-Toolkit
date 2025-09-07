from modules import port_scanner, brute_forcer

def main():
    while True:
        print("=== PENETRATION TESTING TOOLKIT ===")
        print("1. Port Scanner")
        print("2. Brute-Forcer")
        print("3. Exit")
        choice = input("Select module: ")

        if choice == "1":
            target = input("Enter target IP: ")
            port_scanner.scan_ports(target)
        elif choice == "2":
            target = input("Enter target IP: ")
            brute_forcer.run_brute_force(target)
        elif choice == "3":
            print("Exiting... bye hacker!")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
