rows = int(input())
matrix = []


for row in range(rows):
    matrix.append([int(x) for x in input().split()])

booms_cor =  input().split()

for bomb in booms_cor:
    row, col = bomb.split(",")
    row = int(row)
    col = int(col)
    if matrix[row][col] > 0:
        bomb_power = matrix[row][col]
        matrix[row][col] = "x"
        boom_targets = [
            [row - 1, col - 1],
            [row - 1, col],
            [row - 1, col + 1],
            [row, col - 1],
            [row, col],
            [row, col + 1],
            [row + 1, col - 1],
            [row + 1, col],
            [row + 1, col + 1]]
        for target in boom_targets:
            r,c = target[0],target[1]
            if r >= 0 and c >= 0:
                if r < rows and c < rows:
                    if not matrix[r][c] == "x":
                        if matrix[r][c] > 0:
                            matrix[r][c] -= bomb_power
                            check = f"{r},{c}"

sum = 0
alive = 0
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "x":
            matrix[row][col] = 0
        if matrix[row][col] > 0:
            sum+=matrix[row][col]
            alive+=1

print(f"Alive cells: {alive}")
print(f"Sum: {sum}")
for row in range(rows):
    for col in range(rows):
        print(matrix[row][col], end = " ")
    print()


