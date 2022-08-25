def mul(a, b):
    t = 0
    while b != 0:
        t += a
        b -= 1
    return t


a = 56
b = 876
print(mul(a, b))
