# question 1
n = int(input("Enter a number: "))
sum_sq = 0

for i in range(1, n + 1):
    sum_sq += i * i

print("Sum of squares:", sum_sq)


# question 2
n = int(input("Enter a number: "))
sum_div = 0

for i in range(1, n):
    if n % i == 0:
        sum_div += i

if sum_div == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# question 3
s = input("Enter a string: ")

visited = ""

for char in s:
    if char not in visited:
        count = 0
        for c in s:
            if c == char:
                count += 1
        print(char, ":", count)
        visited += char
