def most_frequent(nums):
    freq = {}

    # Count frequency
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Find max frequency element
    max_count = 0
    max_element = None

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            max_element = key

    return max_element


numbers = [1, 3, 2, 1, 4, 1, 3, 3, 3]
print(most_frequent(numbers))