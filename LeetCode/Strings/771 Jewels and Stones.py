def numJewelsInStones(jewels, stones):
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
