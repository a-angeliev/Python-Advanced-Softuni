rows,cols  = [int(x) for x in input().split()]
string = input()

text = []
current_text = []
matrix = []
flag = True

for el in string:
    text.append(el)

current_text = text.copy()

row = -1
col = 0

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(0)

for i in range(rows*cols):
    if col == cols :
        flag = False
        row += 1
    elif col == 0:
        flag = True
        row += 1

    if not current_text:
        current_text = text.copy()

    if flag:
        matrix[row][col] = current_text.pop(0)
        col += 1
    else:
        col -= 1
        matrix[row][col] = current_text.pop(0)


for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end = " ")
    print()