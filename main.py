def register_income():
    pass

def register_expense():
    pass

def display_total_balance():
    pass

def display_diff():
    pass

def show_logs():
    pass

def main():
    while True:
        print("-- Finance APP --")
        print("What do you want to do")
        print("1 - Register income")
        print("2 - Register expense")
        print("3 - Display total balance")
        print("4 - Display diff")
        print("5 - Show logs")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_income()
        elif choice == "2":
            register_expense()
        elif choice == "3":
            display_total_balance()
        elif choice == "4":
            display_diff()
        elif choice == "5":
            show_logs()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
