#question 1
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current balance:", self.__balance)
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.show_balance()


#question 2
class Shape:
    def area(self):
        print("Area method of Shape")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
rect = Rectangle(5, 4)
print("Area of Rectangle:", rect.area())

circle = Circle(3)
print("Area of Circle:", circle.area())
