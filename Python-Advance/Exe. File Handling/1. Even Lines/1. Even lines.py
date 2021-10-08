symb = {"-", ",", ".", "!", "?"}

with open('text.txt', 'r') as file:
    index = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        if not index % 2 == 0:
            index += 1
            continue
        for symbol in symb:
            line = line.replace(symbol, "@")
        line = " ".join(line.split()[::-1])
        print(line)
        index += 1