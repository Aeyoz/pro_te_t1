# Jugador 1: ❌
# Jugador 2: 🟢
board = [["🔳","🔳","🔳"],["🔳","🔳","🔳"],["🔳","🔳","🔳"]]
player1 = True
winner = ""
moves = 0
playing = True
while playing:
    for row in board:
        for column in row:
            print(column, end=" ")
        print()
    if player1:
        user_input = input("Player 1 choice (Ej: 3,1): ").split(",")
        row = int(user_input[0])
        column = int(user_input[1])
        if 1 <= row and column <= 3 and board[row - 1][column - 1] == "🔳":
            row -= 1; column -= 1
            board[row][column] = "❌"
            player1 = not player1
            moves += 1
        else:
            print("Introduce a valid coordenate")
    else:
        user_input = input("Player 2 choice (Ej: 1,1): ").split(",")
        row = int(user_input[0])
        column = int(user_input[1])
        if 1 <= row and column <= 3 and board[row - 1][column - 1] == "🔳":
            row -= 1; column -= 1
            board[row][column] = "🟢"
            player1 = not player1
            moves += 1
        else:
            print("Introduce a valid coordenate")
    for row in board:
        if row[0] == row[1] == row[2]:                                                  # Horizontal
            if "🔳" != row[0] == "❌":
                winner = "player1"
                playing = False
            elif "🔳" != row[0] == "🟢":
                winner = "player2"
                playing = False
            break
        for column in row:
            index = row.index(column)
            if board[0][index] == board[1][index] == board[2][index]:                    # Vertical
                if "🔳" != board[0][index] == "❌":
                    winner = "player1"
                    playing = False
                elif "🔳" != board[0][index] == "🟢":
                    winner = "player2"
                    playing = False
                break
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:                    # Diagonal
            if "🔳" != row[index] == "❌":
                winner = "player1"
                playing = False
            elif "🔳" != row[index] == "🟢":
                winner = "player2"
                playing = False
            break
        elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:                  # Inversed diagonal
            if "🔳" != row[index] == "❌":
                winner = "player1"
                playing = False
            elif "🔳" != row[index] == "🟢":
                winner = "player2"
                playing = False
            break
    else:
        if moves == 9:
            winner = "None, it's a Tie"
            playing = False
for row in board:
    for column in row:
        print(column, end=" ")
    print()
print(f"And the winner is: {winner}"