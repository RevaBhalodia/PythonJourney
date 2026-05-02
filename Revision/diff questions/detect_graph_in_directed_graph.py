def has_cycle(graph):
    visited = set()
    path = set()

    def dfs(node):
        if node in path:
            return True
        if node in visited:
            return False

        path.add(node)
        visited.add(node)

        for nei in graph[node]:
            if dfs(nei):
                return True

        path.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False

# Example
graph1 = {0: [1], 1: [2], 2: [0]}  # Cycle exists
graph2 = {0: [1], 1: [2], 2: []}   # No cycle
print(has_cycle(graph1))  # Output: True    
print(has_cycle(graph2))  # Output: False   
