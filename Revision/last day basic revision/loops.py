# question 1
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j < i:
            print(j, end="+")
        else:
            print(j, end="")
    print()


# question 2
num = int(input("Enter a number: "))

sum_digits = 0
product_digits = 1

temp = num
while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product_digits *= digit
    temp //= 10

if sum_digits == product_digits:
    print("Spy Number")
else:
    print("Not a Spy Number")


# question 3
s = input("Enter a string: ")

printed = ""

for char in s:
    if s.count(char) > 1 and char not in printed:
        print(char, end=" ")
        printed += char
