first_numbers = []
second_numbers = []
current_first = input().split()
current_second = input().split()

for el in current_first:
    if not int(el) in first_numbers:
        first_numbers.append(int(el))

for el in current_second:
    if not int(el) in second_numbers:
        second_numbers.append(int(el))


lines = int(input())


for i in range(lines):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for i in range(2, len(command)):
                if command[i].isdigit():
                    if not int(command[i]) in first_numbers:
                        first_numbers.append(int(command[i]))
        elif command[1] == "Second":
            for i in range(2, len(command)):
                if command[i].isdigit():
                    if not int(command[i]) in second_numbers:
                        second_numbers.append(int(command[i]))
    elif command[0] == "Remove":
        if command[1] == "First":
            for i in range(2, len(command)):
                if command[i].isdigit():
                    if int(command[i]) in first_numbers:
                        first_numbers.remove(int(command[i]))
        elif command[1] == "Second":
            for i in range(2, len(command)):
                if command[i].isdigit():
                    if int(command[i]) in second_numbers:
                        second_numbers.remove(int(command[i]))
    elif command[0] == "Check" and command[1] == "Subset":
        tup_a = set(first_numbers)
        tup_b = set(second_numbers)
        if tup_a.issubset(tup_b):
            print("True")
        elif tup_b.issubset(tup_a):
            print("True")
        else:
            print("False")

first_numbers = sorted(first_numbers)
second_numbers = sorted(second_numbers)
first_numbers = [str(x) for x in first_numbers]
second_numbers = [str(x) for x in second_numbers]
print(", ".join(first_numbers))
print(", ".join(second_numbers))