rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([x for x in input().split()])

command = input().split()
while not command[0] == 'END':
    if command[0] == "swap":
        if command[1] and command[2] and command[3] and command[4]:
            if len(command) == 5:
                command.pop(0)

                command = [int(x) for x in command]
                row1, col1, row2, col2 = command
                if row1<rows and row2<rows and col1<cols and col2<cols:
                    matrix[row1][col1],matrix[row2][col2] = matrix[row2][col2],matrix[row1][col1]
                    for i in range(rows):
                        for j in range(cols):
                            print(matrix[i][j],end = " ")
                        print()
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")

    command = input().split()
