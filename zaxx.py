print("Welcome to ZAXX CYBER")

while True:
    print("\n[1] About")
    print("[2] Help")
    print("[0] Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        print("ZAXX CYBER Project")
    elif choice == "2":
        print("Help Menu")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option")