import os
import time


def clear():
    os.system("clear")


def banner():
    clear()

    # Large ZAXX logo
    os.system("figlet -f big ZAXX")

    print("                 Version 1.0")
    print()


def main():
    while True:
        banner()

        print("[1] Phone Number Info")
        print("[2] Mutual Phone Number Info")
        print("[3] Location Info")
        print("[4] Number to All Side Link")
        print("[5] Exit")

        choice = input("\n[>] Enter choice: ").strip()

        if choice == "1":
            clear()
            banner()

            print("[+] Phone Number Info\n")
            number = input("[>] Enter phone number: ")

            print("\n[+] Number :", number)
            print("[+] Status : Number received")
            print("[+] Note   : Public information only.")

            input("\nPress Enter to continue...")

        elif choice == "2":
            clear()
            banner()

            print("[+] Mutual Phone Number Info\n")
            number = input("[>] Enter phone number: ")

            print("\n[+] Number :", number)
            print("[+] Status : Demo mode")
            print("[!] Private contacts or accounts are not accessed.")

            input("\nPress Enter to continue...")

        elif choice == "3":
            clear()
            banner()

            print("[+] Location Info\n")
            number = input("[>] Enter phone number: ")

            print("\n[+] Number :", number)
            print("[+] Result : General region information only")
            print("[!] Exact live location cannot be obtained from a phone number alone.")

            input("\nPress Enter to continue...")

        elif choice == "4":
            clear()
            banner()

            print("[+] Number to All Side Link\n")
            number = input("[>] Enter phone number: ")

            clean = (
                number.replace("+", "")
                .replace(" ", "")
                .replace("-", "")
            )

            print("\n=============== NUMBER LINKS ===============")
            print("[+] WhatsApp : https://wa.me/" + clean)
            print("[+] Google   : https://www.google.com/search?q=" + clean)
            print("[+] Bing     : https://www.bing.com/search?q=" + clean)
            print("=============================================")

            input("\nPress Enter to continue...")

        elif choice == "5":
            clear()
            print("\nGoodbye! ZAXX CYBER\n")
            break

        else:
            print("\n[!] Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    main()