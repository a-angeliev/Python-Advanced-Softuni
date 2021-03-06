stack = []
lines = int(input())

for _ in range(lines):
    command = input().split()
    if command[0] == '1':
        if command[1]:
            stack.append(int(command[1]))
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))

for index in range(len(stack)):
    stack[index] = str(stack[index])

print(', '.join(stack[::-1]))