import sqlite3

conn = sqlite3.connect("./database.db")
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        type TEXT,
        amount REAL
    )
    """)
    conn.commit()

create_tables()

def register_income():
    amount = float(input("Enter the income amount: "))
    cursor.execute("INSERT INTO transactions (type, amount) VALUES (?, ?)", ("income", amount))
    conn.commit()
    print("Income registered successfully!")

def register_expense():
    amount = float(input("Enter the expense amount: "))
    cursor.execute("INSERT INTO transactions (type, amount) VALUES (?, ?)", ("expense", amount))
    conn.commit()
    print("Expense registered successfully!")

def display_total_balance():
    cursor.execute("SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END) FROM transactions")
    total_balance = cursor.fetchone()[0]
    print(f"Total balance: {total_balance:.2f}")

def display_diff():
    cursor.execute("SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END) FROM transactions")
    total_balance = cursor.fetchone()[0]

    print("Transaction Details:")
    cursor.execute("SELECT type, amount FROM transactions")
    transactions = cursor.fetchall()

    for transaction in transactions:
        sign = "+" if transaction[0] == "income" else "-"
        print(f"{sign} {transaction[1]:.2f} {transaction[0]}")

    print(f"\nTotal balance: {total_balance:.2f}")
    if total_balance < 0:
        print("Your balance is in deficit.")
    elif total_balance > 0:
        print("Your balance is positive.")
    else:
        print("Your balance is neutral.")

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
