cups = input().split()
bottles = input().split()
cups = [int(x) for x in cups]
bottles = [int(x) for x in bottles]
wasted = 0
currnet_cup = cups[0]
while cups:
    current_bot = bottles.pop()

    if currnet_cup <= current_bot:
        wasted += current_bot-currnet_cup
        cups.pop(0)
        if cups:
            currnet_cup = cups[0]
    else:
        currnet_cup = currnet_cup-current_bot
    if not bottles:
        break
cups = [str(x) for x in cups]
bottles = [str(x) for x in bottles]
if bottles:
    print(f"Bottles: {' '.join(bottles[::-1])} ")
    print(f"Wasted litters of water: {wasted}")
else:
    print(f"Cups: {' '.join(cups)}")
    print(f"Wasted litters of water: {wasted}")

