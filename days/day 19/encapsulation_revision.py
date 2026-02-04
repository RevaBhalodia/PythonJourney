#Create a class BankAccount with:private attribute __balance,methods to deposit and display balance
#Try accessing __balance directly and observe the result.
#Write why this happens (comment).

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("balance:", self.__balance)

acc = BankAccount(10000)

acc.deposit(2000)
acc.show_balance()

#print(acc.__balance) __balance is private and python changes __balance to bankaccount__balance internally,
#so it cannot be accessed directly outside the class.