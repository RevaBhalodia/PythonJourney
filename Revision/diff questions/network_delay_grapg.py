import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float("inf") for i in range(1, n+1)}
    dist[k] = 0

    heap = [(0, k)]

    while heap:
        time, node = heapq.heappop(heap)

        if time > dist[node]:
            continue

        for nei, w in graph[node]:
            if time + w < dist[nei]:
                dist[nei] = time + w
                heapq.heappush(heap, (dist[nei], nei))

    res = max(dist.values())
    return res if res < float("inf") else -1
# Example
print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # Output: 2