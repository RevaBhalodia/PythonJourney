'''
Develop a secure bank account model.
Requirements:
Create a class BankAccount
Declare a private variable __balance
Provide methods to deposit and view balance
Goal:
Apply encapsulation to protect sensitive data.
'''
class BankAccount:
    def __init__(self):
        self.__balance = 0  

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount()
acc.deposit(5000)
acc.show_balance()