bees = [int(x) for x in input().split()]
nectar = [int(x) for x in input().split()]
sym = input().split()
result = 0
bees = bees[::-1]
if bees and nectar:
    while True:
        current_bee = bees[-1]
        current_nectar = nectar[-1]
        if str(current_bee).isdigit() and str(current_nectar).isdigit():
            if current_nectar >= current_bee and sym:
                current_sym = sym.pop(0)
                if current_sym == "*":
                    current_result = current_bee * current_nectar
                    bees.pop()
                    nectar.pop()
                    if current_result >= 0:
                        result += current_result
                    else:
                        result += -current_result
                elif current_sym == "/":
                    if not current_nectar == 0:
                        current_result = current_bee / current_nectar
                        bees.pop()
                        nectar.pop()
                        if current_result >= 0:
                            result += current_result
                        else:
                            result += -current_result
                    else:
                        bees.pop()
                        nectar.pop()
                elif current_sym == "-":
                    current_result = current_bee - current_nectar
                    bees.pop()
                    nectar.pop()
                    if current_result >= 0:
                        result += current_result
                    else:
                        result += -current_result
                elif current_sym == "+":
                    current_result = current_bee + current_nectar
                    bees.pop()
                    nectar.pop()
                    if current_result >= 0:
                        result += current_result
                    else:
                        result += -current_result
            else:
                nectar.pop()

            if not bees or not nectar:
                break
print(f"Total honey made: {result}")
if bees:
    bees = [str(x) for x in bees[::-1]]
    print(f"Bees left: {', '.join(bees)}")
if nectar:
    nectar = [str(x) for x in nectar]
    print(f"Nectar left: {', '.join(nectar)}")