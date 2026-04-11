def merge_sorted(a, b):
    i = j = 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged


list1 = [1,3,5,7]
list2 = [2,4,6,8]

print(merge_sorted(list1, list2))