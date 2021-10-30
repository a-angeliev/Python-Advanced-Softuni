matrix = []
for row in range(6):
    matrix.append(input().split())

hitted_b = []
result = 0
throws = []

for _ in range(3):
    throws.append([int(x) for x in input().lstrip("(").rstrip(")").split(", ")])
# throw_1 = [int(x) for x in input().lstrip("(").rstrip(")").split(", ")]
# throw_2 = [int(x) for x in input().lstrip("(").rstrip(")").split(", ")]
# throw_3 = [int(x) for x in input().lstrip("(").rstrip(")").split(", ")]

for throw in throws:
    if 0 <= throw[0] < 6 and 0<= throw[1] < 6:
        if matrix[throw[0]][throw[1]] == "B":
            if not [throw[0], throw[1]] in hitted_b:
                hitted_b.append([throw[0],throw[1]])
                for row in range(6):
                    if matrix[row][throw[1]].isdigit():
                        result += int(matrix[row][throw[1]])

if result <= 99 :
    print(f"Sorry! You need {100 - result} points more to win a prize.")
else:
    if result <= 199:
        print(f"Good job! You scored {result} points, and you've won Football.")
    elif result <= 299:
        print(f"Good job! You scored {result} points, and you've won Teddy Bear.")
    else:
        print(f"Good job! You scored {result} points, and you've won Lego Construction Set.")