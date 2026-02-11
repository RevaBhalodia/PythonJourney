#1
num = int(input("Enter a number: "))

if num % 8 == 0 and num % 12 != 0:
    print("It is a multiple of 8 but not 12.")
else:
    print("Condition not satisfied.")


#2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if abs(num1) < abs(num2):
    print(num1, "is closer to zero.")
elif abs(num2) < abs(num1):
    print(num2, "is closer to zero.")
else:
    print("Both numbers are equally close to zero.")


#3
s = input("Enter a string: ")

only_digits = True

for ch in s:
    if ch < '0' or ch > '9':
        only_digits = False
        break

if only_digits and s != "":
    print("String contains only digits.")
else:
    print("String does not contain only digits.")


#4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All equal")
else:
    print("Not equal")
