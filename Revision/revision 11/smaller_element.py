def elements_with_smaller_right(nums):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                result.append(nums[i])
                break  

    return result


# Example
print(elements_with_smaller_right([4, 2, 1, 3]))