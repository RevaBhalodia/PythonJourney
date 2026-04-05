import heapq

graph = {
'A':[('B',1),('C',4)],
'B':[('D',2),('E',5)],
'C':[('F',1)],
'D':[],
'E':[],
'F':[]
}

def ucs(start,goal):
    pq=[(0,start)]
    visited=set()

    while pq:
        cost,node=heapq.heappop(pq)

        if node==goal:
            print("Cost:",cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for n,c in graph[node]:
            heapq.heappush(pq,(cost+c,n))

ucs('A','F')