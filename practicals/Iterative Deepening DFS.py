graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

def dls(node,goal,depth):
    if depth==0 and node==goal:
        return True
    if depth>0:
        for child in graph[node]:
            if dls(child,goal,depth-1):
                return True
    return False

def iddfs(start,goal):
    depth=0
    while True:
        if dls(start,goal,depth):
            print("Found at depth",depth)
            return
        depth+=1

iddfs('A','F')