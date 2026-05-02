#i have to create 4 function
from datetime import datetime
import json
#build a class called Expenstracker 
class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load()  # load JSON into memory once
    
    def load(self):
        # read data.json and return the list
        with open("data.json","r") as f:
            return json.load(f)
    
    def save(self):
        # write self.expenses to data.json
        with open("data.json","w") as f:
            json.dump(self.expenses,f)
    
    def add(self, amount, category, note):
        # create a dict, append to self.expenses, call save
        
        dictionary = {}
        dictionary["id"] = len(self.expenses)+1
        dictionary["amount"] = amount
        dictionary["category"] = category
        dictionary["note"] = note
        dictionary ["day"] = datetime.today().strftime( "%Y-%m-%d")
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
    
        #do i have to add an esle in here? because if the list is empty the pg create a dic and the varibale totale 
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
            return True
        
        before = len(self.expenses)
        self.expenses = [dic for dic in self.expenses if  dic["id"] != id]
        for index, expens in enumerate(self.expenses):
            expens["id"] = index + 1
        self.save()
        if len(self.expenses) == before:
            print("no expense found with this id")
        
        
       
     