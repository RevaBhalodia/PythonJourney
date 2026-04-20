class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.message = f"Cannot withdraw ₹{amount}. Balance: ₹{balance}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return self.balance

acc = BankAccount(1000)
try:
    acc.withdraw(1500)
except InsufficientFundsError as e:
    print(f"Error: {e}")
finally:
    print(f"Current balance: ₹{acc.balance}")