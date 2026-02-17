import argparse
from expense_tracker_cli.expense_manager import ExpenseManager

def main():
    parser = argparse.ArgumentParser(
        prog="ExpenseTracker",
        description="Expense Tracker for managing expenses through the terminal"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add new expense")
    add_parser.add_argument("--description", help="Expense description", required=True)
    add_parser.add_argument("--amount", help="Expense amount", required=True) 

    subparsers.add_parser("list", help="List all expenses") 
    
    summary_parser = subparsers.add_parser("summary", help="Show total expense summary")
    summary_parser.add_argument("--month", type=int, choices=range(1, 13),
                                metavar="MONTH", help="Month number (1-12) for monthly summary")


    update_expenses = subparsers.add_parser("update", help="Update Expense")
    update_expenses.add_argument("--id", type=int, help="Expense's id", required=True)
    update_expenses.add_argument("--description", type=str, help="New description")
    update_expenses.add_argument("--amount", type=float, help="New amount") 

    delete_parser = subparsers.add_parser("delete", help="delete an expense")
    delete_parser.add_argument("id", type=int, help="Expense ID") 

    args = parser.parse_args()
    manager = ExpenseManager()

    if args.command == "add":
        expense = manager.add_expense(amount=args.amount, description=args.description)

        if isinstance(expense, str):
            print(f"Error: {expense}") 
        else:
            print(f"Expense added successfully (ID: {expense.id})")


    elif args.command == "list":
        expenses = manager.list_expenses()

        if not expenses:
            print("No expenses found")
            return
        
        print(f"{'ID':<5} {'Date':<22} {'Description':<20} {'Amount':>10}")
        print("-" * 60)
        for e in expenses:
            print(f"{e.id:<5} {e.createdAt:<22} {e.description:<20} ${e.amount:>9.2f}")


    elif args.command == "update":
        try:
            expense = manager.update_expense(
                expense_id=args.id,
                description=args.description,
                amount=args.amount
            )
            print(f"Expense {args.id} updated successfully")

        except ValueError as e:
            print(e)
            return
        
    elif args.command == "delete":
        try:
            manager.delete_expense(id=args.id)

        except ValueError as e:
            print(e)

    elif args.command == "summary":
        if args.month:
            manager.monthly_summary(args.month)
        else:
            manager.expenses_summary()

    else:
        parser.print_help()  



if __name__ == "__main__":
    main()
