line = input().split()
result = []
current_num = []

for el in line:
    res = 0
    if el.isdigit():
        current_num.append(int(el))
    elif el == "*":
        res = current_num[0]
        for els in range(1,len(current_num)):
            res = res * current_num[els]
        current_num.clear()
        current_num.append(res)
    elif el == "/":
        res = current_num[0]
        for els in range(1,len(current_num)):
            res = res / current_num[els]
        res = res // 1
        current_num.clear()
        current_num.append(res)
    elif el == "+":
        res = current_num[0]
        for els in range(1,len(current_num)):
            res = res + current_num[els]
        current_num.clear()
        current_num.append(res)
    elif el == "-":
        res = current_num[0]
        for els in range(1,len(current_num)):
            res = res - current_num[els]
        current_num.clear()
        current_num.append(res)
    else:
        current_num.append(int(el))

print(int(current_num[0]))
