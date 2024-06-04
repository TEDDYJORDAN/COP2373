from functools import reduce

def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    return expenses

def analyze_expenses(expenses):
    if not expenses:
        return None, None, None

    total_expense = reduce(lambda x, y: x + y[1], expenses, 0)
    highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
    lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    return total_expense, highest_expense, lowest_expense

def main():
    expenses = get_expenses()
    total_expense, highest_expense, lowest_expense = analyze_expenses(expenses)

    if total_expense is None:
        print("No expenses entered.")
    else:
        print(f"\nTotal Expense: ${total_expense:.2f}")
        print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
        print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

if __name__ == "__main__":
    main()