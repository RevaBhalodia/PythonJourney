from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    
    # Sort based on frequency
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    
    return result


nums = [1,1,1,2,2,3,3,3,3,4]
print(top_k_frequent(nums, 2))