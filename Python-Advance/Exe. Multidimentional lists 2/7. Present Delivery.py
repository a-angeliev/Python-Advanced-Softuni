presents = int(input())
rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append(input().split())

happy_kids = 0
all_happy_kids = 0
santa_coor = []
move_coor = []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "V":
            happy_kids +=1
            all_happy_kids +=1
        elif matrix[row][col] == "S":
            santa_coor.append(row)
            santa_coor.append(col)


command = input()
while not command == "Christmas morning":

    dict_move = {"up": [santa_coor[0] - 1, santa_coor[1]],
                 "down": [santa_coor[0] + 1, santa_coor[1]],
                 "left": [santa_coor[0], santa_coor[1] - 1],
                 "right": [santa_coor[0], santa_coor[1] + 1]}

    move_coor.clear()
    move_coor.append(dict_move[command][0])
    move_coor.append(dict_move[command][1])
    if 0 <= move_coor[0] < rows and 0 <= move_coor[1] < rows:
        if matrix[move_coor[0]][move_coor[1]] == "-":
            matrix[move_coor[0]][move_coor[1]] = "S"
            matrix[santa_coor[0]][santa_coor[1]] = "-"
            santa_coor.clear()
            santa_coor.append(move_coor[0])
            santa_coor.append(move_coor[1])
        elif matrix[move_coor[0]][move_coor[1]] == "V":
            matrix[move_coor[0]][move_coor[1]] = "S"
            matrix[santa_coor[0]][santa_coor[1]] = "-"
            santa_coor.clear()
            santa_coor.append(move_coor[0])
            santa_coor.append(move_coor[1])
            presents -= 1
            happy_kids  -=1
            if presents == 0:
                break
        elif matrix[move_coor[0]][move_coor[1]] == "C":
            matrix[move_coor[0]][move_coor[1]] = "S"
            matrix[santa_coor[0]][santa_coor[1]] = "-"
            if matrix[move_coor[0]-1][move_coor[1]] == "V" or matrix[move_coor[0]-1][move_coor[1]] == "X":

                if matrix[move_coor[0] - 1][move_coor[1]] == "V":
                    happy_kids -= 1
                presents -=1
                matrix[move_coor[0] - 1][move_coor[1]] = "-"
                if presents == 0:
                    break
            if matrix[move_coor[0]+1][move_coor[1]] == "V" or matrix[move_coor[0]+1][move_coor[1]] == "X":

                presents -=1
                if matrix[move_coor[0] + 1][move_coor[1]] == "V":
                    happy_kids -=1
                matrix[move_coor[0] + 1][move_coor[1]] = "-"
                if presents == 0:
                    break
            if matrix[move_coor[0]][move_coor[1]-1] == "V" or matrix[move_coor[0]][move_coor[1]-1] == "X":

                presents -=1
                if matrix[move_coor[0]][move_coor[1] - 1] == "V":
                    happy_kids -=1
                matrix[move_coor[0]][move_coor[1] - 1] = "-"
                if presents == 0:
                    break
            if matrix[move_coor[0]][move_coor[1]+1] == "V" or matrix[move_coor[0]+1][move_coor[1]+1] == "X":

                presents -=1
                if matrix[move_coor[0]][move_coor[1] + 1] == "V":
                    happy_kids -=1
                matrix[move_coor[0]][move_coor[1] + 1] = "-"
                if presents == 0:
                    break
        elif matrix[move_coor[0]][move_coor[1]] == "X":
            matrix[santa_coor[0]][santa_coor[1]] = "-"
            santa_coor.clear()
            santa_coor.append(move_coor[0])
            santa_coor.append(move_coor[1])
    command = input()

if presents == 0 and not happy_kids == 0:
    print("Santa ran out of presents!")

for row in range(rows):
    for col in range(rows):
        print(matrix[row][col], end = " ")
    print()

if happy_kids == 0:
    print(f"Good job, Santa! {all_happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {happy_kids} nice kid/s.")


