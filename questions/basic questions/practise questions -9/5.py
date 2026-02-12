class Transaction:
    def __init__(self, amount, t_type):
        if t_type not in ["credit", "debit"]:
            raise ValueError("Type must be 'credit' or 'debit'")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.amount = amount
        self.type = t_type


class Account:
    def __init__(self):
        self.transactions = []

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t.type == "credit":
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    def add_transaction(self, transaction):
        if transaction.type == "debit":
            if self.get_balance() - transaction.amount < 0:
                print("Transaction declined! Insufficient balance.")
                return
        
        self.transactions.append(transaction)
        print(" Transaction successful!")
