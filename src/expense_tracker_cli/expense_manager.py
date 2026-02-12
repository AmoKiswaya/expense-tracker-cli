from expense_tracker_cli.expense import Expense
import json

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
        return max(self._expenses.keys()) + 1 
    
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

    def list_expenses(Self):
        pass

    def expenses_summary(self):
        pass

    def delete_expense(self):
        pass

    def save_expenses(self):
        data = {}

        for expense_id, expense in self._expenses.items():
            data[expense_id] = expense.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(data, file)
    
    def load_expenses():
        pass