green = int(input())
free_win = int(input())
command = input()
que = []
car = 0
succsses_car = 0
is_crashed = False
free_car = 0
while not command == "END":
    if not command =="green":
        que.append(command)
    else:
        for i in range(green):
            if que and car==0:
                current_car = que.pop(0)
                succsses_car +=1
                car = len(current_car)
            car -=1
            if car < 0:
                car = 0
            if i == green - 1:
                if not car == 0:
                    free_car = car
        if free_car > free_win:
            a = free_car - free_win
            ind = len(current_car) - a
            hitted_car = current_car[ind:ind+1]
            print("A crash happened!")
            print(f"{current_car} was hit at {hitted_car}.")
            is_crashed = True


    if is_crashed:
        break
    command = input()
if not is_crashed:
    print("Everyone is safe.")
    print(f"{succsses_car} total cars passed the crossroads.")