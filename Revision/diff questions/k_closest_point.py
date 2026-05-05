import heapq

def k_closest(points, k):
    heap = []

    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (dist, x, y))

    return [[x, y] for (_, x, y) in heapq.nsmallest(k, heap)]
# Example
print(k_closest([[1, 3], [-2, 2]], 1))  # Output: [[-2, 2]]
