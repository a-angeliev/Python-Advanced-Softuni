def get_primes(list):
    for el in list:
        if el > 1:
            if el == 2 or el == 3 or el == 5 or el ==7:
                yield el
            elif el % 2 != 0 and el % 3 != 0 and el % 5 != 0 and el % 7 != 0:
                yield el

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))