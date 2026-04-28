def bellman_ford(n, edges, src):
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return "Negative cycle detected"

    return dist

# Example
edges = [(0,1,4),(0,2,5),(1,2,-3),(2,3,4)]
print(bellman_ford(4, edges, 0))