# Jugador 1: ❌
# Jugador 2: 🟢
match_field = [["🔳","🔳","🔳"],["🔳","🔳","🔳"],["🔳","🔳","🔳"]]
turn = False
playing = True
player1 = True

while playing:   
    for box in match_field:
        for element in box:
            print(element, end=" ")
        print()
    turn = not turn
    while turn:
        if player1:
            user_input = input("Player1, please introduce the coordenates separated by coma: ").split(",")
            row = int(user_input[0])
            column = int(user_input[1])
            if 1 <= row and column <= 3 and "🔳" == match_field[row - 1][column - 1]:
                row -= 1
                column -= 1
                match_field[row][column] = "❌"
                player1 = not player1
            else:
                print("Wrong coordenate, introduce a valid one")
        else:
            user_input = input("Player2, please introduce the coordenates separated by coma: ").split(",")
            row = int(user_input[0])
            column = int(user_input[1])
            if 1 <= row and column <= 3 and "🔳" == match_field[row - 1][column - 1]:
                row -= 1
                column -= 1 
                match_field[row][column] = "🟢"
                player1 = not player1
            else:
                print("Wrong coordenate, introduce a valid one")
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
                break            