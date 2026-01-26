# loops revision questions
#1
for i in range(1, 51):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

# 2
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

# 3
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

