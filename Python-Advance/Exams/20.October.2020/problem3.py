import sys


def best_list_pureness(list: list, number):
    pureness_count = 0
    best_pureness = -sys.maxsize
    for rotate in range(number+1):
        result = 0
        for index in range(len(list)):
            result += list[index] * index
        if best_pureness < result:
            best_pureness = result
            pureness_count = rotate
        last_el = list.pop()
        list.insert(0, last_el)

    return f"Best pureness {best_pureness} after {pureness_count} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)



