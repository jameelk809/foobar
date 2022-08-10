"""
Given an array of size N and you have to tell whether the array is perfect or not.
An array is said to be perfect if it's reverse array matches the original array.
If the array is perfect then print "PERFECT" else print "NOT PERFECT".
"""


def IsPerfect(arr, n):
    rev = arr[::-1]
    if arr == rev:
        return True
    else:
        return False


Arr = [1, 2, 3, 2, 1]
n = 5
ans = IsPerfect(Arr, n)
