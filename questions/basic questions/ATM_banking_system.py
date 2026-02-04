'''
Simulate an ATM machine.
Create a class BankAccount
Use encapsulation (__balance)
Methods:deposit,withdraw,check balance,
Validate:
Withdrawal amount,Insufficient balance,Use a menu with loop,Log each transaction to a file.
'''
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.log_transaction(f"Deposited ₹{amount}")
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            self.log_transaction(f"Withdrawn ₹{amount}")
            print("Withdrawal successful.")

    def check_balance(self):
        print("Current Balance: ₹", self.__balance)
        self.log_transaction("Checked balance")

    def log_transaction(self, message):
        with open("atm_transactions.txt", "a") as file:
            file.write(f"{self.name}: {message} | Balance: ₹{self.__balance}\n")

account = BankAccount("User", 1000)

while True:
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = int(input("Enter deposit amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = int(input("Enter withdrawal amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Try again.")
