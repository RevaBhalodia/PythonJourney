def longest_increasing_sequence(nums):
    if not nums:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            current_length = 1

        max_length = max(max_length, current_length)

    return max_length


# Main Program
nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = longest_increasing_sequence(nums)

print("Longest consecutive increasing sequence length:", result)