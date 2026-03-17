nums = [1,2,2,3,3,3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print("Frequency:", freq)