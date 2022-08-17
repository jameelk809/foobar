"""
Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of
its prior elements. Note : 1st element of the array should be considered in the count of the result.
"""


arr = [7, 4, 8, 2, 9]
maxx = -1
count = 0
for i in range(len(arr)):
    if arr[i] > maxx:
        maxx = arr[i]
        count += 1
print(count)
