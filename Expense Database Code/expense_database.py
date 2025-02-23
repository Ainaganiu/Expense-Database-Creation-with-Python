#Expenses Database using a list of Expense objects
import uuid
from datetime import datetime

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.date = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "date": self.date.strftime('%Y-%m-%d %H:%M:%S')
        }

class ExpenseDB:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, title, amount):
        expense = Expense(title, amount)
        self.expenses.append(expense)
        
    def remove_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                self.expenses.remove(expense)
                break
                
    def get_expense_by_id(self, id):
        for expense in self.expenses:
            if expense.id == id:
                return expense
        return None
    
    def get_expense_by_title(self, title):
        result = []
        for expense in self.expenses:
            if expense.title == title:
                result.append(expense)
        return result
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
    
# Example usage
p1 = ExpenseDB()
p1.add_expense('Food', 100)
p1.add_expense('Transport', 50)
p1_dict = p1.to_dict()
for i,v in enumerate(p1_dict):
    print(i,v)
