# 1
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
acc = BankAccount("Riya", 5000)
acc.deposit(2000)
acc.withdraw(1000)
acc.display_balance()


# 2
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_grade(self):
        avg = (self.m1 + self.m2 + self.m3) / 3

        if avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"
s = Student(80, 70, 75)
print("Grade:", s.get_grade())


