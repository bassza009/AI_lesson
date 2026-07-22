def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '_']

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False      

def minimax(board, depth, maximizing_player):
    if is_winner(board, "X"):
        return 10 - depth
    elif is_winner(board, "O"):
        return -10 + depth
    elif len(get_empty_cells(board)) == 0:
        return 0
    
    if maximizing_player:
        max_eval = float("-inf")
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'  
            eval = minimax(board, depth + 1, False)
              
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'  
            eval = minimax(board, depth + 1, True)
            
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float("-inf")
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        move_val = minimax(board, 0, False)
        board[i][j] = "_"

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

        
        if best_val == 10:
            break
            
    return best_move

def play_tic_tac_toe():
    
    board = [list(input()) for _ in range(3)]

    row, col = find_best_move(board)
    print((row * 3) + col)
        
if __name__ =="__main__":
    play_tic_tac_toe()