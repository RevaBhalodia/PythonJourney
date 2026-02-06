# 1
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print("Number of factors:", count)


# 2
for num in range(1, 501):
    last_digit = num % 10
    first_digit = num

    while first_digit >= 10:
        first_digit //= 10

    if first_digit == last_digit:
        print(num, end=" ")


# 3
n = int(input("Enter a number: "))

temp = n
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

divisor = 10 ** (digits - 1)

while divisor > 0:
    digit = n // divisor
    print(digit)
    n = n % divisor
    divisor //= 10


# 4
for i in range(1, 5):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
