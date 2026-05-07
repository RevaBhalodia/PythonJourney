def can_partition(nums):
    total = sum(nums)

    if total % 2:
        return False

    target = total // 2
    dp = {0}

    for num in nums:
        new_dp = dp.copy()
        for t in dp:
            if t + num == target:
                return True
            new_dp.add(t + num)
        dp = new_dp

    return target in dp
# Example usage:
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# For example, given the array [1, 5, 11, 5], return true, as the array can be partitioned as [1, 5, 5] and [11].
# Given the array [1, 2, 3, 5], return false, as the array cannot be partitioned into equal sum subsets.    