def checkValid(string):
    if string.isalpha():
        string = string.replace(" ", "")
        str_lower = string.lower()
        if string != str_lower:
            return True
        else:
            return False


if __name__ == '__main__':
    count = 0
    strlist = ['abcAB aB', 'wWeErR', 'qqqqqq', 'AAAAA', 'jfL@gg']
    for item in strlist:
        if checkValid(item):
            count += 1
    print("count of valid string: ", count)
    print("count of invalid string: ", len(strlist) - count)
