def all_unique(nums):
    return len(nums) == len(set(nums))


nums = list(map(int, input("Enter numbers: ").split()))

print(all_unique(nums))