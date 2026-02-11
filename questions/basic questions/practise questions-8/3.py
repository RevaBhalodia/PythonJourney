#1
def sum_of_squares(lst):
    total = 0
    for num in lst:
        total += num * num
    return total
print(sum_of_squares([1, 2, 3, 4]))


#2
def first_non_repeating(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None
print(first_non_repeating("aabbcdde"))


#3
def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse
print(reverse_number(1234))


#4
def unique_elements(list1, list2):
    result = []
    
    for item in list1:
        if item not in list2:
            result.append(item)
    
    for item in list2:
        if item not in list1:
            result.append(item)
    
    return result
print(unique_elements([1, 2, 3], [2, 3, 4]))
