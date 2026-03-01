# Function to check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def sum_prime_factors(n):
    i = 2
    total = 0

    while i <= n:
        while n % i == 0:
            total += sum_of_digits(i)
            n = n // i
        i += 1

    return total

num = int(input("Enter a number: "))

if is_prime(num):
    print("Not a Smith Number (because it is prime)")
else:
    sum_digits = sum_of_digits(num)
    sum_factors = sum_prime_factors(num)

    if sum_digits == sum_factors:
        print("It is a Smith Number")
    else:
        print("It is NOT a Smith Number")