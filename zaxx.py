import os
import time


def clear():
    os.system("clear")


def banner():
    clear()

    print(r"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║       ███████╗ █████╗ ██╗  ██╗██╗  ██╗                            ║
║       ╚══███╔╝██╔══██╗╚██╗██╔╝╚██╗██╔╝                            ║
║          ███╔╝ ███████║ ╚███╔╝  ╚███╔╝                             ║
║         ███╔╝  ██╔══██║ ██╔██╗  ██╔██╗                             ║
║        ███████╗██║  ██║██╔╝ ██╗██╔╝ ██╗                            ║
║        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                            ║
║                                                                      ║
║                         ZAXX CYBER                                   ║
║                         Version 1.0                                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    print()


def pause():
    input("\nPress Enter to continue...")


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

            banner()

            print("[+] Phone Number Info\n")

            number = input("[>] Enter phone number: ")

            print("\n======================================")
            print("[+] Number :", number)
            print("[+] Status : Number received")
            print("[+] Note   : Public information only.")
            print("======================================")

            pause()

        elif choice == "2":

            banner()

            print("[+] Mutual Phone Number Info\n")

            number = input("[>] Enter phone number: ")

            print("\n======================================")
            print("[+] Number :", number)
            print("[+] Status : Demo mode")
            print("[!] Private contacts/accounts are not accessed.")
            print("======================================")

            pause()

        elif choice == "3":

            banner()

            print("[+] Location Info\n")

            number = input("[>] Enter phone number: ")

            print("\n======================================")
            print("[+] Number :", number)
            print("[+] Result : General region information only")
            print("[!] Exact live location is not available.")
            print("======================================")

            pause()

        elif choice == "4":

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

            pause()

        elif choice == "5":

            clear()

            print("""
╔══════════════════════════════════════╗
║                                      ║
║             ZAXX CYBER              ║
║             Version 1.0             ║
║                                      ║
║              Goodbye!               ║
║                                      ║
╚══════════════════════════════════════╝
""")

            break

        else:

            print("\n[!] Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    main()