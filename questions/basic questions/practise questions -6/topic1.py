#1
num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("It is a 3-digit number")
else:
    print("It is not a 3-digit number")


#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % 2 == 0 and b % 2 == 0:
    print("Both numbers are even")
else:
    print("Both numbers are not even")


#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


#4
ch = input("Enter a character: ")

ascii_val = ord(ch)

if ascii_val == 65 or ascii_val == 69 or ascii_val == 73 or ascii_val == 79 or ascii_val == 85 or \
   ascii_val == 97 or ascii_val == 101 or ascii_val == 105 or ascii_val == 111 or ascii_val == 117:
    print("It is a vowel")
else:
    print("It is not a vowel")


#5
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
