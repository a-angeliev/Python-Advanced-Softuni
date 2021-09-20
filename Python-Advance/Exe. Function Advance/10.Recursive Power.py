def recursive_power(num1, num2):
    if num2 == 0:
        return 1
    return num1 * recursive_power(num1,num2-1)

print(recursive_power(2, 10))