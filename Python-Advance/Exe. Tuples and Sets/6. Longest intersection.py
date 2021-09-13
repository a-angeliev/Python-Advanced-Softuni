lines = int(input())
tup = set()
all_int =[]
for _ in range(lines):

    inter1, inter2 = input().split("-")
    inter1_a, inter1_b = inter1.split(",")
    inter2_a, inter2_b = inter2.split(",")
    inter1_a, inter1_b = int(inter1_a), int(inter1_b)
    inter2_a, inter2_b = int(inter2_a), int(inter2_b)

    if inter1_a > inter2_a:
        start = inter1_a
    else:
        start = inter2_a

    if inter1_b > inter2_b:
        end = inter2_b
    else:
        end = inter1_b

    for i in range(start-1,end):
        tup.add(i+1)
    all_int.append(tuple(tup))
    tup.clear()

currnet_el = ""
for el in all_int:
    if len(el) > len(currnet_el):
        currnet_el = el
print(f"Longest intersection is {list(currnet_el)} wiht lengh {len(currnet_el)}")