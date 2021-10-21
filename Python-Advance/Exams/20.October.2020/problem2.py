matrix = []

for row in range(8):
    matrix.append(input().split())

queens_coor = []
queens = []
for row in range(8):
    for col in range(8):
        if matrix[row][col] == "Q":
            queens_coor.append([row,col])


def move_up(row, col):
    while row >= 0:
        row -= 1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False


def move_down(row, col):
    while row < 7:
        row += 1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False


def move_left(row, col):
    while col >= 0:
        col -= 1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False

def move_right(a, b):
    while b < 7:
        b += 1
        if matrix[a][b] == "K":
            return True
        elif matrix[a][b] == "Q":
            return False
    return False


def move_up_left(row, col):
    while row >=0 and col >= 0:
        row -=1
        col -=1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False


def move_up_right(row, col):
    while row >= 0 and col <7:
        row -= 1
        col += 1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False

def move_down_left(row, col):
    while row < 7 and col >= 0:
        row +=1
        col -=1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False


def move_down_right(row, col):
    while row <7 and col <7:
        row += 1
        col += 1
        if matrix[row][col] == "K":
            return True
        elif matrix[row][col] == "Q":
            return False
    return False

def is_catched_king(ro, co):
    if move_up(ro, co):
        return True
    elif move_down(ro,co):
        return True
    elif move_left(ro, co):
        return True
    elif move_right(ro, co):
        return True
    elif move_up_left(ro,co):
        return True
    elif move_up_right(ro, co):
        return True
    elif move_down_left(ro,co):
        return True
    elif move_down_right(ro, co):
        return True
    return False

for quen in queens_coor:
    if is_catched_king(quen[0], quen[1]):
        queens.append([quen[0],quen[1]])
if queens:
    for el in queens:
        print(el)
else:
    print("The king is safe!")