def group_by_digits(nums):
    result = {}
    
    for num in nums:
        digit_count = len(str(abs(num)))    
        
        if digit_count in result:
            result[digit_count].append(num)
        else:
            result[digit_count] = [num]
    
    return result


print(group_by_digits([5, 23, 456, 78, 1]))