chocolets = [int(x) for x in input().split(", ")]
milks = [int(x) for x in input().split(", ")]

shakes = 0
milks = milks[::-1]

while not shakes == 5:
    milk = milks[-1]
    chocolet = chocolets[-1]
    if milk <= 0 or chocolet <= 0:
        if milk <= 0:
            milks.pop()
        if chocolet <= 0:
            chocolets.pop()
    elif milk == chocolet:
        shakes += 1
        milks.pop()
        chocolets.pop()
    else:
        milk = milks.pop()
        milks.insert(0, milk)
        chocolets[-1] -= 5

    if not chocolets or not milks:
        break
if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolets:
    chocolets = [str(x) for x in chocolets]
    print(f'Chocolate: {", ".join(chocolets)}')
else:
    print("Chocolate: empty")
if milks:
    milks = [str(x) for x in milks[::-1]]
    print(f"Milk: {', '.join(milks)}")
else:
    print("Milk: empty")
