#A shop gives a discount of 10% if total bill is more than ₹1000.
#Take prices of 5 items and calculate the final bill using a loop.

total = 0

for i in range(1, 6):
    price = float(input(f"Enter price of item {i}: "))
    total += price

if total > 1000:
    discount = total * 0.10
    final_bill = total - discount
else:
    final_bill = total

print("Total Bill:", total)
print("Final Bill after discount:", final_bill)


#Take a number and print whether it is:a single-digit,double-digit,or more than two digits.
num = int(input("Enter a number: "))

if -9 <= num <= 9:
    print("Single-digit number")
elif -99 <= num <= 99:
    print("Double-digit number")
else:
    print("More than two digits")
