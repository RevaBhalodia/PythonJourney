# 1
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(10))   
print(check_number(-5))    
print(check_number(0))     


# 2
def average_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
print(average_list([10, 20, 30, 40]))


# 3
def count_digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    return count
print(count_digits("abc1234xyz"))


# 4
def smaller(a, b):
    if a < b:
        return a
    else:
        return b
print(smaller(10, 5))



