def common_elements(a, b):
    result = []
    
    for item in a:
        if item in b and item not in result:
            result.append(item)
    
    return result


list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]

print(common_elements(list1, list2))