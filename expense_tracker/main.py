"""Entry point for the Expense Tracker.

Run from the day8_project folder with:
    python -m expense_tracker.main
"""

from expense_tracker.expenses import add_expense, show_total, view_expenses


def show_menu():
    """Print the menu options."""
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")


def main():
    """Run the menu loop until the user exits."""
    expenses = []

    try:
        while True:
            show_menu()
            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                add_expense(expenses)
            elif choice == "2":
                view_expenses(expenses)
            elif choice == "3":
                show_total(expenses)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended. Exiting Expense Tracker. Goodbye!")


if __name__ == "__main__":
    main()
