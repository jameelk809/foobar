def FilledBuckets(N, queries):
    bucket = [0] * N
    for query in queries:
        if query == 1:
            bucket = [1]*N
        if query == 2:
            for i in range(len(bucket)):
                if (i + 1) % 2 == 0:
                    bucket[i] = 0
        if query == 3:
            for i in range(len(bucket)):
                if (i + 1) % 2 != 0:
                    bucket[i] = 0
        if query == 4:
            bucket = [0]*N
    # print(bucket)
    return bucket.count(1)


# Write your code here
queries = [1, 2, 2]
N = 5
print(FilledBuckets(N, queries))
