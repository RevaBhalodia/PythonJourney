#1
for num in range(1, 301):
    temp = str(num)
    for ch in temp:
        if ch in "02468":
            print(num)
            break


#2
num = input("Enter a number: ")

largest = '0'

for ch in num:
    if ch > largest:
        largest = ch

print("Largest digit is:", largest)


#3
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end="")
    print()


#4
n = int(input("Enter a number: "))

total = 0

for i in range(1, n+1):
    if i % 4 == 0:
        total += i

print("Sum is:", total)
