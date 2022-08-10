import math


val_dict = {'0': [0, 2]}
item = 1
numbers = '0123456789'
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
smalls = 'abcdefghijklmnopqrstuvwxyz'
temp_string = numbers + capitals + smalls

for c in temp_string[1:]:
    val_dict[c] = [item, item + 1]
    item = item + 1

list_element = input().split()
r = {}

for item in list_element:
    r_element = 0
    if len(item) == 1:
        r_element = val_dict[item][0]
    else:
        TEMP = val_dict[item[0]][0] * val_dict[item[1]][1]
        r_element = val_dict[item[1]][0] + TEMP
    r[item] = r_element

n = len(r)

if n == 1:
    print(r[list_element[0]])
else:
    maximum = 1
    for item in list_element:
        for item2 in list_element:
            if item != item2:
                maximum = max(maximum, math.gcd(r[item], r[item2]))
    print(maximum)
