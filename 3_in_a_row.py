import os
# Jugador 1: ❌
# Jugador 2: 🟢
match_field = []
playing = True
player1 = True

for i in range(3):
    match_field.append([])
    for j in range(3):
        match_field[i].append("🔳")

while playing:
    for row in match_field:
        for column in row:
            print(column, end=" ")
        print()
    if player1:
        user_input = input("Jugador 1 introduce las coordenadas de la casilla separadas por comas: ").split(",")
        row = int(user_input[0])
        column = int(user_input[1])
        if row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
            row -= 1
            column -= 1
            match_field[row][column] = "❌"
            player1 = not player1
            os.system("cls")
        else:
            print("Introduzca una coordenada valida")
    else:
        user_input = input("Jugador 2 introduce las coordenadas de la casilla separadas por comas: ").split(",")
        row = int(user_input[0])
        column = int(user_input[1])
        if row and column <= 3 and match_field[row - 1][column - 1] == "🔳":
            row -= 1
            column -= 1
            match_field[row][column] = "🟢"
            player1 = not player1
        else:
            print("Introduzca una coordenada valida")
