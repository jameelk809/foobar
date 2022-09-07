def strstr(s,x):
    if x in s:
        return s.index(x)
    else:
        return -1


s = 'GeeksForGeeks'
x = 'For'
print(strstr(s, x))