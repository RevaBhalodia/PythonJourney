from collections import deque

# BFS for Water Jug Problem
def water_jug_bfs():
    capacity_A = 4
    capacity_B = 3
    goal = 2

    visited = set()
    queue = deque()

    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()

        print(f"Current State: ({a}, {b})")

        if a == goal:
            print("\nGoal Reached!")
            return

        next_states = [
            (capacity_A, b),  # Fill A
            (a, capacity_B),  # Fill B
            (0, b),           # Empty A
            (a, 0),           # Empty B
            (a - min(a, capacity_B - b), b + min(a, capacity_B - b)),  # A -> B
            (a + min(b, capacity_A - a), b - min(b, capacity_A - a))   # B -> A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

# Run
water_jug_bfs()