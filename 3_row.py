# Jugador 1: ❌
# Jugador 2: 🟢
match_field = [["🔳","🔳","🔳"],["🔳","🔳","🔳"],["🔳","🔳","🔳"]]
player1 = True
turn = False
winner = ""
playing = True
filled = False

while playing:
    for row in match_field:
        for column in row:
            print(column, end=" ")
        print()
    if not filled:
        if player1:
            user_input = input("Player 1 introduce the coordenates of which box you'd want your mark to be drawn, separated by a coma: ").split(",")
            row = int(user_input[0])
            column = int(user_input[1])
            if row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
                row -= 1
                column -= 1
                match_field[row][column] = "❌"
                player1 = not player1
            else:
                print("Introduzca una coordenada valida")
        else:
            user_input = input("Player 2 introduce the coordenates of which box you'd want your mark to be drawn, separated by a coma: ").split(",")
            row = int(user_input[0])
            column = int(user_input[1])
            if row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
                row -= 1
                column -= 1
                match_field[row][column] = "🟢"
                player1 = not player1
            else:
                print("Introduzca una coordenada valida")
    for row in match_field:
        if row[0] == row[1] and row[1] == row[2]:                                                          # Horizontal
            if "🔳" != row[0] == "❌":
                winner = "player1"
                playing = False
            elif "🔳" != row[0] == "🟢":
                winner = "player2"
                playing = False
            break
        for column in row:
            index = row.index(column)
            if match_field[0][index] == match_field[1][index] == match_field[2][index]:                    # Vertical
                if "🔳" != match_field[0][index] == "❌":
                    winner = "player1"
                    playing = False
                elif "🔳" != match_field[0][index] == "🟢":
                    winner = "player2"
                    playing = False
                break
    else:
        if match_field[0][0] == match_field[1][1] and match_field[1][1] == match_field[2][2]:              # Diagonal
                if "🔳" != row[index] == "❌":
                    winner = "player1"
                    playing = False
                elif "🔳" != row[index] == "🟢":
                    winner = "player2"
                    playing = False
                break
        if match_field[2][0] == match_field[1][1] and match_field[1][1] == match_field[0][2]:            # Inversed diagonal
                if "🔳" != row[index] == "❌":
                    winner = "player1"
                    playing = False
                elif "🔳" != row[index] == "🟢":
                    winner = "player2"
                    playing = False
                break
        for i in match_field:
            for j in i:
                if j == '🔳':
                    filled = False
                    break
        if filled == True:
            winner = "None"

for row in match_field:
    for column in row:
        print(column, end=" ")
    print()
print(f"And the winner is: {winner}")