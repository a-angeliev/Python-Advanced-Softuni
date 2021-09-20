def func_executor(*args):
    list = []
    for el in args:
        function = el[0]
        # num1,num2 = el[1]
        list.append(function(*el[1]))
    return list



# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))