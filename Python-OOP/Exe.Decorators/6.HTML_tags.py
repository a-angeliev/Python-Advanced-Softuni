def tags(n):
    def decorator(func):
        def wrapper(*args):
            return f"<{n}>{func(*args)}</{n}>"
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
