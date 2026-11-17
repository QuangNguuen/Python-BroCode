import random
board = []

for row in range(4):
    board.append([])
    for column in range(4):
        board[row].append("")

print(board)



for row in range(4):
    for col in range(4):
        board([row][col]) = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(board)