def is_strictly_increasing(nums):
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True


# Example
print(is_strictly_increasing([1, 2, 3, 4]))   # True
print(is_strictly_increasing([1, 3, 2, 4]))   # False