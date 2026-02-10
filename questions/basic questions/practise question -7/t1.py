#1
num = int(input("Enter a number: "))

if num % 6 == 0 and num % 9 == 0:
    print("Divisible by both 6 and 9")
else:
    print("Not divisible by both 6 and 9")


#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a > c and a < b):
    print(a, "is the middle number")
elif (b > a and b < c) or (b > c and b < a):
    print(b, "is the middle number")
else:
    print(c, "is the middle number")


#3
ch = input("Enter a character: ")

ascii_value = ord(ch)

if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
    print("It is an alphabet")
else:
    print("It is not an alphabet")


#4
import math

num = int(input("Enter a number: "))

root = int(math.sqrt(num))

if root * root == num:
    print("Perfect square")
else:
    print("Not a perfect square")


#5
num = int(input("Enter a number: "))

if num % 10 == 0 or num % 10 == 5:
    print("Ends with 0 or 5")
else:
    print("Does not end with 0 or 5")
