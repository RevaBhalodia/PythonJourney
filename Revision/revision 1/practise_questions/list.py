# question 1
def modify_list(nums):
    new_list = []

    for i in range(len(nums)):
        if i % 2 == 0:
            new_list.append(nums[i] * 2)
        else:
            new_list.append(nums[i])

    return new_list
print(modify_list([1, 2, 3, 4, 5]))


# question 2
def merge_alternatively(list1, list2):
    merged = []

    for i in range(len(list1)):
        merged.append(list1[i])
        merged.append(list2[i])

    return merged
print(merge_alternatively([1, 2, 3], [10, 20, 30]))


# question 3
def longest_increasing_sublist(nums):
    longest = []
    current = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [nums[i]]

    if len(current) > len(longest):
        longest = current

    return longest
print(longest_increasing_sublist([1, 2, 3, 1, 2]))
