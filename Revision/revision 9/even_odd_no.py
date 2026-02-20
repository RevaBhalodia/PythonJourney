def group_even_odd(nums):
    result = {
        "even": [],
        "odd": []
    }

    for num in nums:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)

    return result


numbers = [1, 2, 3, 4, 5]
print(group_even_odd(numbers))