box = [int(x) for x in input().split()]
rack = int(input())
cloth = 0
currnet_rack = 0
racks = 1
while box:
    if currnet_rack + box[-1] <= rack:
        currnet_rack+=box[-1]
        box.pop()
    else:
        currnet_rack = 0
        racks+=1

print(racks)
