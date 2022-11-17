# Jugador 1: ❌
# Jugador 2: 🟢
match_field = []
turn = True
playing = True
player1 = True

for i in range(3):
    match_field.append([])
    for j in range(3):
        match_field[i].append("🔳")

while turn:
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
                if 1 <= row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
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
                if 1 <= row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
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

print(f"Winner = {winner}")