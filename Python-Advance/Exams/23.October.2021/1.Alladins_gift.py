materials = [int(x) for x in input().split()]
magic = [int(x) for x in input().split()[::-1]]
gemstone = 0
porcelain = 0
gold = 0
jew = 0

while True:
    if materials == [] or magic == []:
        break

    result = magic[-1] + materials[-1]
    if 100<= result <= 199:
        gemstone +=1
        materials.pop()
        magic.pop()
    elif 200 <= result <=299:
        porcelain+=1
        materials.pop()
        magic.pop()
    elif 300<= result <= 399:
        gold += 1
        materials.pop()
        magic.pop()
    elif 400<= result <= 499:
        jew +=1
        materials.pop()
        magic.pop()
    elif result <100:
        if result % 2 == 0:
            result = (magic[-1] *3) +(materials[-1]*2)
            if 100 <= result <= 199:
                gemstone += 1
                materials.pop()
                magic.pop()
            elif 200 <= result <= 299:
                porcelain += 1
                materials.pop()
                magic.pop()
            elif 300 <= result <= 399:
                gold += 1
                materials.pop()
                magic.pop()
            elif 400 <= result <= 499:
                jew += 1
                materials.pop()
                magic.pop()
            else:
                materials.pop()
                magic.pop()
        else:
            result = result * 2
            if 100 <= result <= 199:
                gemstone += 1
                materials.pop()
                magic.pop()
            elif 200 <= result <= 299:
                porcelain += 1
                materials.pop()
                magic.pop()
            elif 300 <= result <= 399:
                gold += 1
                materials.pop()
                magic.pop()
            elif 400 <= result <= 499:
                jew += 1
                materials.pop()
                magic.pop()
            else:
                materials.pop()
                magic.pop()
    elif result > 499:
        result = result/2
        if 100 <= result <= 199:
            gemstone += 1
            materials.pop()
            magic.pop()
        elif 200 <= result <= 299:
            porcelain += 1
            materials.pop()
            magic.pop()
        elif 300 <= result <= 399:
            gold += 1
            materials.pop()
            magic.pop()
        elif 400 <= result <= 499:
            jew += 1
            materials.pop()
            magic.pop()
        else:
            materials.pop()
            magic.pop()
    else:
        materials.pop()
        magic.pop()

if gemstone != 0 and porcelain != 0:
    print("The wedding presents are made!")
elif gold != 0 and jew != 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic[::-1]))}")
if jew != 0:
    print(f"Diamond Jewellery: {jew}")
if gemstone != 0:
    print(f"Gemstone: {gemstone}")
if gold != 0:
    print(f"Gold: {gold}")
if porcelain != 0:
    print(f"Porcelain Sculpture: {porcelain}")