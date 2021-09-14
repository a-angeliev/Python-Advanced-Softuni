import sys

rows, cols = input().split()
rows, cols =int(rows), int(cols)

matrix = []
start = []
cur_sum = -sys.maxsize
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows-2):
    for col in range(cols - 2):
        sums = sum([matrix[row][col],matrix[row][col+1],matrix[row][col+2],
                    matrix[row+1][col],matrix[row+1][col+1],matrix[row+1][col+2],
                    matrix[row+2][col],matrix[row+2][col+1],matrix[row+2][col+2]])
        if sums > cur_sum:
            cur_sum = sums
            start.clear()
            start.append([row,col])
print(f"Sum = {cur_sum}")
row,col = start[0]
print(matrix[row][col],matrix[row][col+1],matrix[row][col+2])
print(matrix[row+1][col],matrix[row+1][col+1],matrix[row+1][col+2])
print(matrix[row+2][col],matrix[row+2][col+1],matrix[row+2][col+2])
