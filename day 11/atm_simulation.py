balance = float(input("enter your balance:"))
withdraw = float(input("enter your withdrawl amount:"))

if withdraw % 100 != 0:
    print("withdrawl amount should be a multiple of 100")    

elif withdraw > balance:
    print("insufficient balance")

else:
    balance = balance - withdraw
    print("withdrawl successful")
    print(" remaining balance:", balance)
