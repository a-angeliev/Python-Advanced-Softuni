n,m = input().split()
n,m = int(n), int(m)
set1 = set()
set2 = set()
for _ in range(n):
    set1.add(int(input()))

for _ in range(m):
    set2.add(int(input()))

for el in (set1 & set2):
    print(el)