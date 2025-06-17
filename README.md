# Expense-Database-Creation-with-Python
A simple expense tracking application written in Python that demonstrates object-oriented programming by managing expenses using classes.
## Project Description

This project includes:
- An Expense class for creating expense records.
- An ExpenseDB class for managing a collection of expenses.
- Methods to add, remove, and retrieve expenses.
- A simple command-line interface (or usage example) to display stored expenses.

## How to Clone

To clone this repository, run:

bash
git clone https://github.com/Ainaganiu/Expense-Database-Creation-with-Python.git

## How to Run
Prerequisites:

Python 3.x installed on your system.
**Steps**:
- Navigate to the project directory: ```cd expense-database```
- Run the Python script: ```python expense_database.py```
```# Example usage
p1 = ExpenseDB()
p1.add_expense('Food', 100)
p1.add_expense('Transport', 50)
p1_dict = p1.to_dict()
for i,v in enumerate(p1_dict):
    print(i,v)
```

Thank you!!!!
