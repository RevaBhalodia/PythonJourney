# question 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(numbers):
    return [num for num in numbers if is_prime(num)]
print(prime_list([1, 2, 3, 4, 5, 6, 7, 10, 11]))


# question 2
def split_list(lst):
    mid = (len(lst) + 1) // 2
    return lst[:mid], lst[mid:]
print(split_list([1, 2, 3, 4, 5]))


# question 3
def replace_negatives(lst):
    return [0 if num < 0 else num for num in lst]
print(replace_negatives([3, -1, 5, -7, 9]))
