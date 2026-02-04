# 1
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)


# 2
nums = [5, 10, 15, 20]
new_list = []

for num in nums:
    new_list.append(num * 2)

print(new_list)
