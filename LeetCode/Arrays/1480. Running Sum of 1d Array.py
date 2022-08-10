def runningSum(nums):
    res = []
    s = 0
    for item in nums:
        s += item
        res.append(s)
    return res


nums = [3, 1, 2, 10, 1]
print(runningSum(nums))