def getIndex(number_list, num):
    index = 0
    if number_list.count(num) > 1:
        index = number_list.index(num, number_list.index(num)+1)
    return index


lis = [1, 2, 2, 1, 0]
n = 2
ind = getIndex(lis, n)
print(ind)


