matrix = []
for _ in range(5):
    matrix.append(input().split())
targets = 0
man_coor = []
for row in range(5):
    for col in range(5):
        if matrix[row][col] == "x":
            targets += 1
        elif matrix[row][col] == "A":
            man_coor.append(row)
            man_coor.append(col)
            break




command_number = int(input())
move_coor = []
shooted_targets = []

for i in range(command_number):

    command = input().split()
    if command[0] == "move":
        direction,steps = command[1], int(command[2])
        if steps < 0:
            steps = 0
        # if steps < 0:
        #     steps = -steps
        #     if direction == "up":
        #         direction = "down"
        #     elif direction == "down":
        #         direction = 'up'
        #     elif direction == "right":
        #         direction = "left"
        #     elif direction == "left":
        #         direction = "right"
        for i in range(steps):
            dict_move = {"up": [man_coor[0] - 1, man_coor[1]],
                         "down": [man_coor[0] + 1, man_coor[1]],
                         "left": [man_coor[0], man_coor[1] - 1],
                         "right": [man_coor[0], man_coor[1] + 1]}
            move_coor.clear()
            move_coor.append(dict_move[direction][0])
            move_coor.append(dict_move[direction][1])
            if 0 <= move_coor[0] < 5 and 0 <= move_coor[1] < 5:
                if matrix[move_coor[0]][move_coor[1]] == ".":
                    matrix[move_coor[0]][move_coor[1]] = "A"
                    matrix[man_coor[0]][man_coor[1]] = "."
                    man_coor.clear()
                    man_coor.append(move_coor[0])
                    man_coor.append(move_coor[1])
                else:
                    break
            else:
                break

    elif command[0] == "shoot":
        direction = command[1]
        if direction == "up":
            for i in range(man_coor[0]-1, -1,-1):
                if matrix[i][man_coor[1]] == "x":
                    matrix[i][man_coor[1]] = "."
                    shooted_targets.append([i, man_coor[1]])
                    targets -= 1
                    break
        elif direction == "down":
            for i in range(man_coor[0]+1,5):
                if matrix[i][man_coor[1]] == "x":
                    matrix[i][man_coor[1]] = "."
                    shooted_targets.append([i, man_coor[1]])
                    targets -= 1
                    break
        elif direction == "left":
            for i in range(man_coor[1] - 1, -1, -1):
                if matrix[man_coor[0]][i] == "x":
                    matrix[man_coor[0]][i] = "."
                    shooted_targets.append([man_coor[0],i])
                    targets -= 1
                    break
        elif direction == "right":
            for i in range(man_coor[1]+1, 5):
                if matrix[man_coor[0]][i] == "x":
                    matrix[man_coor[0]][i] = "."
                    shooted_targets.append([man_coor[0], i])
                    targets -= 1
                    break
    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {len(shooted_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

for el in shooted_targets:
    print(el)




