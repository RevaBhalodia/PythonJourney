#question 1
for i in range(1, 6):
    print("*" * i)



#question 2
num = int(input("Enter a number: "))

if num <= 1:
    print("not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime number")
    else:
        print("not a prime number")
