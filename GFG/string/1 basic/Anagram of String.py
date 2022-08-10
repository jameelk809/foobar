"""
Given two strings S1 and S2 in lowercase, the task is to make them anagram.
The only allowed operation is to remove a character from any string. Find the
minimum number of characters to be deleted to make both the strings anagram.
Two strings are called anagram of each other if one of them can be converted
into another by rearranging its letters.
"""


def remAnagram(str1, str2):
    count = 0
    # if len(str1) > len(str2):
    #     big = str1
    #     small = str2
    # else:
    #     big = str2
    #     small = str1
    for item in S1:
        if item not in S2:
            count += 1
    return count


S2 = 'basgadhbfgvhads'
S1 = 'sjdhgvbjdsbhvbvd'
print(remAnagram(S1, S2))
