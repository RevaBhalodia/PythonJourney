def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix = {0:1}

    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix:
            count += prefix[curr_sum - k]

        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

    return count

# Example
print(subarray_sum([1,1,1], 2))  # Output: 2