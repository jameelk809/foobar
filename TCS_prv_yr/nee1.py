# def checkVowels(array):
#     char = '@'
#     vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
#     count = 0
#     for item in array:
#         lis = list(item)
#         out = ''
#         for j in range(len(lis)):
#             if lis[j] in vowels:
#                 count += 1
#                 lis[j] = char
#         for element in lis:
#             out += element
#         print(out + ' ' + str(count))
#         count = 0
#
#
# num = int(input())
# cos = input()
# array = []
# for item in range(num):
#     array.append(input().lower())
#
# checkVowels(array)










def checkVowels(string, char):
    vow = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', '@']
    return_string = ""
    for ch in string:
        if ch in vow:
            return_string += char
            continue
        return_string += ch

    return_string += str(return_string.count(char))
    return return_string


tc = int(input())
ch = input()
str_li = []
for i in range(tc):
    str_li.append(checkVowels(input(), ch))

for string in str_li:
    print(string)

#
#
#
#
#
#
# # def checkVowels(string, char):
# #     vow = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
# #     return_string = ""
# #     for ch in string:
# #         if ch in vow:
# #             return_string += char
# #             continue
# #         return_string += ch
# #
# #     return_string += str(return_string.count(char))
# #     return return_string
# #
# #
# # tc = int(input())
# # ch = input()
# # str_li = []
# # for i in range(tc):
# #     str_li.append(checkVowels(input(), ch))
# #
# # print("\n".join(str_li))
# #
