# 1
def median(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
print(median([3, 1, 4, 2, 5]))   

# 2
def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(hcf(12, 18))  

# 3
def is_kaprekar(num):
    square = num * num
    s = str(square)
    length = len(s)

    left = int(s[:length // 2]) if s[:length // 2] != "" else 0
    right = int(s[length // 2:])

    return left + right == num
print(is_kaprekar(45))  


# 4
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq
print(word_frequency("This is a test This is"))




