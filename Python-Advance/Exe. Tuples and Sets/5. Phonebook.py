
command = input()
phonebook = {}
while not command.isdigit():
    name, number = command.split("-")
    phonebook[name] = number
    command = input()
for _ in range(int(command)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
