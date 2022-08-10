"""
Given a list of names, display the longest name.
"""


def longest(names, n):
    maxlen = len(names[0])
    maxitem = names[0]
    for item in names:
        length = len(item)
        if length > maxlen:
            maxlen = length
            maxitem = item
    return maxitem


names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
n = 5
print(longest(names, n))
