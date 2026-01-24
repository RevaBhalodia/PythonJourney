#Write a program to print all numbers between 1 and 100 that are:divisible by 3,but not divisible by 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)


#Take a number n as input and use a loop to:count how many digits it has
n = int(input("Enter a number: "))
count = 0

while n != 0:
    n = n // 10
    count += 1

print("Number of digits:", count)
