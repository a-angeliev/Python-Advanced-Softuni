rows, cols = input().split()
rows, cols  = int(rows), int(cols)

matrix = []
equal = 0
for row in range(rows):
    matrix.append(input().split())

for i in range(rows-1):
    for j in range(cols-1):
        el = matrix[i][j]
        if matrix[i+1][j] == el and matrix[i+1][j+1] == el and matrix[i][j+1] == el:
            equal+=1
print(equal)
