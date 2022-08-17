# TCS NQT Coding Question Day 1 Slot 2 – Question 1
"""Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with
his friends. So every time when the months starts he counts the number of sundays he will get to enjoy. Considering
the month can start with any day, be it Sunday, Monday…. Or so on. Count the number of Sunday jack will get within n
number of days. """

day = "mon"
n = 20

arr = ["mon", "tue,", "wed", "thu", "fri", "sat", "sun"]
i = arr.index(day)
res = 1
rem = 6 - i
n = n - rem
if n > 0:
    res += n // 7
print(res)
