def is_terminal(coin):
    return coin <= 0

def minimax(coin, maximizing_player):
    if is_terminal(coin):
        if maximizing_player:
            return -1 
        else:
            return 1   

    if maximizing_player:
        max_eval = float("-inf")
        for pick in range(1, min(2, coin) + 1):
            eval = minimax(coin - pick, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for pick in range(1, min(2, coin) + 1):
            eval = minimax(coin - pick, True)
            min_eval = min(min_eval, eval)
        return min_eval

def find_first_move(coin):
    
    if coin >= 1 and minimax(coin - 1, False) == 1:
        return 1
    
    if coin >= 2 and minimax(coin - 2, False) == 1:
        return 2
    
    return 0

if __name__ == "__main__":
    coin = int(input())
    print(find_first_move(coin))
