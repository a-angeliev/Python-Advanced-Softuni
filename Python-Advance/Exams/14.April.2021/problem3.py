def flights(*args):
    dicts = {}
    if "Finish" in args:
        ind = args.index("Finish")
    args = [x for x in args[0:ind]]
    for index in range(0, ind, 2):
        if args[index] not in dicts:
            dicts[args[index]] = args[index+1]
        else:
            dicts[args[index]] += args[index+1]
    return dicts

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
