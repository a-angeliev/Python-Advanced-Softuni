orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]
orders = orders[::-1]
pizza_count = 0
while True:
    if orders == []:
        print(f'All orders are successfully completed!')
        print(f'Total pizzas made: {pizza_count}')
        emplo = map(lambda x: str(x), employees)
        print(f'Employees: {", ".join(emplo)}')
        break
    if employees == []:
        ord = map(lambda x: str(x), orders)
        print(f"Not all orders are completed.")
        print(f"Orders left: {', '.join(ord)}")
        break

    while not 0 < orders[-1] <= 10:
        if not 0 < orders[-1] <= 10:
            orders.pop()
            if orders == []:
                print(f'All orders are successfully completed!')
                print(f'Total pizzas made: {pizza_count}')
                emplo = map(lambda x: str(x), employees)
                print(f'Employees: {", ".join(emplo)}')
                exit(0)

    current_order = orders[-1]
    current_employee = employees[-1]
    if 0 < current_order < 11:
        if current_employee - current_order >= 0:
            pizza_count += current_order
            orders.pop()
            employees.pop()
        else:
            pizza_count += current_employee
            orders[-1] -= current_employee
            employees.pop()








