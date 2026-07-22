def is_winner(coin):
    if(coin <= 0 ):
        return True
    return False

def minimax(coin,maximixing_player):
    if is_winner(coin):
        if maximixing_player :
            return -1
        else :
            return 1

    if maximixing_player :
        max_eval = float("-inf")
        for pick in range(1,min(2,coin)+1):
            eval = minimax(coin-pick,False)
            max_eval = max(max_eval,eval)
        return max_eval
    else :
        min_eval = float("inf")
        for pick in range(1,min(2,coin)+1):
            eval = minimax(coin-pick,True)
            min_eval = min(min_eval,eval)
        return min_eval
def find_best_pick(coin):
    best_val = float("-inf")
    best_pick = 1
    max_pick = 2
    for pick in range(1,min(max_pick,coin)+1):
        move_val = minimax(coin-pick,False)

        if move_val > best_val:
            best_val = move_val
            best_pick = pick
        if best_val == 1:
            break
    return best_pick    
def play_coin_game():
    coin = 10
    max_pick = 2
    user_turn = True
    while True :
        if user_turn:
            try:                
                user_pick_coin = int(input(f"Pick coin no more than {max_pick} : "))
                while(user_pick_coin > max_pick or user_pick_coin<=0 or user_pick_coin > coin):
                    user_pick_coin = int(input(f"Pick coin again!! no more than {max_pick} : "))
                coin -= user_pick_coin
                print(coin)
                

                if is_winner(coin):
                    print("You Win!!")
                    break
                user_turn = False
            except(ValueError):
                print("Invalid input")
                continue
                
        else:
            print("AI is thinking...")
            coin -= find_best_pick(coin)
            print(f"Coin left {coin}")
            if is_winner(coin):
                print("You Lose!!")
                break
            user_turn = True

if __name__ == "__main__":
    play_coin_game()