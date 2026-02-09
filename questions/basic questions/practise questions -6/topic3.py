#1
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print(sum_of_digits(123))


#2
def count_odd(numbers):
    count = 0
    for n in numbers:
        if n % 2 != 0:
            count += 1
    return count

print(count_odd([1, 2, 3, 4, 5, 6]))


#3
def count_uppercase(text):
    count = 0
    for ch in text:
        if 'A' <= ch <= 'Z':
            count += 1
    return count

print(count_uppercase("Hello WORld"))


#4
def absolute_difference(a, b):
    if a > b:
        print(a - b)
    else:
        print(b - a)

absolute_difference(10, 4)
