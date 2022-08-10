"""
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray.
Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.
"""


def PalinArray(arr ,n):
    for item in arr:
        if str(item) != str(item)[::-1]:
            return 0
    return 1


A = [111, 222, 343, 88, 121]
n = 5
if PalinArray(A, n):
    print(1)
else:
    print(0)
