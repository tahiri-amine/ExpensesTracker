#i have to create 4 function
from datetime import datetime
import json
#build a class called Expenstracker 
class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load()  # load JSON into memory once
    #because self.load() return a list
    def load(self):
        # read data.json and return the list
        try:
            with open("data.json","r",encoding="utf-8") as f:
                return json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            return []
    
    def save(self): 
        # write self.expenses to data.json
        with open("data.json","w",encoding="utf-8") as f:
            json.dump(self.expenses,f,indent=4)
    
    def add(self, amount, category, note):
        # create a dict, append to self.expenses, call save
        
        dictionary = {}
        dictionary["id"] = len(self.expenses)+1
        dictionary["amount"] = amount
        dictionary["category"] = category
        dictionary["note"] = note
        dictionary["day"] = datetime.today().strftime( "%Y-%m-%d")
        self.expenses.append(dictionary)
        self.save()
    def list(self):
        if not self.expenses:
            print("you have no expenses yet ( ✜︵✜ )")
        else:
            print("your expenses are :")
            for expens in self.expenses:
                print(expens)
    def summary(self):
        if not self.expenses:
            print("you have no expenses yet ( ✜︵✜ )")
            return
        dictionary ={}
        totale = 0
        for expens in self.expenses:
            totale += expens["amount"]
            cat = expens["category"]
            if cat in dictionary:
                dictionary[cat] += expens["amount"]
            else:
                dictionary[cat] = expens["amount"]
        print("Totale spent:",totale)
        for element in dictionary:
            print(element,dictionary[element],"DH")
    def delete(self,id):
        if not self.expenses:
            print("you have no expenss yet try to add some expenss :)")
            return 
        
        before = len(self.expenses)
        self.expenses = [dic for dic in self.expenses if  dic["id"] != id]
        for index, expens in enumerate(self.expenses):
            expens["id"] = index + 1
        self.save()
        if len(self.expenses) == before:
            print("no expense found with this id")
    def modify_category(self,id,new_category):
        if not self.expenses:
            print("your already have no expenss to modifie ( ✜︵✜ ) ")
        else:
            is_id = False
            for expense in self.expenses:
                if expense["id"] == id:
                        expense["category"] = new_category
                        is_id = True
            if not is_id:
                print("the giving id is not found")
            else:
                self.save()
        


        
        
       
     
