# 1
def rotate_until_max(lst):
    max_val = max(lst)
    index = lst.index(max_val)
    return lst[index:] + lst[:index]


lst = [3, 4, 1, 9, 2]
print(rotate_until_max(lst))


# 2
def sum_zero_pairs(lst):
    pairs = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 0:
                pairs.append((lst[i], lst[j]))

    return pairs

lst = [2, -2, 3, -3, 4]
print(sum_zero_pairs(lst))


# 3
def rearrange_odd_even(lst):
    odd_pos = []
    even_pos = []

    for i in range(len(lst)):
        if (i + 1) % 2 != 0:
            odd_pos.append(lst[i])
        else:
            even_pos.append(lst[i])

    return odd_pos + even_pos


lst = [10, 20, 30, 40, 50, 60]
print(rearrange_odd_even(lst))


# 4
def group_by_length(words):
    result = {}

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)

    return result

words = ["hi", "hello", "cat", "python", "dog"]
print(group_by_length(words))
