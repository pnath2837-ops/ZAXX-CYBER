import os
import sys
import time


# ==============================
# ZAXX CYBER - VERSION 1.0
# ==============================

def clear():
    os.system("clear")


def loading():
    clear()

    print("\n[+] Starting ZAXX CYBER...\n")

    animation = [
        "[■□□□□□□□□□] 10%",
        "[■■□□□□□□□□] 20%",
        "[■■■□□□□□□□] 30%",
        "[■■■■□□□□□□] 40%",
        "[■■■■■□□□□□] 50%",
        "[■■■■■■□□□□] 60%",
        "[■■■■■■■□□□] 70%",
        "[■■■■■■■■□□] 80%",
        "[■■■■■■■■■□] 90%",
        "[■■■■■■■■■■] 100%"
    ]

    for frame in animation:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.15)

    time.sleep(0.5)


def banner():
    print("""
╔══════════════════════════════════════╗
║                                      ║
║  ███████╗  █████╗  ██╗  ██╗ ██╗  ║
║  ╚══███╔╝ ██╔══██╗ ╚██╗██╔╝ ╚██╗ ║
║     ███╔╝ ███████║  ╚███╔╝   ╚███ ║
║    ███╔╝  ██╔══██║  ██╔██╗   ██╔╝ ║
║   ███████╗██║  ██║ ██╔╝ ██╗ ██╔╝  ║
║   ╚══════╝╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝   ║
║                                      ║
║           ZAXX CYBER               ║
║            Version 1.0             ║
║                                      ║
╚══════════════════════════════════════╝
""")


def phone_info():
    print("\n[+] PHONE NUMBER INFO")

    number = input(
        "[>] Enter phone number with country code: "
    ).strip()

    print("\n======================================")
    print("[+] Number :", number)
    print("[+] Status : Number received")
    print(
        "[+] Note   : Detailed public information "
        "requires a legitimate lookup service."
    )
    print("======================================")

    input("\nPress Enter to continue...")


def mutual_phone_info():
    print("\n[+] MUTUAL PHONE NUMBER INFO")

    number = input(
        "[>] Enter phone number with country code: "
    ).strip()

    print("\n======================================")
    print("[+] Number :", number)
    print("[+] Status : Demo mode")
    print(
        "[+] No private account or contact data "
        "is accessed."
    )
    print("======================================")

    input("\nPress Enter to continue...")


def location_info():
    print("\n[+] LOCATION INFO")

    number = input(
        "[>] Enter phone number with country code: "
    ).strip()

    try:
        import phonenumbers
        from phonenumbers import geocoder

        parsed = phonenumbers.parse(number, None)

        region = geocoder.description_for_number(
            parsed,
            "en"
        )

        print("\n=========== LOCATION INFO ===========")
        print("[+] Number :", number)
        print(
            "[+] Region :",
            region if region else "Unknown"
        )
        print(
            "[+] Country Code : +"
            + str(parsed.country_code)
        )
        print(
            "[+] Note: This gives general "
            "number-region information only."
        )
        print("=====================================")

    except ImportError:
        print("\n[!] phonenumbers package is not installed.")
        print("[!] Run: pip install phonenumbers")

    except Exception:
        print("\n[!] Invalid phone number format.")

    input("\nPress Enter to continue...")


def number_links():
    print("\n[+] NUMBER LINKS")

    number = input(
        "[>] Enter phone number with country code: "
    ).strip()

    clean_number = (
        number
        .replace("+", "")
        .replace(" ", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
    )

    print("\n================ NUMBER LINKS ================")

    print(
        "[+] WhatsApp : "
        "https://wa.me/" + clean_number
    )

    print(
        "[+] Google    : "
        "https://www.google.com/search?q="
        + clean_number
    )

    print(
        "[+] Bing      : "
        "https://www.bing.com/search?q="
        + clean_number
    )

    print("==============================================")

    input("\nPress Enter to continue...")


def main():
    loading()

    while True:
        clear()

        banner()

        print("""
[1] Phone Number Info
[2] Mutual Phone Number Info
[3] Location Info
[4] Number to All Side Link
[5] Exit
""")

        choice = input("[>] Enter choice: ").strip()

        if choice == "1":
            phone_info()

        elif choice == "2":
            mutual_phone_info()

        elif choice == "3":
            location_info()

        elif choice == "4":
            number_links()

        elif choice == "5":
            clear()
            print("\nZAXX CYBER shutting down...")
            time.sleep(1)
            print("Goodbye!")
            break

        else:
            input(
                "\n[!] Invalid choice! "
                "Press Enter to continue..."
            )


if __name__ == "__main__":
    main()