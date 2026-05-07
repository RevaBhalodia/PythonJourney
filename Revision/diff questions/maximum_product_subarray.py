def max_product(nums):
    res = max(nums)
    curr_max = curr_min = 1

    for n in nums:
        temp = curr_max * n

        curr_max = max(n, temp, curr_min * n)
        curr_min = min(n, temp, curr_min * n)

        res = max(res, curr_max)

    return res
# Example usage:
# Given an integer array, find the contiguous subarray within an array (containing at least one number) which has the largest product.
# For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
# Given the array [-2,0,-1], the result is 0, because the result cannot be 2, since [-2,-1] is not a contiguous subarray.   
