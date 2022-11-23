# Jugador 1: ❌
# Jugador 2: 🟢
board = [["🔳","🔳","🔳"],["🔳","🔳","🔳"],["🔳","🔳","🔳"]]
playing = True
player = "Player 1"
moves = 0
winner = ""
last_move = ""
while playing:
    for row in board:
        for column in row:
            print(column, end=" ")
        print()
    user_input = input(f"{player} choice (Ej: 3,1): ").split(",")
    row = int(user_input[0])
    column = int(user_input[1])
    if 1 <= row <= 3 and 1 <= column <= 3 and board[row - 1][column - 1] == "🔳":
        row -= 1; column -= 1; moves += 1
        if player == "Player 1":
            board[row][column] = "❌"
            player = "Player 2"
            last_move = "player 1"
        else:
            board[row][column] = "🟢"
            player = "Player 1" 
            last_move = "player 2"
    else:
        print("Please introduce a valid coordenate")    
    horizontals = ((board[0][0] == board[0][1] == board[0][2] != "🔳") or (board[1][0] == board[1][1] == board[1][2] != "🔳") or (board[2][0] == board[2][1] == board[2][2] != "🔳")) 
    diagonals = ((board[0][0] == board[1][1] == board[2][2] != "🔳") or (board[2][0] == board[1][1] == board[0][2] != "🔳"))
    verticals = ((board[0][0] == board[1][0] == board[2][0] != "🔳") or (board[0][1] == board[1][1] == board[2][1] != "🔳") or (board[0][2] == board[1][2] == board[2][2] != "🔳"))
    win_condition = any([verticals, horizontals, diagonals])
    if win_condition:
        winner = last_move
        playing = False
    elif moves == 9:
        winner = "None, it's a tie"
        playing = False
for row in board:
        for column in row:
            print(column, end=" ")
        print()
print(f"And the winner is: {winner}")