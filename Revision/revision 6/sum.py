nums = [1, 9, 5, 5, 3, 7]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 10:
            print((nums[i], nums[j]))
