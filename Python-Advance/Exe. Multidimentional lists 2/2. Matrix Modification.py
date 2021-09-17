rows = int(input())
matrix = []

for row in range(rows):
    new_line = [int(x) for x in input().split()]
    matrix.append(new_line)

command = input().split()
while not command[0] == "END":
    if (command[0] == "Add" or command[0] == "Subtract" )and len(command) == 4:
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])
        if 0 <= row < rows and 0<= col < len(matrix[row]):
            if command[0] == "Add":
                matrix[row][col] += value
            else:
                matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input().split()

for row in matrix:
    str_row = [str(x) for x in row]
    print(" ".join(str_row))


    # elif command[0] == "Subtract" and len(command) == 4:
    #     row = int(command[1])
    #     col = int(command[2])
    #     value = int(command[3])
    #     if 0 <= row < rows and 0<= col < len(matrix[row]):
    #         matrix[row][col] += value
    #     else:
    #         print("Invalid coordinates")
