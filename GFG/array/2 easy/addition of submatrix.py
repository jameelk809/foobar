"""
Given a matrix Arr of size N x M. You are given position of submatrix as
X1, Y1 and X2, Y2 inside the matrix. Find the sum of all elements inside
that submatrix. Here X1, Y1, X2, Y2 are 1-based.
"""


def subMatrixSum(arr, n, m, x1, y1, x2, y2):
    s = 0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            s += arr[i][j]
    return s


Arr = [
    [9, 8, 7],
    [4, 2, 1],
    [6, 5, 3]
]
N = 3
M = 3
# Arr = [
#     [ 1,  2,  3,  4,  5,  6],
#     [ 7,  8,  9, 10, 11, 12],
#     [13, 14, 15, 16, 17, 18],
#     [19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30]
# ]

# X1 = 3
# Y1 = 4
# X2 = 4
# Y2 = 5

X1 = 1
Y1 = 2
X2 = 3
Y2 = 3

print(subMatrixSum(Arr, N, M, X1, Y1, X2, Y2))
