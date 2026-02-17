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
expense-tracker add --description GYM --amount 70
# Output

# Delete expense
expense-tracker delete 1
# Output

# List expenses from memory
expense-tracker list
# Output 

# Update an expense
expense tracker update --id 1 --description "Virginia GYM" --amount 100
# Output

```

Project Reference
https://roadmap.sh/projects/expense-tracker