# Test case
t = int(input())
# loop for each test case
for tc in range(t):
    # number of elements
    n = int(input())
    # itemList
    itemList = list(map(int, input().split()))
    i = 0
    max = 0
    itemType = itemList[0]
    # loop to calculate max possible type of dish
    while i < n:
        # count variable
        c = 1
        j = i + 1
        while j < n:
            if itemList[i] == itemList[j] and j != i + 1:
                c += 1
                if j < n - 1 and itemList[j] == itemList[j + 1]:
                    j += 1
            j += 1
        # if the count is greater than max then max=c
        if max < c:
            max = c
            itemType = itemList[i]
        i += 1
    # print the type of Dish
    print(itemType)
