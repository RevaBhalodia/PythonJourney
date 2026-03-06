def sum_divisible(lst):
    total = 0

    for i in lst:
        if i % 3 == 0 and i % 5 == 0:
            total = total + i

    return total


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Sum:", sum_divisible(numbers))