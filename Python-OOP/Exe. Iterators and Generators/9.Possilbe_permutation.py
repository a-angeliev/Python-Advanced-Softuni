from itertools import permutations
def possible_permutations(info):
    perm = permutations(info)
    for el in list(perm):
        current_reustl = []
        for el in el:
            current_reustl.append(el)
        yield current_reustl

[print(n) for n in possible_permutations([1, 2, 3])]