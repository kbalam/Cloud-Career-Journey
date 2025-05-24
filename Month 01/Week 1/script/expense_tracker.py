import os

# ---------- Functions ----------
script_dir = os.path.dirname(os.path.abspath(__file__))

output_dir = os.path.join(script_dir, "..", "output")
os.makedirs(output_dir, exist_ok=True)  

file_path = os.path.join(output_dir, "expenses.txt")

def add_expense(date, category, amount, note):
    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number.")
        return

    try:
        with open(file_path, "a") as file:
            file.write(f"{date},{category},{amount},{note}\n")
        print("Expense added successfully!")
    except IOError as e:
        print(f"Error writing to file: {e}")



def view_expenses():
    if not os.path.exists(file_path):
        print("No expenses found.")
        return

    total = 0.0
    print("\nAll Expenses:")
    print("-" * 40)
    try:
        with open(file_path, "r") as file:
            for line in file:
                try:
                    date, category, amount, note = line.strip().split(",", 3)
                    print(f"{date} | {category} | ₹{amount} | {note}")
                    total += float(amount)
                except ValueError:
                    print(f"Skipping malformed line: {line.strip()}")
    except IOError as e:
        print(f"Error reading file: {e}")
        return

    print("-" * 40)
    print(f"💰 Total Spent: ₹{total:.2f}\n")


def show_menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Exit")

# ---------- Main Program ----------

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Travel, etc.): ")
            amount = input("Enter amount: ")
            note = input("Enter note: ")
            add_expense(date, category, amount, note)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            print("Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
