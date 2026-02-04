# 1
num = int(input("Enter a number: "))
temp = num
digits = list(map(int, str(num)))

total = 0
for i in range(len(digits)):
    total += digits[i] ** (i + 1)

if total == num:
    print("Disarium Number")
else:
    print("Not a Disarium Number")


# 2
for num in range(1, 301):
    temp = num
    product = 1

    while temp > 0:
        digit = temp % 10
        product *= digit
        temp //= 10

    if product % 3 == 0:
        print(num)


# 3
num = int(input("Enter a number: "))
largest_even = -1

while num > 0:
    digit = num % 10
    if digit % 2 == 0 and digit > largest_even:
        largest_even = digit
    num //= 10

if largest_even == -1:
    print("No even digit found")
else:
    print("Largest even digit:", largest_even)


# 4
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# 5
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels and s.count(ch) > 1:
        continue
    result += ch

print("Result:", result)
