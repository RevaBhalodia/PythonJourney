expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))

def total_expense():
    total = sum(x[1] for x in expenses)
    print("Total spent:", total)

def show_expenses():
    for e in expenses:
        print(e[0], ":", e[1])

while True:
    print("\n1.Add 2.Show 3.Total 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_expense()
    elif ch == "2":
        show_expenses()
    elif ch == "3":
        total_expense()
    else:
        break