import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    """Load expenses from JSON file or return empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_expenses(expenses):
    """Save the list of expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Prompt user to add a new expense record."""
    print("\n--- Add New Expense ---")
    description = input("Enter description (e.g., Groceries, Rent): ").strip()
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid numerical amount.")

    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip().capitalize()
    
    # Use current date or custom date
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date_str = datetime.today().strftime("%Y-%m-%d")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date_str
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Successfully recorded: '{description}' - ${amount:.2f}")

def view_monthly_summary(expenses):
    """Filter expenses by month (YYYY-MM) and display category breakdowns."""
    print("\n--- Monthly Expense Summary ---")
    month_input = input("Enter Month (YYYY-MM) or press Enter for current month: ").strip()
    
    if not month_input:
        month_input = datetime.today().strftime("%Y-%m")

    filtered = [e for e in expenses if e["date"].startswith(month_input)]
    
    if not filtered:
        print(f"No records found for {month_input}.")
        return

    total_spent = sum(e["amount"] for e in filtered)
    category_totals = {}
    
    for e in filtered:
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + e["amount"]

    print(f"\nExpenses for {month_input}:")
    print("-" * 35)
    for entry in filtered:
        print(f"{entry['date']} | {entry['category']:<12} | ${entry['amount']:<8.2f} | {entry['description']}")
    
    print("-" * 35)
    print(f"TOTAL SPENT: ${total_spent:.2f}\n")
    
    print("Breakdown by Category:")
    for cat, total in category_totals.items():
        percentage = (total / total_spent) * 100
        print(f" - {cat:<12}: ${total:.2f} ({percentage:.1f}%)")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_monthly_summary(expenses)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
