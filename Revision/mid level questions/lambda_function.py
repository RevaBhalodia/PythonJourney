from functools import reduce

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

squared    = list(map(lambda x: x**2, nums))
evens      = list(filter(lambda x: x % 2 == 0, nums))
total      = reduce(lambda a, b: a + b, nums)
top3       = sorted(set(nums), reverse=True)[:3]

print("Squared:", squared)
print("Evens:  ", evens)
print("Sum:    ", total)
print("Top 3:  ", top3)