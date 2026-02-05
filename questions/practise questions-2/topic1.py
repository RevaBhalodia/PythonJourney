# 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

maximum = max(a, b, c)
minimum = min(a, b, c)

middle = a + b + c - maximum - minimum

print("Middle value is:", middle)


# 2
num = input("Enter a number: ")

inc = True
dec = True

for i in range(len(num) - 1):
    if num[i] >= num[i + 1]:
        inc = False
    if num[i] <= num[i + 1]:
        dec = False

if inc:
    print("Increasing")
elif dec:
    print("Decreasing")
else:
    print("Mixed")


# 3
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 4
s = input("Enter a string: ")

is_alpha = True

for ch in s:
    if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
        is_alpha = False
        break

if is_alpha:
    print("String contains only alphabets")
else:
    print("String contains digits or symbols")
