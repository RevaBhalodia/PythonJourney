import random

N = 4

def calculate_conflicts(board):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current_conflicts = calculate_conflicts(board)
        neighbors = []

        for i in range(N):
            for j in range(N):
                if j != board[i]:
                    new_board = board[:]
                    new_board[i] = j
                    neighbors.append(new_board)

        best_neighbor = min(neighbors, key=calculate_conflicts)
        best_conflicts = calculate_conflicts(best_neighbor)

        if best_conflicts >= current_conflicts:
            return board

        board = best_neighbor


solution = hill_climbing()
print("Hill Climbing Solution:", solution)
print("Conflicts:", calculate_conflicts(solution))