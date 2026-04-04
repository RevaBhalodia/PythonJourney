import random
import math

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


def simulated_annealing():
    board = [random.randint(0, N - 1) for _ in range(N)]
    temperature = 100
    cooling = 0.95

    while temperature > 0.1:
        current_conflicts = calculate_conflicts(board)

        if current_conflicts == 0:
            return board

        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)

        new_board = board[:]
        new_board[i] = j

        new_conflicts = calculate_conflicts(new_board)
        delta = new_conflicts - current_conflicts

        if delta < 0:
            board = new_board
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                board = new_board

        temperature *= cooling

    return board


solution = simulated_annealing()
print("Simulated Annealing Solution:", solution)
print("Conflicts:", calculate_conflicts(solution))