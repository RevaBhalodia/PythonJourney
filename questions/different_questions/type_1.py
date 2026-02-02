# 1
def count_primes(numbers):
    count = 0

    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1

    return count
nums = [2, 3, 4, 5, 6, 7, 9]
print(count_primes(nums))


# 2
def char_frequency(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq
text = "hello"
print(char_frequency(text))


# 3
def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse
print(reverse_number(12345))
