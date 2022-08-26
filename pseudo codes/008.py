def combine(p):
    if p <= 17:
        combine(combine(p*2))
    return p + 3


print(combine(8))
