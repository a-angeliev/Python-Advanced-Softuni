def fill_the_box(a,b,c,*args):
    cube_size = a*b*c
    sum = 0
    for el in args:
        if el == "Finish":
            break
        if el < cube_size:
            cube_size -=el
        else:
            if not cube_size == 0:
                sum = el - cube_size
                cube_size = 0
            else:
                sum +=el
    if not cube_size == 0:
        return f"There is free space in the box. You could put {cube_size} more cubes."
    else:
        return f"No more free space! You have {sum} more cubes."
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))