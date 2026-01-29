# list
# question 1
nums = [1, 2, 2, 3, 4, 3, 5]

unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print(unique)


# question 2
nums = [5, 12, 7, 20, 3, 18]

average = sum(nums) / len(nums)

result = []

for i in nums:
    if i > average:
        result.append(i)

print(result)


# question 3
nums = [1, 2, 3, 4, 5]
k = 2

rotated = nums[k:] + nums[:k]

print(rotated)
