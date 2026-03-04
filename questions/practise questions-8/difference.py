nums = list(map(int, input("Enter numbers: ").split()))

min_val = nums[0]
max_diff = 0

for num in nums:
    if num < min_val:
        min_val = num
    elif num - min_val > max_diff:
        max_diff = num - min_val

print("Maximum Difference:", max_diff)