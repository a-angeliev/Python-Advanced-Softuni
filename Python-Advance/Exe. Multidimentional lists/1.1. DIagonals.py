n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(", ")])

p_sum = 0
p_el = []
s_sum = 0
s_el = []
for i in range(n):
    p_sum += matrix[i][i]
    p_el.append(str(matrix[i][i]))
    s_sum += matrix[i][-i-1]
    s_el.append(str(matrix[i][-i-1]))

print(f"Primary diagonal: {', '.join(p_el)}. Sum: {p_sum}")
print(f"Secondary diagonal: {', '.join(s_el)}. Sum: {s_sum}")



