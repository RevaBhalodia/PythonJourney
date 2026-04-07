def flatten_list(nested):
    flat = []

    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)

    return flat

data = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(data))