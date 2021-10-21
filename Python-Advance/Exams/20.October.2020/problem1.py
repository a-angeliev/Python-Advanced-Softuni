import sys

numbers = [int(x) for x in input().split(", ")]
choosen_index= int(input())
current_number = []
cycle = 0

while True:
    a = sys.maxsize
    ind = -sys.maxsize
    for index in range(len(numbers)):
        if str(numbers[index]).isdigit():
            if numbers[index] < a:
                a = numbers[index]
                ind = index

    numbers[ind] = "x"
    cycle += a
    if choosen_index == ind:
        break
print(cycle)
