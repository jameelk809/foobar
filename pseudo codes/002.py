def fun(a, b):
    n = 0
    if b < 1:
        return n
    else:
        return fun(a+b+2, b-2)


print(fun(2, 4))