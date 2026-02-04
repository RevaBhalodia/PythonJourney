# question 1
def even_odd_sum(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum
print(even_odd_sum([1, 2, 3, 4, 5]))


# question 2
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
print(longest_word("accepting the day as it comes"))

# question 3
def is_harshad(n):
    sum_digits = 0
    temp = n

    while temp > 0:
        sum_digits += temp % 10
        temp //= 10

    return n % sum_digits == 0
print(is_harshad(20))

