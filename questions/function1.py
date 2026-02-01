# question 1
def difference_max_min(numbers):
    return max(numbers) - min(numbers)
print(difference_max_min([10, 3, 25, 7]))


# question 2
def count_unique_words(sentence):
    words = sentence.split()
    return len(set(words))
print(count_unique_words("hell is filled with people like you."))


# question 3
def is_strong_number(num):
    import math
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)
        temp //= 10

    return total == num
print(is_strong_number(145))   
print(is_strong_number(123))   
