def findMedianSortedArrays(nums1, nums2):
    merged_nums = nums1 + nums2
    merged_nums.sort()
    n = len(merged_nums)
    if n % 2 == 0:
        median = (merged_nums[(n//2-1)] + merged_nums[n//2])/2
    else:
        median = merged_nums[n//2]
    return median


nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
