lines = int(input())
odd_set = set()
even_set = set()
current_ascii = 0
for i in range(lines):
    name = input()
    for el in name:
        current_ascii += ord(el)
    current_ascii = int(current_ascii/ (i+1))
    if current_ascii % 2 == 0:
        odd_set.add(current_ascii)
    else:
        even_set.add(current_ascii)
    current_ascii = 0
even_sum = sum(even_set)
odd_sum = sum(odd_set)
odd_set = set(str(x) for x in odd_set)
even_set = set(str(x) for x in even_set)
if even_sum < odd_sum:
    a = list(odd_set.symmetric_difference(even_set))
    print(", ".join(a))
else:
    b = list(even_set.difference(odd_set))
    print(", ".join(b))

