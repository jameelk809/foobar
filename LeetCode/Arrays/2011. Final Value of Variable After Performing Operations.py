def finalValueAfterOperations(operations):
    res = 0
    for ops in operations:
        if '++' in ops:
            res += 1
        if '--' in ops:
            res -= 1
    return res


operations = ["X++", "++X", "--X", "X--"]
print(finalValueAfterOperations(operations))
