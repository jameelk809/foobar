# day 7

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)


N = 10
print(2*factorial(N-1))
