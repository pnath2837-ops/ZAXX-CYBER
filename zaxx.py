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
        print("\nPhone Number Info")
        input("\nPress Enter to continue...")

    elif choice == "2":
        print("\nDemo Menu")
        input("\nPress Enter to continue...")

    elif choice == "3":
        print("\nRegion Information")
        input("\nPress Enter to continue...")

    elif choice == "4":
        print("\nDemo Menu")
        input("\nPress Enter to continue...")

    elif choice == "5":
        print("\nHelp Menu")
        input("\nPress Enter to continue...")

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        input("\nInvalid choice! Press Enter...")