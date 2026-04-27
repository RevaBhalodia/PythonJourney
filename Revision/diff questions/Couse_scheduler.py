from collections import defaultdict, deque

def find_order(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return order if len(order) == numCourses else []

# Example
print(find_order(4, [[1,0],[2,0],[3,1],[3,2]]))