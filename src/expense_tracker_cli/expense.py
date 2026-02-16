from datetime import datetime


class Expense:
    def __init__(self, expense_id: int, description: str, amount: float,
                 created_at: str = None, updated_at: str = None):
        """
        Create an expense object.
        expense_id: unique identifier
        """

        self.id = expense_id
        self.description = description
        self.amount = amount
        now = f"{datetime.now():%d-%m-%YT%H:%M:%S}"

        self.createdAt = created_at or now 
        self.updatedAt = updated_at or now 

    @classmethod
    def from_dict(cls, data: dict):
        return cls (
            expense_id=data["id"],
            description=data.get("description"),
            amount=data.get("amount"),
            created_at = data.get("createdAt"), 
            updated_at = data.get("updatedAt") 
        )

    def to_dict(self):
        """
        Convert expense object to a dictionary for JSON storage.
        """
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }


    def update(self, description: str, amount: float):
        if amount is not None:
            if float(amount) <= 0:
                return "Amount should be greater than 0"
            self.amount = float(amount)

        if description is not None:
            self.description = description

        self.updatedAt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")