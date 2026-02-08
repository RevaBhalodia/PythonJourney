# 1
def count_div_by_5(lst):
    count = 0
    for num in lst:
        if num % 5 == 0:
            count += 1
    return count

print(count_div_by_5([10, 23, 45, 12, 5]))


# 2
def count_spaces(s):
    count = 0
    for ch in s:
        if ch == ' ':
            count += 1
    return count

print(count_spaces("Python is very easy"))


# 3
def sum_prime_digits(n):
    prime_sum = 0
    for digit in str(n):
        if digit in '2357':
            prime_sum += int(digit)
    return prime_sum

print(sum_prime_digits(273451))


# 4
def shorter_string(s1, s2):
    if len(s1) < len(s2):
        return s1
    else:
        return s2

print(shorter_string("Python", "Java"))
