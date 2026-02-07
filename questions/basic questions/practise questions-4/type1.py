# 1
num = int(input("Enter a number: "))

if 10 <= abs(num) <= 99:
    print("It is a two-digit number")
else:
    print("It is not a two-digit number")


# 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)


# 3
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("It is an uppercase alphabet")
else:
    print("It is not an uppercase alphabet")


# 4
num = int(input("Enter a number: "))

if (num % 4 == 0 or num % 6 == 0) and not (num % 4 == 0 and num % 6 == 0):
    print("Divisible by 4 or 6 but not both")
else:
    print("Condition not satisfied")
