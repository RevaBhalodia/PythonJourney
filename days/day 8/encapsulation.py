#encapsulation = wrapping data and functions into a single unit(object).
# question 
# create account class with 2 attributes - balance and account no.
#create methods for debit,credit and printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("RS", amount, "was debited")
        print("total balance=", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("RS", amount, "was credited")
        print("total balance=", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 1234599)
acc1.debit(1000)
acc1.credit(599)

