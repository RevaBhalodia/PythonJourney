from collections import Counter

def least_interval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    
    # Count how many tasks have max frequency
    max_count = list(freq.values()).count(max_freq)

    # Formula
    time = (max_freq - 1) * (n + 1) + max_count

    return max(time, len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
print(least_interval(tasks, 2))