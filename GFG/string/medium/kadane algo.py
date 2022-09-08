def maxSubArraySum(arr, N):
    sumed = arr[0]
    maxsum = arr[0]
    for i in range(1, N):
        sumed = max(arr[i], arr[i] + sumed)
        maxsum = max(maxsum, sumed)
    return maxsum


N = 5
Arr = [1, 2, 3, -2, 5]
print(maxSubArraySum(Arr, N))
