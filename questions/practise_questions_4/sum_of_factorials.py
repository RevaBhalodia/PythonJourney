import math

def sum_of_digit_factorials(n):
    total = 0
    
    while n > 0:
        digit = n % 10
        total += math.factorial(digit)
        n //= 10

    return total


print(sum_of_digit_factorials(145))