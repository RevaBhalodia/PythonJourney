nums = list(map(int, input("Enter numbers: ").split()))

result = {}

for i in range(len(nums)):
    num = nums[i]

    if num not in result:
        result[num] = []

    result[num].append(i)

print(result)