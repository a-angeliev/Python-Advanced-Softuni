food_qty = int(input())
que = input().split()
que = [int(x) for x in que]
print(max(que))

while food_qty > 0 and que:
    if que[0] < food_qty:
        food_qty -= que[0]
        que.pop(0)
    else:
        food_qty-= food_qty

if que:
    que = [str(x) for x in que]
    print(f"Orders left: {' '.join(que)}")
else:
    print("Orders complete")