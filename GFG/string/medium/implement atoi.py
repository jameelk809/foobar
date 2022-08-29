def atoi(string):
    if string[0] != "-" and (ord(string[0]) < 47 or ord(string[0]) > 57):
        return -1
    for i in range(1, len(string)):
        if 48 <= ord(string[i]) <= 57:
            continue
        else:
            return -1
    return int(string)


str = '-123'
print(atoi(str))
