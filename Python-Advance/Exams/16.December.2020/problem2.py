string = input()
rows = int(input())
matrix = []
move_coor = []
player_coor = []
for row in range(rows):
    matrix.append([])
    col = 0
    for el in input():
        matrix[row].append(el)
        if el == "P":
            player_coor.append(row)
            player_coor.append(col)
        col += 1

moves = int(input())

for _ in range(moves):
    command = input()
    move = {"right": [player_coor[0], player_coor[1] + 1], "left": [player_coor[0], player_coor[1] - 1],
             "up": [player_coor[0] - 1, player_coor[1]], "down": [player_coor[0] + 1, player_coor[1]]}

    if 0 <= move[command][0] < rows and  0 <= move[command][1] < rows:
        move_coor.clear()
        move_coor.append(move[command][0])
        move_coor.append(move[command][1])
        el = matrix[move_coor[0]][move_coor[1]]
        if el.isalpha():
            string += matrix[move_coor[0]][move_coor[1]]
            matrix[player_coor[0]][player_coor[1]] = "-"
            player_coor.clear()
            player_coor.append(move_coor[0])
            player_coor.append(move_coor[1])
            matrix[player_coor[0]][player_coor[1]] = "P"
        else:
            matrix[player_coor[0]][player_coor[1]] = "-"
            player_coor.clear()
            player_coor.append(move_coor[0])
            player_coor.append(move_coor[1])
            matrix[player_coor[0]][player_coor[1]] = "P"
    else:
        if string:
            string = string[:-1]
print(string)
for row in range(rows):
    for col in range(rows):
        print(matrix[row][col], end = '')
    print()