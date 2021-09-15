# [a-z] == 97 - 122
# [A-Z] = 65 - 90

rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(f"{chr(row + 97)}{chr(col + row + 97)}{chr(row + 97)}")

for row in range(rows):
    for col in range(cols):
        print(matrix[row][col], end = " ")
    print()

