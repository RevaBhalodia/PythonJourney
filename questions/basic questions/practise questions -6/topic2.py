#1
for num in range(1, 101):
    temp = num
    sum_digits = 0

    while temp > 0:
        sum_digits += temp % 10
        temp //= 10

    if sum_digits > 10:
        print(num)


#2
num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print("Product of digits:", product)


#3
for i in range(1, 6):
    print("*" * i)


#4
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 4 == 0:
        continue
    print(i)


#5
num = int(input("Enter a number: "))

while num > 0:
    print(num % 10, end="")
    num //= 10
