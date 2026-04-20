def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Only loads one value at a time
for num in fibonacci(100):
    print(num, end=" ")

# As a list
fib_list = list(fibonacci(50))
print(fib_list)