#1
def second_smallest(lst):
    lst = list(set(lst))   
    lst.sort()
    return lst[1]

numbers = [4, 2, 7, 2, 9]
print(second_smallest(numbers))


#2
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))


#3
def count_digits(num):
    count = 0
    if num == 0:
        return 1
    while num > 0:
        count += 1
        num //= 10
    return count

print(count_digits(12345))


#4
def common_elements(list1, list2):
    common = []
    for i in list1:
        if i in list2 and i not in common:
            common.append(i)
    return common

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6]
print(common_elements(a, b))


