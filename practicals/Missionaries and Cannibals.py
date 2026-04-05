from collections import deque

def is_valid(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def bfs():
    start = (3,3,1)
    queue = deque([start])
    visited = set([start])

    while queue:
        m,c,boat = queue.popleft()
        print(m,c,boat)

        if (m,c,boat) == (0,0,0):
            print("Goal reached")
            return

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm,dc in moves:
            if boat == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            if 0<=new[0]<=3 and 0<=new[1]<=3 and is_valid(new[0],new[1]):
                if new not in visited:
                    visited.add(new)
                    queue.append(new)

bfs()