
class Expense:
    def __init__(self, expense_id: int, description: str):
        """
        Create an expense object.
        expense_id: unique identifier
        """

        self.id = expense_id
        self.description = description
        