# question 1
for i in range(1, 101):
    if i % 10 == 7:
        print(i)

# question 2
num = input("Enter a number: ")

if num[0] != '0' and '0' in num:
    print("Duck number")
else:
    print("Not a Duck number")


# question 3
for i in range(1, 5):
    print(str(i) * i)
