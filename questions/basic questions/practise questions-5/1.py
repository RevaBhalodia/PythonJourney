# 1
n = int(input("Enter a number: "))

if n % 3 == 0 or n % 7 == 0:
    print("The number is a multiple of 3 or 7")
else:
    print("The number is not a multiple of 3 or 7")


# 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
smallest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print("Difference =", largest - smallest)


# 3
ch = input("Enter a character: ")

ascii_value = ord(ch)

if ascii_value >= 48 and ascii_value <= 57:
    print("It is a digit")
else:
    print("It is not a digit")


# 4
n = int(input("Enter a number: "))

if n >= 50 and n <= 100:
    print("The number lies between 50 and 100")
else:
    print("The number does not lie between 50 and 100")
