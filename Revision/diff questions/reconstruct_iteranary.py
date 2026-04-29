from collections import defaultdict

def find_itinerary(tickets):
    graph = defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    res = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        res.append(node)

    dfs("JFK")
    return res[::-1]

# Example
print(find_itinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))