def buildArray(nums):
    build = []
    for i in range(len(nums)):
        build.append(nums[nums[i]])
    return build


nums = [0, 2, 1, 5, 3, 4]
print(buildArray(nums))
