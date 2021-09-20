def even_odd(*args):
    command = args[-1]
    args = args[:-1]
    if command == "even":
        new_nums = [x for x in args if x % 2 == 0]
    elif command == "odd":
        new_nums = [x for x in args if not x % 2 ==0]
    else:
        new_nums = []
    return new_nums

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
