def sum(n):
    if n != 0:
        return n + n * sum(n-1)
    else:
        return n


print(sum(4))
