from collections import Counter
import heapq

def least_interval(tasks, n):
    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = []

    while max_heap or queue:
        time += 1

        if max_heap:
            cnt = heapq.heappop(max_heap) + 1
            if cnt != 0:
                queue.append((cnt, time + n))

        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.pop(0)[0])

    return time

# Example
print(least_interval(["A","A","A","B","B","B"], 2))
# Output: 8