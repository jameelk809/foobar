"""
Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number: When a number(should contain 3 digits or more) is multiplied
by 2 and 3 ,and when both these products are concatenated with the original number,
then it results in all digits from 1 to 9 present exactly once.
"""


def fascinating(n):
    if len(str(n)) > 2:
        flag = False
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = str(n) + str(n*2) + str(n*3)
        temp = []
        for digit in res:
            if digit not in temp and digit in num:
                temp.append(digit)
            else:
                return False
        return True
    return False


# N = 192
N = 273
ans = fascinating(N)
if ans:
    print('Fascinating')
else:
    print('not Fascinating')
