def getConcatenation(nums):
    res = []
    for i in range(len(nums)):
        res.append(nums[i])
    for i in range(len(nums)):
        res.append(nums[i])
    return res


nums = [1, 3, 2, 1]
print(getConcatenation(nums))