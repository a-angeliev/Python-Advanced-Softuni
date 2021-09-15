
coals = 0
flag = True
def left(matrix, s_pos):
    global coals
    value = s_pos.copy()
    s_row,s_col = s_pos
    move_cor = [s_row,s_col-1]
    if move_cor[0] >= 0 or move_cor[1] >= 0:
        if move_cor[0] < len(matrix) or move_cor[1] < len(matrix):
            if matrix[move_cor[0]][move_cor[1]] == "c":
                coals -= 1
                matrix[move_cor[0]][move_cor[1]] = '*'
                matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col] = matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "*":
                matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col] = matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "e":
                return "game over"
    return value


def up(matrix,s_pos):
    global coals
    value = s_pos.copy()
    s_row,s_col = s_pos
    move_cor = [s_row-1,s_col]
    if move_cor[0] >= 0 and move_cor[1] >= 0:
        if move_cor[0] < len(matrix) and move_cor[1] < len(matrix):
            if matrix[move_cor[0]][move_cor[1]] == "*":
                matrix[s_row][s_col] , matrix[move_cor[0]][move_cor[1]] = matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "c":
                coals -=1
                matrix[move_cor[0]][move_cor[1]] = "*"
                matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]] = matrix[move_cor[0]][move_cor[1]],matrix[s_row][s_col]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "e":
                return "game over"
    return value


def right(matrix,s_pos):
    global coals
    value = s_pos.copy()
    s_row,s_col = s_pos
    move_cor = [s_row,s_col+1]
    if move_cor[0] >= 0 and move_cor[1] >= 0:
        if move_cor[0] < len(matrix) and move_cor[1] < len(matrix):
            if matrix[move_cor[0]][move_cor[1]] == "*":
                matrix[s_row][s_col] , matrix[move_cor[0]][move_cor[1]] = matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "c":
                coals -=1
                matrix[move_cor[0]][move_cor[1]] = "*"
                matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]] = matrix[move_cor[0]][move_cor[1]],matrix[s_row][s_col]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "e":
                return "game over"
    return value

def down(matrix,s_pos):
    global coals
    value = s_pos.copy()
    s_row,s_col = s_pos
    move_cor = [s_row+1,s_col]
    if move_cor[0] >= 0 and move_cor[1] >= 0:
        if move_cor[0] < len(matrix) and move_cor[1] < len(matrix):
            if matrix[move_cor[0]][move_cor[1]] == "*":
                matrix[s_row][s_col] , matrix[move_cor[0]][move_cor[1]] = matrix[move_cor[0]][move_cor[1]], matrix[s_row][s_col]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "c":
                coals -=1
                matrix[move_cor[0]][move_cor[1]] = "*"
                matrix[s_row][s_col], matrix[move_cor[0]][move_cor[1]] = matrix[move_cor[0]][move_cor[1]],matrix[s_row][s_col]
                return move_cor
            elif matrix[move_cor[0]][move_cor[1]] == "e":
                return "game over"

    return value

rows = int(input())
matrix = []


commands = input().split()

for row in range(rows):
    matrix.append(input().split())
    for el in matrix[row]:
        if el == "c":
            coals +=1
s_pos = []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "s":
            s_pos = [row,col]
            break
    if s_pos:
        break
flat = True
for command in commands:
    if command == 'left':
        result = left(matrix,s_pos)
        if not result == "game over":
            s_pos.clear()
            s_pos = result.copy()

        else:
            print(f"Game Over! ({s_pos[0]}, {s_pos[1]-1})" )
            flag = False
            break
    elif command == "up":

        result = up(matrix,s_pos)
        if not result  == 'game over':
            s_pos.clear()
            s_pos = result.copy()

        else:
            print(f"Game Over! ({s_pos[0]-1}, {s_pos[1]})")
            flag = False
            break
    elif command == 'down':
        result = down(matrix, s_pos)
        if not result == "game over":
            s_pos.clear()
            s_pos = result.copy()
        else:
            print(f"Game Over! ({s_pos[0]+1}, {s_pos[1]})")
            flag = False
            break
    elif command == "right":
        result = right(matrix, s_pos)
        if not result == "game over":
            s_pos.clear()
            s_pos = result.copy()
        else:
            print(f"Game over! ({s_pos[0]}, {s_pos[1]+1})")
            flag = False
            break
    if coals == 0:
        break
if flag:
    if not coals == 0:
        print(f"{coals} pieces of coal left. ({s_pos[0]}, {s_pos[1]}) ")
    else:
        print(f'You collected all coal! ({s_pos[0]}, {s_pos[1]})')





