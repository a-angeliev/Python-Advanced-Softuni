names = []
for _ in range(int(input())):
    names.append(input())

for name in set(names):
    print(name)