def D_to_B(n):
    x = bin(n)
    x = x.replace("0b", "")
    return x


print(D_to_B(4))
