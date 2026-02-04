# 1
for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# 2
num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# 3
for i in range(5, 0, -1):
    print("*" * i)

