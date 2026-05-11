from collections import Counter
import heapq

def top_k_frequent(words, k):
    count = Counter(words)

    return heapq.nsmallest(
        k,
        count.keys(),
        key=lambda word: (-count[word], word)
    )

# Example
print(top_k_frequent(
    ["i","love","leetcode","i","love","coding"], 2
))
