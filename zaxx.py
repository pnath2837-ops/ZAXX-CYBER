import os
import sys
import time

def clear():
    os.system("clear")

# Loading Animation
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
    time.sleep(0.2)

time.sleep(1)

while True:
    clear()

    print("""
╔══════════════════════════════════════════════╗
║                                              ║
║ ███████╗ █████╗ ██╗  ██╗██╗  ██╗             ║
║ ╚══███╔╝██╔══██╗╚██╗██╔╝╚██╗██╔╝             ║
║   ███╔╝ ███████║ ╚███╔╝  ╚███╔╝              ║
║  ███╔╝  ██╔══██║ ██╔██╗  ██╔██╗              ║
║ ███████╗██║  ██║██╔╝ ██╗██╔╝ ██╗             ║
║ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝             ║
║                                              ║
║               ZAXX CYBER                     ║
║                Version 1.0                   ║
║                                              ║
╚══════════════════════════════════════════════╝

[1] Phone Number Info
[2] Mutual Phone Number Info
[3] Location Info
[4] Number to All Side Link
[5] Help
[6] Exit
""")

    choice = input("\n[>] Enter choice: ")

    if choice == "1":
    print("\n[+] Phone Number Info")
    number = input("[>] Enter phone number: ")

    print("\n[+] Number:", number)
    print("[+] Country information: Entered number received.")
    print("[+] Note: Detailed public information requires a phone-number lookup service.")

    input("\nPress Enter to continue...")

    elif choice == "2":
        print("\nDemo Menu")
        input("\nPress Enter to continue...")

    elif choice == "3":
    print("\n[+] Location Info")
    number = input("[>] Enter phone number with country code: ")

    try:
        import phonenumbers
        from phonenumbers import geocoder

        parsed = phonenumbers.parse(number, None)
        region = geocoder.description_for_number(parsed, "en")

        print("\n========== LOCATION INFO ==========")
        print("[+] Number :", number)
        print("[+] Region :", region or "Unknown")
        print("[+] Country Code :", "+" + str(parsed.country_code))
        print("[+] Note: This is general region information.")
        print("[+] Live/private location is not available.")
        print("===================================")

    except Exception:
        print("\n[!] Invalid phone number format.")

    input("\nPress Enter to continue...")

    elif choice == "4":
    print("\n[+] Number Links")
    number = input("[>] Enter phone number with country code: ")

    # Remove spaces and + for link generation
    clean_number = number.replace("+", "").replace(" ", "").replace("-", "")

    print("\n========== NUMBER LINKS ==========")
    print("[+] WhatsApp : https://wa.me/" + clean_number)
    print("[+] Google   : https://www.google.com/search?q=" + clean_number)
    print("[+] Bing     : https://www.bing.com/search?q=" + clean_number)
    print("===================================")

    input("\nPress Enter to continue...")

 
    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        input("\nInvalid choice! Press Enter...")