#Write a function that takes a list of numbers and returns:maximum number,minimum number.
def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num



#Write a function that checks whether a given string is a palindrome or not.
def is_palindrome(s):
    s = s.lower()   
    return s == s[::-1]
