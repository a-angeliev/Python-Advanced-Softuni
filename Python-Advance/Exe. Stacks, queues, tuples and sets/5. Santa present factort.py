matirials = [int(x) for x in input().split()]
magic = [int(x) for x in input().split()]
doll  = 0
train = 0
bear = 0
bicycle = 0

magic = magic[::-1]
while True:
    c_mat = matirials[-1]
    c_mag = magic[-1]
    if c_mat == 0 or c_mag == 0:
        if c_mat == 0:
            matirials.pop()
        if c_mag == 0:
            magic.pop()
    elif c_mat* c_mag == 400 or c_mag * c_mat == 150 or c_mag*c_mat==250 or c_mag * c_mat == 300:
        if c_mat * c_mag == 400:
            matirials.pop()
            magic.pop()
            bicycle +=1
        elif c_mat * c_mag == 300:
            matirials.pop()
            magic.pop()
            bear += 1
        elif c_mat * c_mag == 250:
            matirials.pop()
            magic.pop()
            train += 1
        elif c_mat * c_mag == 150:
            matirials.pop()
            magic.pop()
            doll += 1
    elif c_mag * c_mat < 0:
        result = c_mag+c_mat
        matirials.pop()
        magic.pop()
        matirials.append(result)
    elif c_mag *c_mat == 0:
        matirials.pop()
        magic.pop()
    elif c_mag * c_mat > 0:
        magic.pop()
        matirials[-1] +=15

    if not magic or not matirials:
        break

if not doll == 0 and not train == 0:
    print("The presents are crafted! Merry Christmas!")
elif not bear == 0 and not bicycle == 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if matirials:
    matirials = [str(x) for x in matirials[::-1]]
    print(f"Materials left: {', '.join(matirials)}")
if magic:
    magic = [str(x) for x in magic[::-1]]
    print(f"Magic left: {', '.join(magic)}")

if not bicycle == 0:
    print(f"Bicycle: {bicycle}")
if not doll == 0:
    print(f"Doll: {doll}")
if not bear  == 0:
    print(f"Teddy bear: {bear}")
if not train == 0:
    print(f"Wooden train: {train}")
