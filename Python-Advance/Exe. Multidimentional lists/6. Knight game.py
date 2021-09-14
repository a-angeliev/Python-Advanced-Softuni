def attack_number(matr,row,col):
    k_moves = [
        [row-1,col-2],
        [row-2,col-1],
        [row-2,col+1],
        [row-1,col+2],
        [row+1,col+2],
        [row+2,col+1],
        [row+2,col-1],
        [row+1,col-2]]
    numbers_of_attack = 0
    for move in k_moves:
        r,c= move[0],move[1]
        if r >= 0 and  c >= 0:
            if r < len(matr) and c < len(matr):
                if matrix[r][c] == 'K':
                    numbers_of_attack+=1

    return int(numbers_of_attack)

rows = int(input())
matrix = []

for row in range(rows):
    current_row = input()
    matrix.append([])
    matrix[row] = [el for el in current_row]

biggest_attacker = None
attacker_pos = []
count = 0
while not biggest_attacker == 0:
    biggest_attacker = 0
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'K':
                current_k = attack_number(matrix,i,j)
                if current_k > biggest_attacker:
                    biggest_attacker = current_k
                    attacker_pos.clear()
                    attacker_pos.append(int(i))
                    attacker_pos.append(int(j))
    if biggest_attacker == 0:
        break
    else:
        r, c = attacker_pos[0],attacker_pos[1]
        matrix[r][c] = 0
        count +=1
        attacker_pos.clear()

print(count)

