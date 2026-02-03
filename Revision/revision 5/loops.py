# 1
num = int(input("Enter a number: "))
smallest = 9

while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10

print("Smallest digit:", smallest)


# 2
for num in range(100, 501):
    temp = num
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp = temp // 10

    if digit_sum % 2 == 0:
        print(num)


# 3
num = int(input("Enter a number: "))
square = num * num
digit_sum = 0

while square > 0:
    digit_sum += square % 10
    square = square // 10

if digit_sum == num:
    print("Neon Number")
else:
    print("Not a Neon Number")


# 4
s = input("Enter a string: ")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(len(s)):
    if is_prime(i):
        print(s[i], end="")


# 5
for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
