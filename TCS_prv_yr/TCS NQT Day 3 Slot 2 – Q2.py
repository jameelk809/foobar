"""An international round table conference will be held in india. Presidents from all over the world representing
their respective countries will be attending the conference. The task is to find the possible number of ways(P) to
make the N members sit around the circular table such that. The president and prime minister of India will always sit
next to each other. """


def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)


N = 10
print(2*factorial(N-1))
