def first_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return None  


print(first_duplicate([3, 1, 4, 2, 1, 5]))