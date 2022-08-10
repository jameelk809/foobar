def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    res = []
    for candy in candies:
        if candy + extraCandies >= m:
            res.append(True)
        else:
            res.append(False)
    return res


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
