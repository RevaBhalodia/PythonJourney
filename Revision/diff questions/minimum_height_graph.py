from collections import defaultdict, deque

def find_min_height_trees(n, edges):
    if n == 1:
        return [0]

    graph = defaultdict(set)

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    leaves = deque(
        [i for i in range(n) if len(graph[i]) == 1]
    )

    remaining = n

    while remaining > 2:
        size = len(leaves)
        remaining -= size

        for _ in range(size):
            leaf = leaves.popleft()

            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)

    return list(leaves)
# Example
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(find_min_height_trees(n, edges))
# Output: [3, 4]
