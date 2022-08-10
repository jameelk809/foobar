"""
You are given an array arr[] of size N.
The array consists of a permutation of the set {1, 2, 3, … , N} for some positive integer N.
You have to start at the position which has 1 in the array and then travel to the position
which has 2. Then from 2, you travel to 3 and so on till you reach the position which has N.
When you travel from Arr[i] to Arr[j], the distance travelled is | i– j |.
Find the total distance you have to travel to reach N when you start from 1.
"""


def distance(arr, n):
    temp = [0]*n
    res = 0
    for i in range(n):
        temp[arr[i]-1] = i
    for i in range(n-1):
        res += abs(temp[i] - temp[i+1])
    return res


N = 5
Arr = [5, 1, 4, 3, 2]
print(distance(Arr, N))
