lines = int(input())
list = []
distance = 0
ranges = 0
flag = False
not_match = False
for _ in range(lines):
    command = input().split()
    list.append(int(command[0]))
    list.append(int(command[1]))
cout = 0
while not flag:
    for index in range(0, lines*2, 2):
        distance += list[index+1]
        ranges += list[index]
        if ranges >= distance:
            ranges -= distance
            distance = 0
            flag = True
        else:
            list = list[2:]+list[:2]
            distance = 0
            ranges = 0
            cout+=1
            flag = False
            if cout == lines+1:
                not_match = True
                break
            break
    if not_match:
        break
print(cout)