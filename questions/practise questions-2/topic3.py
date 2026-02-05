# 1
def find_smallest_largest(lst):
    smallest = lst[0]
    largest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest
numbers = [4, 7, 1, 9, 3]
print(find_smallest_largest(numbers))


# 2
def sum_even_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            total += digit
        num = num // 10

    return total
print(sum_even_digits(123456))  

# 3
def is_valid_identifier(s):
    if not (s[0].isalpha() or s[0] == '_'):
        return False

    for ch in s:
        if not (ch.isalnum() or ch == '_'):
            return False

    return True
print(is_valid_identifier("var_1"))  
print(is_valid_identifier("1var"))    


# 4
def unique_elements(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)

    for item in list2:
        if item not in list1:
            result.append(item)

    return result
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(unique_elements(a, b)) 

