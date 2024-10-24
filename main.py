#budget_tracker
from expense import Expense
import calendar
import datetime


def main():
    print("Running expense tracker")
    expense_file_path = "expenses.csv"
    budget = 2053
    
    # Get user input for expense

    expenses = get_user_expenses()


    # write their expense to a file

    save_expense_to_file(expenses, expense_file_path)

    # read file and summarize expenses

    summarise_expenses(expense_file_path, budget)





def get_user_expenses():
    print("Getting user expenses")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "🍔Food",
        "🏡Home",
        "🚤Travel",
        "🍻Fun",
        "💈Misc"

    ]

    

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")


        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount )
            return new_expense
        else:
            print("Invalid category. Please try again.")


        
    

    







def save_expense_to_file(expenses:Expense, expense_file_path):
    print(f"Saving user expenses: {expenses} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expenses.name}, {expenses.category}, {expenses.amount}\n")



def summarise_expenses(expense_file_path, budget):
    print(f"Summarising user expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expenses_name, expenses_category, expenses_amount = line.strip().split(",")
            line_expense = Expense(
                    name = expenses_name, amount = float(expenses_amount), category = expenses_category
                    )
            
            expenses.append(line_expense)
    
    category_amounts = {}
    for expense in expenses:
        key = expense.category
        if key in category_amounts:
            category_amounts[key] += expense.amount
        else:
            category_amounts[key] = expense.amount

    
    
    
    
    print("Expenses by Category")
    for key, amount in category_amounts.items():
        print(f"  {key}: £{amount:.2f}")


    total_spent = sum({ex.amount for ex in expenses})
    print(f"💹Total spent:  £{total_spent:.2f} this month! ")

    remaining_budget = budget - total_spent
    print(f"👉Budget remaining:  £{remaining_budget:.2f}")


    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    

    daily_budget = remaining_budget / remaining_days
    print(f"⌛Budget per day:  £{daily_budget}")

    




if __name__ == "__main__":
    main()