colors = ['red', 'blue','yellow','orange','purple','green']
string = [x for x in input().split()]

finded_colors = []

while string:
    if len(string) > 1:
        left_str = string[0]
        right_str = string[-1]
        if left_str+right_str in colors:
            finded_colors.append(left_str+right_str)
            string.pop()
            string.pop(0)
        elif right_str+left_str in colors:
            finded_colors.append(right_str+left_str)
            string.pop()
            string.pop(0)
        else:
            left_str = left_str[:-1]
            right_str = right_str[:-1]
            string.pop()
            string.pop(0)
            leng = len(string)
            if leng /2 == 0:
                index = int(leng /2)
            else:
                index = int(leng//2)
            if not len(string) == 1:
            #     if not right_str == "":
            #         string.insert(index, right_str)
            #     if not left_str == "":
            #         string.insert(index-1, left_str)
            # else:
            #     if not right_str == "":
            #         string.insert(0,right_str)
            #     if not left_str == "":
            #         string.insert(0,left_str)
                if not left_str == "":
                    string.insert(index, left_str)
                    if not right_str == "":
                        string.insert(index+1,right_str )
                else:
                    if not right_str == "":
                        string.insert(index, right_str)
            else:
                if not right_str == "":
                    string.insert(0,right_str)
                if not left_str == "":
                    string.insert(0,left_str)
    else:
        st = string[0]
        if st in colors:
            finded_colors.append(st)
        string.pop()
        break

for el in finded_colors:
    if el == "orange":
        if not "red" in finded_colors or not "yellow" in finded_colors:
            finded_colors.remove(el)
    elif el == "purple":
        if not "red" in finded_colors or not "blue" in finded_colors:
            finded_colors.remove(el)
    elif el == "green":
        if not "blue" in finded_colors or not "yellow" in finded_colors:
            finded_colors.remove(el)
print(finded_colors)
