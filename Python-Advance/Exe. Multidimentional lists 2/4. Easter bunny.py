import sys

rows = int(input())
matrix = []
bunny_start = []
for row in range(rows):
    current_row = input().split()
    matrix.append([])
    for i in range(len(current_row)):
        if current_row[i] == "B":
            bunny_start.append(row)
            bunny_start.append(i)
        if current_row[i].lstrip("-").isdigit():
            matrix[row].append(int(current_row[i]))
        else:
            matrix[row].append(current_row[i])

sum_up = 0
sum_down = 0
sum_right = 0
sum_left = 0

for i in range(bunny_start[0]-1, -1, -1):
    if matrix[i][bunny_start[1]] == "B":
        break
    elif matrix[i][bunny_start[1]] == "X":
        break
    # elif matrix[i][bunny_start[1]] < 0:
    #     sum_up += matrix[i][bunny_start[1]]
    elif str(matrix[i][bunny_start[1]]).lstrip("-").isdigit():
        sum_up += matrix[i][bunny_start[1]]


for i in range(bunny_start[0]+1,rows):
    if matrix[i][bunny_start[1]] == "B":
        break
    elif matrix[i][bunny_start[1]] == "X":
        break
    # elif matrix[i][bunny_start[1]] < 0:
    #     sum_down += matrix[i][bunny_start[1]]
    elif str(matrix[i][bunny_start[1]]).lstrip("-").isdigit():
        sum_down += matrix[i][bunny_start[1]]

for i in range(bunny_start[1]-1, -1 , -1):
    if matrix[bunny_start[0]][i] == "B":
        break
    elif matrix[bunny_start[0]][i] == "X":
        break
    # elif matrix[bunny_start[0]][i] < 0:
    #     sum_left += matrix[bunny_start[0]][i]
    elif str(matrix[bunny_start[0]][i]).lstrip("-").isdigit():
        sum_left += matrix[bunny_start[0]][i]

for i in range(bunny_start[1]+1, rows):
    if matrix[bunny_start[0]][i] == "B":
        break
    elif matrix[bunny_start[0]][i] == "X":
        break
    # elif matrix[bunny_start[0]][i] < 0:
    #     sum_right += matrix[bunny_start[0]][i]
    elif str(matrix[bunny_start[0]][i]).lstrip("-").isdigit():
        sum_right += matrix[bunny_start[0]][i]


direction = ""
final_sum = -sys.maxsize

if final_sum <= sum_up:
    final_sum = sum_up
    direction = 'Up'
if final_sum <= sum_down:
    final_sum = sum_down
    direction = "Down"
if final_sum <= sum_left:
    final_sum = sum_left
    direction = "Left"
if final_sum <= sum_right:
    final_sum = sum_right
    direction = "Right"

if direction == "Up":
    print("up")
    for i in range(bunny_start[0] - 1, -1, -1):
        if matrix[i][bunny_start[1]] == "B":
            break
        elif matrix[i][bunny_start[1]] == "X":
            break
        else:
            print(f"[{i}, {bunny_start[1]}]")
elif direction == "Down":
    print("down")
    for i in range(bunny_start[0] + 1, rows):
        if matrix[i][bunny_start[1]] == "B":
            break
        elif matrix[i][bunny_start[1]] == "X":
            break
        else:
            print(f"[{i}, {bunny_start[1]}]")
elif direction == "Left":
    print("left")
    for i in range(bunny_start[1] - 1, -1, -1):
        if matrix[bunny_start[0]][i] == "B":
            break
        elif matrix[bunny_start[0]][i] == "X":
            break
        else:
            print(f"[{bunny_start[0]}, {i}]")
elif direction == "Right":
    print("right")
    for i in range(bunny_start[1] + 1, len(matrix[bunny_start[0]])):
        if matrix[bunny_start[0]][i] == "B":
            break
        elif matrix[bunny_start[0]][i] == "X":
            break
        else:
            print(f"[{bunny_start[0]}, {i}]")

print(final_sum)







#
# for row in range(rows):
#     for col in range(rows):
#         print(matrix[row][col], end = " ")
#     print()


