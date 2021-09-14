n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

p_sum = 0
s_sum = 0
for i in range(n):
    p_sum += matrix[i][i]
    s_sum += matrix[i][-i-1]
abs_sum = p_sum-s_sum
if abs_sum < 0:
    print(-abs_sum)
else:
    print(abs_sum)