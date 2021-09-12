str_stack = input()
stack = [x for x in str_stack]
new_stack = []
is_no = False
for el in stack:
    if el == '(' or el == '{' or el == "[":
        new_stack.append(el)
    else:
        if new_stack:
            if el == ")":
                if new_stack[-1] == '(':
                   new_stack.pop()
                else:
                    is_no = True
                    break
            elif el == "}":
                if new_stack[-1] == "{":
                    new_stack.pop()
                else:
                    is_no = True
                    break
            elif el == "]":
                if new_stack[-1] == "[":
                    new_stack.pop()
                else:
                    is_no = True
                    break
            else:
                is_no = True
                break
        else:
            is_no = True
            break

if is_no:
    print("NO")
else:
    print("YES")