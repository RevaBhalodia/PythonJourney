def second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second


numbers = [10, 45, 32, 89, 67]

print("Second largest:", second_largest(numbers))