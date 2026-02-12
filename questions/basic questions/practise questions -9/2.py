def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


def numbers_with_prime_digit_sum(lst):
    result = []
    for num in lst:
        if is_prime(sum_of_digits(num)):
            result.append(num)
    return result



numbers = [23, 14, 56]
print(numbers_with_prime_digit_sum(numbers))
