class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def clone_graph(node):
    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]

        copy = Node(node.val)
        visited[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node) if node else None
# Example
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1]   
node3.neighbors = [node1]   
cloned_node = clone_graph(node1)
print(cloned_node.val)  # Output: 1 
