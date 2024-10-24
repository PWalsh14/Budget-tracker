""" Budget tracker and Planner """

"""
Features I want to include:
- Ability to add income and expenses 
- Categorizing expenses
- Visualisation of spending habits
- Alert system for overspending or nearing budget limits

"""


""" 
REQUIREMENTS
- user enters expenses/income
- save expense/income to csv file
- summarise expense totals
- show remaining budget

"""

#budget class
# name 
# category 
# amount

class Expense:

    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount


    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, £{self.amount:.2f} >"
        
