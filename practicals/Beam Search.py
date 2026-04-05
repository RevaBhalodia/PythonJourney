import heapq

def heuristic(n):
    h={'A':5,'B':4,'C':3,'D':2,'E':1,'F':0}
    return h[n]

graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

def beam(start,goal,width=2):
    queue=[start]

    while queue:
        next_level=[]

        for node in queue:
            print(node)
            if node==goal:
                return

            next_level.extend(graph[node])

        queue=sorted(next_level,key=heuristic)[:width]

beam('A','F')