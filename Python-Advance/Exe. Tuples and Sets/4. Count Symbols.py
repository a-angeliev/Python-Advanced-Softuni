text = input()
elements = {}
for el in text:
    if not el in elements:
        elements[el] = 1
    else:
        elements[el] +=1

for key,value in sorted(elements.items(), key = lambda kvp: kvp[0]):
    print(f"{key}: {value} time/s")