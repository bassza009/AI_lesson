import random 
import copy

def print_board(board):
    print("\n")
    for row in board:
        print(" " + " | ".join(row))
        print("---" * 3)
    print()

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False      

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_full(board):
        return 0
    
    if maximizing_player:
        max_eval = float("-inf")
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'O'
            eval = minimax(board_copy, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = "X"
            eval = minimax(board_copy, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
    
def find_best_move(board):
    best_val = float("-inf")
    best_move = (-1, -1)

    # If it's the AI's first turn and the board is mostly empty, 
    # pick a random spot to speed up processing.
    empty_cells = get_empty_cells(board)
    if len(empty_cells) == 9:
        return random.choice(empty_cells)

    for i, j in empty_cells:
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = "O"

        if is_winner(board_copy, "O"):
            return (i, j)
            
        move_val = minimax(board_copy, 0, False)

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
            
    return best_move

def end_game(board):
    if is_winner(board, "X"):
        print_board(board)
        print('Congratulations!! You Win!')
        return True
    elif is_winner(board, "O"):
        print_board(board)
        print('AI "O" wins! Try again next round.')
        return True
    elif is_full(board):
        print_board(board)
        print("It's a Draw!")
        return True
    return False

def play_tic_tac_toe():
    # Initialize board with spaces instead of empty strings
    board = [[' ' for _ in range(3)] for _ in range(3)]
    user_turn = True  # True if user (X) goes, False if AI (O) goes

    while True:
        print_board(board)
        
        if user_turn:
            try:
                user_input = input("Enter your move (row and column, 0-2, space-separated): ")
                row, col = map(int, user_input.split())
                
                if row not in range(3) or col not in range(3):
                    print("Invalid coordinates! Please enter values between 0 and 2.")
                    continue
                
                if board[row][col] != " ":
                    print("Cell already taken! Try again.")
                    continue
                
                board[row][col] = "X"
                user_turn = False  # Switch turn
                
            except ValueError:
                print("Invalid input format. Please enter two numbers (e.g., 1 1).")
                continue
        else:
            print("AI 'O' is thinking.... ")
            row, col = find_best_move(board)
            board[row][col] = "O"
            user_turn = True  # Switch turn

        if end_game(board):
            break

if __name__ == "__main__":
    play_tic_tac_toe()