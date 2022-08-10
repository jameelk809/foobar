def shuffle(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(shuffle(nums, n))