def expense_splitter():

    expenses = {
        "Amit": 2000,
        "Riya": 1000,
        "Raj": 3000
    }

    print("Expenses:", expenses)

    total = sum(expenses.values())
    n = len(expenses)
    equal_share = total / n

    print("\nTotal Expense:", total)
    print("Each person should pay:", equal_share)

    balance = {}
    for name, amount in expenses.items():
        balance[name] = amount - equal_share

    print("\nSettlement:")

    owes = {k: v for k, v in balance.items() if v < 0}
    gets = {k: v for k, v in balance.items() if v > 0}

    for payer in owes:
        for receiver in gets:
            if abs(owes[payer]) > 0 and gets[receiver] > 0:
                pay_amount = min(abs(owes[payer]), gets[receiver])
                print(f"{payer} should pay {receiver} ₹{pay_amount:.2f}")
                owes[payer] += pay_amount
                gets[receiver] -= pay_amount

expense_splitter()
