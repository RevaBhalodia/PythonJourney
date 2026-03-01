def first_missing_positive(nums):
    positive_numbers = set()

    for num in nums:
        if num > 0:
            positive_numbers.add(num)

    
    i = 1
    while True:
        if i not in positive_numbers:
            return i
        i += 1


nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = first_missing_positive(nums)
print("First missing positive number:", result)