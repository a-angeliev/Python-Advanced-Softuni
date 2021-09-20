def sum_numbers(command, *args):
    sums = 0
    if command == "Odd":
        numbers = [int(x) for x in args[0] if not int(x) % 2 == 0]
        sums = sum(numbers) * len(args[0])
    elif command == "Even":
        numbers = [int(x) for x in args[0] if int(x) % 2 == 0]
        sums = sum(numbers) * len(args[0])

    print(sums)

command = input()
sum_numbers(command, input().split())