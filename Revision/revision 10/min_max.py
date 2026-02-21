def max_min_difference(nums):
    if len(nums) == 0:
        return None   # or raise error

    maximum = nums[0]
    minimum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum - minimum


# Example
print(max_min_difference([4, 2, 9, 1, 5]))  # 8