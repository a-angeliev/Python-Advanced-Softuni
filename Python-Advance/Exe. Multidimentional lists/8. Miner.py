def up(matrix, s_pos):
    s_row,s_col = s_pos
    move_cor = [s_row,s_col-1]
    if move_cor[0] >= 0 or move_cor[1] >= 0:
        if move_cor[0] < len(matrix) or move_cor[1] < len(matrix):
            if matrix[move_cor[0]][move_cor[1]] == "c":
                coals += 1
                matrix[move_cor[0]][move_cor[1]] = '*'
                matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col] = matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]]
            elif matrix[move_cor[0]][move_cor[1]] == "*":
                matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col] = matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]]
            elif matrix[move_cor[0]][move_cor[1]] == "e":
                return "game over"
    for row in range(rows):
        for col in range(rows):
            print(matrix[row][col], end = " ")
        print()
    return [move_cor]

rows = int(input())
matrix = []
global coals
coals = 0

commands = input().split()

for row in range(rows):
    matrix.append(input().split())
    for el in matrix[row]:
        if el == "*":
            coals +=1
print(matrix)
s_pos = []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "s":
            s_pos = [row,col]
            break
    if s_pos:
        break

for command in commands:
    if command == 'left':
        if not up(matrix,s_pos) == "game over":
            s_pos = up(matrix,s_pos)
            print(coals)



