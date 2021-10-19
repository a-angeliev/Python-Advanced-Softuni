males = [int(male) for male in input().split()]
females = [int(fe) for fe in input().split()[::-1]]
matches = 0
end_flag = False
while True:
    if males == [] or females == []:
        end_flag = True
        break

    while males[-1] <= 0:
        males.pop()
        if males == []:
            end_flag = True
            break

    while females[-1] <= 0:
        females.pop()
        if females == []:
            end_flag = True
            break

    if end_flag:
        break

    while males[-1] % 25 == 0:
        males.pop()
        if not males == []:
            males.pop()
            if males == []:
                end_flag = True
                break
        else:
            end_flag = True
            break

    while females[-1] % 25 == 0:
        females.pop()
        if not females == []:
            females.pop()
            if females == []:
                end_flag = True
                break
        else:
            end_flag = True
            break

    if end_flag:
        break

    if females[-1] == males[-1]:
        matches += 1
        females.pop()
        males.pop()
    else:
        females.pop()
        males[-1] -= 2

print(f"Matches: {matches}")
if males == []:
    print("Males left: none")
else:
    males = map(str, males[::-1])
    print(f"Males left: {', '.join(males)}")

if females == []:
    print("Females left: none")
else:
    females = map(str, females[::-1])
    print(f"Females left: {', '.join(females)}")

