# Jugador 1: ❌
# Jugador 2: 🟢
match_field = []
playing = True
player1 = True

for i in range(3):
    match_field.append([])
    for j in range(3):
        match_field[i].append("🔳")

while True:
    for row in match_field:
        for column in row:
            print(column, end=" ")
        print()
    if playing:
        if player1:
            user_input = input("Player 1 introduce the coordenates of which box you'd want your mark to be drawn, separated by a coma: ").split(",")
            row = int(user_input[0])
            column = int(user_input[1])
            if row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
                row -= 1
                column -= 1
                match_field[row][column] = "❌"
                player1 = not player1
                for box in match_field:
                    if "🔳" not in box:
                        playing = False
                        break
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
                for box in match_field:
                    if "🔳" not in box:
                        playing = False
                        break
            else:
                print("Introduzca una coordenada valida")
    else:
        break

match match_field:
    case match_field if match_field[0][0] == match_field[1][1] and match_field[1][1] == match_field[2][2]:    # Diagonal
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][2] == match_field[1][1] and match_field[1][1] == match_field[2][0]:    # Inversed Diagonal
        if match_field[0][2] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][0] == match_field[1][0] and match_field[1][0] == match_field[2][0]:    # Horizontal 1
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[1][0] == match_field[1][1] and match_field[1][1] == match_field[1][2]:    # Horizontal 2
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[2][0] == match_field[2][1] and match_field[2][1] == match_field[2][2]:    # Horizontal 3
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][0] == match_field[1][0] and match_field[1][0] == match_field[2][0]:    # Vertical 1
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][1] == match_field[1][1] and match_field[1][1] == match_field[2][1]:    # Vertical 2
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][2] == match_field[1][2] and match_field[1][2] == match_field[2][2]:    # Vertical 3
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case _:                                                                                                   # Tie
        winner = "None"
print(f"Winner = {winner}")