def areRotations(s1, s2):
    if len(s1) != len(s2):
        return 0
    if s2 not in (s1 * 2):
        return 0
    return 1


s1 = 'mightandmagic'
s2 = 'andmagicmigth'
print(areRotations(s1, s2))
