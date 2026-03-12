balance = 5000

while True:

    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Money deposited successfully")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")

    elif choice == 4:
        print("Thank you for using the bank system")
        break

    else:
        print("Invalid choice")