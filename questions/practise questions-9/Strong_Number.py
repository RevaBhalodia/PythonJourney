num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum_fact = sum_fact + fact
    temp = temp // 10

if sum_fact == num:
    print("Strong Number")
else:
    print("Not a Strong Number")