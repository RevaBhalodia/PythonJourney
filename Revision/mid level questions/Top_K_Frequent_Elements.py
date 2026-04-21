from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

count = Counter(nums)
result = [item for item, freq in count.most_common(k)]

print(result)