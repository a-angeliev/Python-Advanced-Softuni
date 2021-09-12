bullet_price = int(input())
gun_barrel = int(input())
bullets = input().split()
number_of_bullets = len(bullets)
locks = input().split()
bullets = [int(x) for x in bullets]
locks = [int(x) for x in locks]
intelligence = int(input())
reload = gun_barrel
while bullets:
    curren_bullet = bullets.pop()
    reload -= 1
    if curren_bullet<= locks[0]:
        print("Bang!")
        locks.pop(0)
    else:
        print("Ping!")
    if reload == 0:
        if bullets:
            reload = gun_barrel
            print("Reloading!")

    if not locks:
        break
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullets_cost = (number_of_bullets-(len(bullets))) * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${intelligence-bullets_cost}")
