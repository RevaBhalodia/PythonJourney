def rob(nums):
    prev, curr = 0, 0

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr
# Example
print(rob([1,2,3,1]))  # Output: 4
print(rob([2,7,9,3,1]))  # Output: 12
