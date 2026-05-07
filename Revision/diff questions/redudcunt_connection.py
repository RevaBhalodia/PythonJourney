def find_redundant_connection(edges):
    parent = list(range(len(edges) + 1))

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x

    for u, v in edges:
        pu, pv = find(u), find(v)

        if pu == pv:
            return [u, v]

        parent[pu] = pv
# Example usage:
# In this problem, a tree is an undirected graph that is connected and has no cycles    
# The given input is a graph that started as a tree with N nodes (with distinct values from 1 to N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents an undirected edge connecting nodes u and v.
# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. 
