# question 1
def split_into_chunks(lst):
    chunks = []
    for i in range(0, len(lst), 3):
        chunks.append(lst[i:i+3])
    return chunks
print(split_into_chunks([1, 2, 3, 4, 5, 6, 7]))


# question 2
def move_zeros(lst):
    result = []
    zero_count = 0

    for i in lst:
        if i != 0:
            result.append(i)
        else:
            zero_count += 1

    result.extend([0] * zero_count)
    return result
print(move_zeros([0, 1, 0, 3, 12]))


# question 3
def first_repeating(lst):
    seen = []
    for i in lst:
        if i in seen:
            return i
        else:
            seen.append(i)
    return None
print(first_repeating([1, 2, 3, 4, 2, 5]))
