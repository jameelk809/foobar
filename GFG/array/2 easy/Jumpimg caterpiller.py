"""
Given N leaves numbered from 1 to N . A caterpillar at leaf 1, jumps from leaf to leaf in multiples of Aj (Aj, 2Aj, 3Aj).
j is specific to the caterpillar. Whenever a caterpillar reaches a leaf, it eats it a little.
You have to find out how many leaves, from 1 to N, are left uneaten after all K caterpillars have
reached the end. Each caterpillar has its own jump factor denoted by Aj, and each caterpillar starts at leaf number 1.
"""


def uneatenLeaves(arr, n, k):
    f = 0
    for i in range(1, n + 1):
        for j in range(k):
            if i % arr[j] == 0:
                f += 1
                break
    return n - f


N = 10
K = 3
Arr = [2, 3, 5]
print(uneatenLeaves(Arr, N, K))
