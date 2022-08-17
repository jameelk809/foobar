"""An intelligence agency has received reports about some threats. The reports consist of numbers in a mysterious
method. There is a number “N” and another number “R”. Those numbers are studied thoroughly, and it is concluded that
all digits of the number ‘N’ are summed up and this action is performed ‘R’ number of times. The resultant is also a
single digit that is yet to be deciphered. The task here is to find the single-digit sum of the given number ‘N’ by
repeating the action ‘R’ number of times. """


# N = 99
N = 1234
R = 2


def sumDigits(x):
    s = 0
    for digit in str(x):
        s += int(digit)
    return s


sumDig = sumDigits(N)
sumDig = sumDig*R
print(sumDigits(sumDig))
