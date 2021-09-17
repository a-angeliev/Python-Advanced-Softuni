flatten_list = input().split("|")
new_list = []
for el in flatten_list[::-1]:
    cur = el.split()
    for i in cur:
        if not el == "":
            new_list.append(i)


print(" ".join(new_list))