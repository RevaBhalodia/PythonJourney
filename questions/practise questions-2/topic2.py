# 1
n = int(input("Enter n: "))

product = 1

for i in range(1, n + 1):
    product = product * i
    
    for j in range(1, i + 1):
        if j < i:
            print(j, end="×")
        else:
            print(j, end="")
    print()


# 2
count = 0

for num in range(1, 1001):
    if num % 7 == 0 and num % 5 != 0:
        count += 1

print("Count:", count)


# 3
s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string:", rev)


# 4
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print((i + j) % 2, end="")
    print()
