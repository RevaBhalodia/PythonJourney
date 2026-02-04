age = int(input("enter your age:"))
price = 250

if age < 12:
    final_price = price * 0.5
   
elif age >= 60:
    final_price = price * 0.7
    
else:
    final_price = price

print("Ticket Price: ₹", final_price)
    



