# Jugador 1: ❌
# Jugador 2: 🟢
board = [["🔳","🔳","🔳"],["🔳","🔳","🔳"],["🔳","🔳","🔳"]]
player1 = True
winner = ""
moves = 0
playing = True
# while playing:
#     for row in board:
#         for column in row:
#             print(column, end=" ")
#         print()
#     if player1:
#         user_input = input("Player 1 choice (Ej: 3,1): ").split(",")
#         row = int(user_input[0])
#         column = int(user_input[1])
#         if 1 <= row and column <= 3 and board[row - 1][column - 1] == "🔳":
#             row -= 1; column -= 1
#             board[row][column] = "❌"
#             player1 = not player1
#             moves += 1
#         else:
#             print("Introduce a valid coordenate")
#     else:
#         user_input = input("Player 2 choice (Ej: 1,1): ").split(",")
#         row = int(user_input[0])
#         column = int(user_input[1])
#         if 1 <= row and column <= 3 and board[row - 1][column - 1] == "🔳":
#             row -= 1; column -= 1
#             board[row][column] = "🟢"
#             player1 = not player1
#             moves += 1
#         else:
#             print("Introduce a valid coordenate")
#     diagonal = (board[0][0] == board[1][1] == [2][2] or board[2][0] == board[1][1] == board[0][2])
#     horizontal = (board[0][0] == board[0][1] == [0][2] or board[1][0] == board[1][1] == [1][2] or board[2][0] == board[2][1] == [2][2])
#     vertical = (board[0][0] == board[1][0] == [2][0] or board[0][1] == board[1][1] == [2][1] or board[0][2] == board[2][1] == [2][2])   
#     else:
#         if moves == 9:
#             winner = "None, it's a Tie"
#             playing = False
# for row in board:
#     for column in row:
#         print(column, end=" ")
#     print()
# print(f"And the winner is: {winner}")

diagonal = (((board[0][0] == board[1][1] == [2][2]) != "🔳") or ((board[2][0] == board[1][1] == board[0][2]) != "🔳"))
# horizontal = (board[0][0] == board[0][1] == [0][2] or board[1][0] == board[1][1] == [1][2] or board[2][0] == board[2][1] == [2][2])
# vertical = (board[0][0] == board[1][0] == [2][0] or board[0][1] == board[1][1] == [2][1] or board[0][2] == board[2][1] == [2][2])
print(diagonal)