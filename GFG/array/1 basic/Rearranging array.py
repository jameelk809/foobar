"""
Given a list of integers, rearrange the list such that it consists of alternating
minimum-maximum elements using only list operations. The first element of the list
should be the minimum of all elements and the second element should be a maximum
of all elements present in the list. Similarly, the third element will be the next
minimum element and the fourth element is the next maximum element, and so on.
Use of extra space is not permitted. Store the answer in the answer[] array.
You don't need to print that.
"""


def Rearrange(a, n, answer):
    # a.sort()
    # st = 0
    # en = n - 1
    # flag = True
    # for i in range(n):
    #     if flag is True:
    #         answer[i] = a[st]
    #         st += 1
    #     else:
    #         answer[i] = a[en]
    #         en -= 1
    #     flag = bool(1 - flag)
    # for i in range(n):
    #     a[i] = answer[i]
    a.sort()
    i = j = 0
    while j < n-1:
        answer[j], answer[j+1] = a[i], a[n-i-1]
        i += 1
        j += 2
    if n % 2 != 0:
        answer[j] = a[i]


N = 6
A = [5, 7, 3, 1, 8, 0]
answer = [0] * N
Rearrange(A, N, answer)
print(answer)
