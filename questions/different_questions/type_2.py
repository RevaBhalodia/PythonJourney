# 1
n = int(input("Enter how many Fibonacci numbers to print: "))

a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 2
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a Palindrome number")


# 3
print("Numbers divisible by both 4 and 6:")

for i in range(1, 201):
    if i % 4 == 0 and i % 6 == 0:
        print(i, end=" ")
