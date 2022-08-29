def isBinary(str):
    binry = ['0', '1']
    for x in str:
        if x not in binry:
            return False
    return True


print(isBinary('101'))
