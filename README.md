# Expense Tracker
a simple python program that track your expenses .
## usage:
py main.py add   amount  category  note
py main.py list
py main.py summary
py main.py delete  id
## example
py main.py add 50 food lunch
py main.py list
py main.py summary 
py main.py delete 3
## command
- **add** - add expense to the json file 
- **list** - list all the expense
- **summary** - give u a small summary about your expense status
- **delete** - delete an expense by its id
## Project Structure
ExpenseTracker/
├── main.py
├── tracker.py
└── README.md