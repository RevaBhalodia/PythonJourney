import heapq
from collections import defaultdict

def find_cheapest_price(n, flights, src, dst, k):
    graph = defaultdict(list)

    for u, v, price in flights:
        graph[u].append((v, price))

    heap = [(0, src, 0)]

    while heap:
        cost, node, stops = heapq.heappop(heap)

        if node == dst:
            return cost

        if stops <= k:
            for nei, price in graph[node]:
                heapq.heappush(
                    heap,
                    (cost + price, nei, stops + 1)
                )

    return -1
# Example
print(find_cheapest_price(
    3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
))
# Output: 200