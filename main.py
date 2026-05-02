import sys
from tracker import ExpenseTracker  
data = sys.argv
#py main.py add --amount 50 --category food --note "lunch"
usage = """
py main.py add --amount 50 --category food --note "lunch"
py main.py list
py main.py summary
py main.py delete --id 3
"""
e = ExpenseTracker()
if data[1] =="add":
    if len(data) < 4:#because i have 3 argument + the path that sys return
        print("NotEnoughtArgumentError:the mode add expect 3 argument ")
        print(usage)
        sys.exit()
    try:
        e.add(float(data[2]),data[3],data[4])
    except ValueError as e:
        print(e)
        print("--amount must be int or float!")
elif data[1] == "list":
    e.list()
elif data[1] == "summary":
    e.summary()
elif data[1] == "delete":
    if len(data) < 3:# one for the path that already in sys list and one for the id
        print("NotEnoughtArgumentError:the mode add expect 1 argument (id)")
        sys.exit()
    try:
        e.delete(int(data[2]))
    except ValueError:
        print("id must be a number")
else:
    print("ModeError:the",data[1],"isn't a mode the modes are:")
    print("add\ndummary\nlist\ndelete")
    sys.exit()

