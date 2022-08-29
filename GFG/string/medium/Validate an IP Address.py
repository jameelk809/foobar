def isValid(s):
    # s = list(map(int, s.split('.')))
    s = s.split('.')
    if len(s) != 4:
        return False
    for octet in s:
        if not(octet.isnumeric()) or (octet == "" or len(octet) != len(str(int(octet))) or int(octet) > 255):
            return False
    return True


address = '222.0111.111.111'
# address = '5555..555'
print(isValid(address))
