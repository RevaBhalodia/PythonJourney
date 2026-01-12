num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))

operator = input("enter operation( +, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")
