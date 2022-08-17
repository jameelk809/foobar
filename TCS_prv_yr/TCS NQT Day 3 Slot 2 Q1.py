"""
A furnishing company is manufacturing a new collection of curtains. The curtains are of two colors aqua(a) and
black (b). The curtains color is represented as a string(str) consisting of a’s and b’s of length N. Then, they
are packed (substring) into L number of curtains in each box. The box with the maximum number of ‘aqua’ (a)
color curtains is labeled. The task here is to find the number of ‘aqua’ color curtains in the labeled box.
"""

color = 'abbbaabbb'
L = 5

maxx = 0
count = 0
for i in range(len(color)):
    if i % L == 0:
        maxx = max(count, maxx)
        count = 0
    if color[i] == 'a':
        count += 1
maxx = max(count, maxx)
print(maxx)


