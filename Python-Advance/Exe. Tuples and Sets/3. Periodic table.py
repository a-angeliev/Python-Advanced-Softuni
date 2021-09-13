lines = int(input())
elements = set()
current_elements = []
for _ in range(lines):
    current_elements = input().split()
    for el in current_elements:
        elements.add(el)
    current_elements.clear()

for el in elements:
    print(el)
