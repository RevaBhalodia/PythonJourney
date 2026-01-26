# function revision
# 1
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(10)) 
print(check_even_odd(7))  

# 2
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_list([1, 2, 3, 4, 5]))  

# 3
def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("madam"))  
print(is_palindrome("hello"))

