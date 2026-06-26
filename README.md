# Expense Tracker
a simple python program that track your expenses .
## usage:
```
python main.py add   -a <amount> -cat <category>  -nt <note>
python main.py list
python main.py summary
python main.py delete  -id <id>
python main.py modify -id <id> -cat <category> -nt <note>
```
## example
```
python main.py add -a 50 -cat food -nt lunch
python main.py list
python main.py summary 
python main.py delete -id 3 or python main.py delete -all
python main.py modify -id 2 -cat food -nt burger
```
## command
- **add** - add expense to the json file 
- **list** - list all the expense
- **summary** - give u a small summary about your expense status
- **delete** - delete an expense by its id or delete all the expense
- **modify** - modify the category name and the note
## Project Structure
```
ExpenseTracker/
├── main.py
├── tracker.py
└── README.md
```
