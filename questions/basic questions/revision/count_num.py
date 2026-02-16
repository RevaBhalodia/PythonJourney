def unique_once(nums):
    count = {}
    
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    result = []
    for num in count:
        if count[num] == 1:
            result.append(num)
    
    return result


print(unique_once([1,2,2,3,4,4,5]))