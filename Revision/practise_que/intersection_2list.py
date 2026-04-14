def intersection(a, b):
    set1 = set(a)
    result = []

    for num in b:
        if num in set1:
            result.append(num)

    return list(set(result))


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print("Intersection:", intersection(a, b))