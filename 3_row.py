# Jugador 1: ❌
# Jugador 2: 🟢
match_field = []
player1 = True
moves = 0
winner = ""
playing = True

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
                playing = False if "🔳" not in match_field else True
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
                playing = False if "🔳" not in match_field else True
            else:
                print("Introduzca una coordenada valida")
    for row in match_field:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == "❌":
                winner = "player1"
            else:
                winner = "player2"
        for column in row:
            if row[column] == row[column] == row[column]:
                if row[column] == "":
                    winner = "player1"
                else:
                    winner = "player2"
    else:
        if match_field[0][0] == match_field[1][1] and match_field[1][1] == match_field[2][2]:
            if row[0] == "❌":
                winner = "player1"
            else:
                winner = "player2"
        if match_field[2][0] == match_field[1][1] and match_field[1][1] == match_field[0][2]:
            if row[0] == "❌":
                winner = "player1"
            else:
                winner = "player2"
        break
    
print(f"And the winner is: {winner}")