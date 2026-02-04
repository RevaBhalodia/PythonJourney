# 1
def greater_number(a, b):
    if a > b:
        return a
    else:
        return b

print(greater_number(10, 20))


# 2
def count_words(text):
    words = text.split()
    return len(words)

print(count_words("Python is easy to learn"))


# 3
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))
