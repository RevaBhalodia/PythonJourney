def second_largest(nums):
    unique_nums = set(nums)
    
    if len(unique_nums) < 2:
        return None
    
    largest = second = float('-inf')
    
    for num in unique_nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    
    return second


print(second_largest([10, 20, 20, 30, 40]))
