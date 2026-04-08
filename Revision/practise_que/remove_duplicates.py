def remove_duplicates(arr):
    result = []
    
    for item in arr:
        if item not in result:
            result.append(item)
    
    return result


numbers = [1, 2, 2, 3, 4, 3, 5]
print(remove_duplicates(numbers))