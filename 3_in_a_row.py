# Jugador 1: ❌
# Jugador 2: 🟢
match_field = []
playing = True
player1 = True
moves = 0

for i in range(3):
    match_field.append([])
    for j in range(3):
        match_field[i].append("🔳")

match match_field:
    case match_field if match_field[0][0] == match_field[1][1] and match_field[1][1] == match_field[2][2]:
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][0] == match_field[1][0] and match_field[1][0] == match_field[2][0]:
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case match_field if match_field[0][0] == match_field[0][1] and match_field[0][1] == match_field[0][2]:
        if match_field[0][0] == "❌":
            winner = "player1"
        else:
            winner = "player2"
    case _:
        print("No one is the winner")

while moves < 9:
    for row in match_field:
        for column in row:
            print(column, end=" ")
        print()
    if player1:
        user_input = input("Player 1 introduce the coordenates of which box you'd want your mark to be drawn, separated by a coma: ").split(",")
        row = int(user_input[0])
        column = int(user_input[1])
        if row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
            row -= 1
            column -= 1
            match_field[row][column] = "❌"
            player1 = not player1
            moves += 1
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
            moves += 1
        else:
            print("Introduzca una coordenada valida")