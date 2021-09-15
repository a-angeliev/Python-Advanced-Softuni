rows = int(input())
matrix = []


for row in range(rows):
    matrix.append(input().split())

for row in range(rows):
    for j in range(rows):
        element = matrix[row][j]
        if not element.isalpha():
            matrix[row][j] = int(element)
        else:
            matrix[row][j] = 10000


booms_cor = input().split()
for i in range(len(booms_cor)-1 ,0 , -1):
    currnet_el = booms_cor.pop(i)

    if not currnet_el in booms_cor:
        booms_cor.insert(i,currnet_el)



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



