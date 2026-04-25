class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    cost = 0

    for u, v, w in edges:
        if uf.union(u, v):
            cost += w

    return cost

# Example
edges = [
    (0,1,4),
    (0,2,3),
    (1,2,1),
    (1,3,2),
    (2,3,4)
]

print(kruskal(4, edges))  # Output: 6