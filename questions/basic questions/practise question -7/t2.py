#1
for num in range(1, 401):
    s = 0
    temp = num
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s % 2 != 0:
        print(num)


#2
num = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    num //= 10

print("Difference:", even_sum - odd_sum)


#3
for i in range(1, 5):
    print(str(i) * i)


#4
n = int(input("Enter a number: "))

for i in range(7, n + 1, 7):
    print(i)


#5
s = input("Enter a string: ")

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if s.index(s[i]) == i:
        print(s[i], ":", count)
