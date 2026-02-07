# 1
for i in range(1, 201):
    if i % 10 == 5:
        print(i)


# 2
num = int(input("Enter a number: "))
sum_odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        sum_odd += digit
    num //= 10

print("Sum of odd digits:", sum_odd)


# 3
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 4
n = int(input("Enter a number: "))

for i in range(n):
    print("*", end="")
