def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result


numbers = [1,2,2,3,4,4,5,1,6]

print(remove_duplicates(numbers))