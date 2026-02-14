from datetime import datetime


class Expense:
    def __init__(self, expense_id: int, description: str, amount):
        """
        Create an expense object.
        expense_id: unique identifier
        """

        self.id = expense_id
        self.description = description
        self.amount = amount
        self.createdAt = f"{datetime.now():%d-%m-%YT%H:%M:%S}" 

    @classmethod
    def from_dict(cls, data: dict):
        return cls (
            expense_id=data["id"],
            description=data.get("description", ""),
            amount=data.get("amount"),
            created_at = data.get("createdAt") 
        )

    def to_dict(self):
        """
        Convert expense object to a dictionary for JSON storage.
        """
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "createdAt": self.createdAt
        }
