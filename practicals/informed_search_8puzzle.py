import heapq

goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

initial = ((1,2,3),
           (4,0,6),
           (7,5,8))


# Heuristic: misplaced tiles
def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced


# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate neighbors
def neighbors(state):
    x, y = find_blank(state)
    moves = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [list(row) for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            moves.append(tuple(tuple(row) for row in new))

    return moves


# Greedy Best First Search
def greedy_search(start):
    visited = set()
    pq = []

    heapq.heappush(pq, (heuristic(start), start))

    while pq:
        h, state = heapq.heappop(pq)

        print("State:", state)

        if state == goal:
            print("Goal reached using Greedy Search")
            return

        visited.add(state)

        for n in neighbors(state):
            if n not in visited:
                heapq.heappush(pq, (heuristic(n), n))


# A* Search
def astar(start):
    visited = set()
    pq = []

    heapq.heappush(pq, (heuristic(start), 0, start))

    while pq:
        f, g, state = heapq.heappop(pq)

        print("State:", state)

        if state == goal:
            print("Goal reached using A*")
            return

        visited.add(state)

        for n in neighbors(state):
            if n not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(n)
                heapq.heappush(pq, (new_f, new_g, n))


print("Greedy Best First Search\n")
greedy_search(initial)

print("\nA* Search\n")
astar(initial)