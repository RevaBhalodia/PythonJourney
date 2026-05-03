def can_jump(nums):
    reach = 0

    for i in range(len(nums)):
        if i > reach:
            return False
        reach = max(reach, i + nums[i])

    return True
# Example
print(can_jump([2,3,1,1,4]))  # Output: True    
print(can_jump([3,2,1,0,4]))  # Output: False
