from expense_tracker_cli.expense import Expense
import json
from datetime import datetime
import calendar

class ExpenseManager:
    __file_path = "expenses.json"

    def __init__(self):
        self._expenses = {}
        self.load_expenses()

    def expense_id_generate(self):
        """
        Create a unique expense ID based on existing expenses.
        """    

        if not self._expenses:
            return 1
        return max(int(k) for k in self._expenses.keys()) + 1  
    
    def add_expense(self, amount, description):
        try:
            amount = float(amount)
        except ValueError:
            return "Invalid amount. Please enter a number" 

        if amount <= 0:
            return "Amount should be greater than 0"

        new_id = self.expense_id_generate()
        expense = Expense(new_id, description=description, amount=amount)
        self._expenses[new_id] = expense
        self.save_expenses()     
        
        return expense

    def list_expenses(self):
        if not self._expenses:
            return []
        expenses = self._expenses.values()
        return list(self._expenses.values())


    def update_expense(self, expense_id:int, description: str, amount: float):
        expense = self._expenses.get(expense_id) or self._expenses.get(str(expense_id))

        if not expense:
            raise ValueError(f"Expense with id {expense_id} does not exist")

        expense.update(description=description, amount=amount) 
        self.save_expenses()

        return expense 

    def expenses_summary(self):
        if not self._expenses:
            return "No expenses found."
        
        total_amount = sum(expense.amount for expense in self._expenses.values())
        print(f"Total expenses: {total_amount:.2f}")
        
    def monthly_summary(self, month: int):
        if not self._expenses:
            return "No expenses found"
        
        
        month_expenses = [
            expense for expense in self._expenses.values()
            if datetime.strptime(expense.updatedAt, "%d-%m-%YT%H:%M:%S").month == int(month)
        ]

        total_amount = sum(expense.amount for expense in month_expenses)
        print(f"Total expenses for {calendar.month_name[int(month)]}: ${total_amount:.2f}")

    def delete_expense(self, id): 
        try:
            expense_id = int(id)

        except ValueError:
            return "Invalid input. Please enter an integer"
        
        if id not in self._expenses:
            raise ValueError(f"Expense with id {expense_id} not found")

        expense = self._expenses[expense_id]
        del self._expenses[expense_id]
        self.save_expenses()
        return expense
        

    def save_expenses(self):
        data = {}

        for expense_id, expense in self._expenses.items():
            data[expense_id] = expense.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    
    def load_expenses(self):
        """Load existing expenses from JSON file"""
        try:
            with open(ExpenseManager.__file_path, "r") as file: 
                expenses_list = json.load(file)
                for expense_id, expense_data in expenses_list.items():
                   expense_obj = Expense.from_dict(expense_data)
                   self._expenses[expense_id] = expense_obj 

        except FileNotFoundError:
            self._expenses = []
        except json.JSONDecodeError:
            self._expenses = []