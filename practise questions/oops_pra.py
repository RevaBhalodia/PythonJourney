#Create a class Mobile with: brand price Add a method to apply discount on the price.
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount_percent):
        discount = self.price * (discount_percent / 100)
        self.price -= discount

m1 = Mobile("apple:", 100000)
m1.apply_discount(18)


print("brand:", m1.brand)
print("price after discount:", m1.price)

#Create a class Account with: account number balance Add methods to deposit and withdraw (with validation).

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
        else:
            print("Insufficient balance or invalid amount")


acc = Account(101, 5000)

acc.deposit(2000)
acc.withdraw(3000)

print("Account Number:", acc.account_number)
print("Balance:", acc.balance)


    
