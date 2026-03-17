import math

# Initialize board
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")

def check_winner():
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for i,j,k in win_positions:
        if board[i] == board[j] == board[k] and board[i] != " ":
            return board[i]
    
    if " " not in board:
        return "Draw"
    
    return None

# Minimax with Alpha-Beta Pruning
def minimax(is_maximizing, alpha, beta):
    result = check_winner()
    
    if result == "X":
        return -1
    elif result == "O":
        return 1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

# AI move
def best_move():
    best_score = -math.inf
    move = -1
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -math.inf, math.inf)
            board[i] = " "
            
            if score > best_score:
                best_score = score
                move = i
    
    board[move] = "O"

# Game loop
def play():
    print("You are X, AI is O")
    
    while True:
        print_board()
        
        if check_winner():
            break
        
        # Player move
        move = int(input("Enter position (0-8): "))
        if board[move] != " ":
            print("Invalid move!")
            continue
        
        board[move] = "X"
        
        if check_winner():
            break
        
        # AI move
        best_move()
    
    print_board()
    result = check_winner()
    
    if result == "Draw":
        print("It's a Draw!")
    else:
        print(result, "wins!")

# Run the game
play()