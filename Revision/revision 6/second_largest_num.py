def second_largest(nums):
    unique_nums = list(set(nums))  
    
    if len(unique_nums) < 2:
        return "No second largest element"
    
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([10, 20, 20, 30, 40]))
