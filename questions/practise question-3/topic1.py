# 1
n = int(input("Enter a number: "))

sum_digits = 0
product_digits = 1

while n > 0:
    digit = n % 10
    sum_digits += digit
    product_digits *= digit
    n //= 10

if sum_digits > product_digits:
    print("Sum of digits is greater than product of digits")
else:
    print("Product of digits is greater than or equal to sum of digits")


# 2
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s3 = input("Enter third string: ")

longest = s1

if len(s2) > len(longest):
    longest = s2
if len(s3) > len(longest):
    longest = s3

print("Longest string:", longest)


# 3
ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Special character")


# 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(max(a, b), min(a, b) - 1, -1):
    print(i, end=" ")
