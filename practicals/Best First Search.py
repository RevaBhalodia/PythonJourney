import heapq

graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

h={'A':5,'B':3,'C':4,'D':2,'E':1,'F':0}

def best_first(start,goal):
    pq=[(h[start],start)]
    visited=set()

    while pq:
        _,node=heapq.heappop(pq)
        print(node)

        if node==goal:
            return

        visited.add(node)

        for n in graph[node]:
            if n not in visited:
                heapq.heappush(pq,(h[n],n))

best_first('A','F')