# Player 1: ❌
# Player 2: 🟢
board = [["🔳","🔳","🔳"],["🔳","🔳","🔳"],["🔳","🔳","🔳"]]
playing = True
player = "Player 1"
moves = 0                                                                                                                         # All the needed variables for the program 
winner = ""
last_move = ""
accept_rules = ["s","y","yes", "si"]

while (rules := input('''These are the rules for the Tic Tac Toe game:
    
1. You may place your symbol between the coordenates 1,1 and 3,3, in that same format.
2. You cannot place your symbol on a box that has been previously ocupied by the other player.
3. If you lose, please buy some candy for the winner (optional).

Introduce [y] or [s] to accept the rules, or [n] to reject them.
Your choice: ''')).lower() not in accept_rules:
    print("You must accept the rules to play")

while playing:
    for row in board:
        for column in row:
            print(column, end="")
        print()
    play = input(f"{player} choice (Ej: 3,1): ").split(",")
    row = int(play[0])
    column = int(play[1])
    if 1 <= row <= 3 and 1 <= column <= 3 and board[row - 1][column - 1] == "🔳" and len(play) == 2:                               # This part of the code arranges which player 
        row -= 1; column -= 1; moves += 1                                                                                          # moves it's tile and where, it alse checks if the box 
        if player == "Player 1":                                                                                                   # where he wants to "paint" his play has been ocupied.    
            board[row][column] = "❌"                                                                                              # It also saves the value of the last player's turn  
            player = "Player 2"                                                                                        
            last_move = "Player 1"
        else:
            board[row][column] = "🟢"
            player = "Player 1" 
            last_move = "Player 2"
    else:
        if 1 <= row <= 3 and 1 <= column <= 3 and board[row - 1][column - 1] != "🔳" and len(play) == 2:
            error = f"This box is ocupied by {board[row - 1][column - 1]}."
        elif len(play) > 2:
            error = f"The format of your play: {','.join(play)} isn't correct, please, introduce one like this: 1,2."
        elif (1 > row or row > 3) or (1 > column or column > 3):
            error = f"Your play: {row},{column} is out of the bounds of the board."  
        print(error)  
    # These three next lines decide whether the player wins by making a 3 in a row in a horizontal, vertical or diagonal way.
    horizontals = ((board[0][0] == board[0][1] == board[0][2] != "🔳") or (board[1][0] == board[1][1] == board[1][2] != "🔳") or (board[2][0] == board[2][1] == board[2][2] != "🔳")) 
    diagonals = ((board[0][0] == board[1][1] == board[2][2] != "🔳") or (board[2][0] == board[1][1] == board[0][2] != "🔳"))
    verticals = ((board[0][0] == board[1][0] == board[2][0] != "🔳") or (board[0][1] == board[1][1] == board[2][1] != "🔳") or (board[0][2] == board[1][2] == board[2][2] != "🔳"))
    win_condition = any([verticals, horizontals, diagonals])
    if win_condition:
        winner = last_move
        playing = False
    # The moves variable checks if the match is a tie, the maximun number of moves in a tic tac toe match is 9, which may end up in tie.
    elif not win_condition and moves == 9:
        winner = "None, it's a tie"
        playing = False
for row in board:
    for column in row:
        print(column, end="")
    print()
print(f"And the winner is: {winner}")