# 1
def even_odd_difference(lst):
    even_sum = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum - odd_sum
print(even_odd_difference([1, 2, 3, 4, 5]))


# 2
def has_uppercase_and_digit(s):
    has_upper = False
    has_digit = False

    for ch in s:
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True

    return has_upper and has_digit
print(has_uppercase_and_digit("Hello1"))


# 3
def count_trailing_zeros(n):
    count = 0

    while n > 0 and n % 10 == 0:
        count += 1
        n //= 10

    return count
print(count_trailing_zeros(12000))
