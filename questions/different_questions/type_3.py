# 1
def remove_duplicates(lst):
    result = []

    for i in lst:
        if lst.count(i) == 1:
            result.append(i)

    return result
nums = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(nums))


# 2
def adjacent_difference(lst):
    diff = []

    for i in range(len(lst) - 1):
        diff.append(lst[i + 1] - lst[i])

    return diff
print(adjacent_difference([10, 15, 20]))


# 3
def kth_largest(lst, k):
    temp = lst.copy()

    for i in range(k - 1):
        max_val = max(temp)
        temp.remove(max_val)

    return max(temp)
nums = [12, 3, 5, 7, 19]
k = 2
print(kth_largest(nums, k))
