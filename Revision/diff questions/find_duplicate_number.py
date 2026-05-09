def find_duplicate(nums):
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow2 = nums[0]

    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow
# Example usage:
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive, there is only one repeated number in nums, return this repeated number.
# For example, given the array [1,3,4,2,2], the output is 2. Given the array [3,1,3,4,2], the output is 3. Given the array [1,1], the output is 1. Given the array [1,1,2], the output is 1.    