## Expense Tracker
An expense tracker application that manages one's finances. The application comes with features such as add, delete, and view expenses that can be performed on the terminal. The application also provides a summary of the expenses.  

### Features
- Runs from the Terminal.
- Creates expenses using add command and stores them in JSON file and memory.
- Deletes expenses in JSON file and memory using delete command. 
- Updates an expense using update command.
- Lists stored expenses as python object using list command. 
- Shows total expenses summary using summary command.
- Shows total monthly summary using summary command and --month as an option.
- Displays results output in a formatted version in the terminal's output.
- Handles errors such as ValueError.

### Requirements
- Python 3.10+ 

### Installation
1. Clone repository 
```
git clone git@github.com:AmoKiswaya/expense-tracker-cli.git
```
2. Install dependencies in editable mode
```bash
pip install -e .
```

### Usage 
Use expense-tracker command to perform the following actions after installing dependencies.

```bash
# Create an expense
expense-tracker add --description "GYM" --amount 100
expense-tracker add --description "TOKYO VACATION" --amount 2000
# Output 1
Expense added successfully (ID: 1)
# Output 2
Expense added successfully (ID: 2)


# List expenses from memory
expense-tracker list
# Output 
ID    Date                   Description              Amount
------------------------------------------------------------
1     17-02-2026T12:17:32    GYM                  $   100.00
2     17-02-2026T12:19:52    TOKYO VACATION       $  2000.00


# Show expenses summary
expense-tracker summary
# Output
Total expenses: 2100.00

# Show monthly expenses summary
expense-tracker summary --month 2
Total expenses for February: $2100.00

# Update description field of an expense 
expense-tracker update --id 1 --description "Virginia GYM" 
# Output
Expense 1 updated successfully

# Update amount field of an expense
expense-tracker update --id 1 --amount 150
# Output
Expense 1 updated successfully

# Delete expense
expense-tracker delete 1
```

Project Reference
https://roadmap.sh/projects/expense-tracker