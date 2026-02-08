# 1
for i in range(1, 301):
    if '3' in str(i):
        print(i, end=" ")


# 2
n = input("Enter a number: ")

first_digit = int(n[0])
last_digit = int(n[-1])

print("Sum =", first_digit + last_digit)


# 2
for i in range(1, 5):
    print("*" * i)


# 4
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)
