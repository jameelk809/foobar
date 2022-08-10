# # batch = 'asfddagha'
# batch = 'HelloWorld'.lower()
# unique = 0
# for i in range(len(batch)):
#     flag = True
#     count = 0
#     for j in range(len(batch)):
#         if batch[i] == batch[j]:
#             count += 1
#         if count > 1:
#             flag = False
#             break
#     if flag:
#         unique += 1
# print(unique)


# string = 'HelloWorld'.lower()
# arr = list(string)
# temp = [0]*255
# count = 0
# for i in range(len(arr)):
#     temp[ord(arr[i])] += 1
# for i in range(255):
#     if temp[i] == 1:
#         count += 1
# print(count)

# def CheckPassword(strg, n):
#     num = 0
#     cap = 0
#     flag = 0
#     if len(strg) >= 4:
#         flag = 1
#         arr = list(strg)
#         if 48 <= ord(arr[0]) <= 57:
#             flag = 0
#         for item in arr:
#             if 48 <= ord(item) <= 57:
#                 num += 1
#             if 65 <= ord(item) <= 90:
#                 cap += 1
#             if item == ' ' or item == '/':
#                 flag = 0
#         if num < 1 or cap < 1:
#             flag = 0
#     return flag
#
#
# string = 'A4..'
# print(CheckPassword(string, len(string)))

# st = 'srtrwffsrrt'
#
#
# def FirstNonRepeat(st):
#     arr = list(st)
#     freq = [0] * 255
#     for i in range(len(arr)):
#         freq[ord(arr[i])] += 1
#     for item in arr:
#         if freq[ord(item)] == 1:
#             return item
#     return '0'
#
#
# print(FirstNonRepeat(st))
#
# from collections import Counter
#
#
# def FirstNonRepeat(string):
#     freq = Counter(string)
#     for i in string:
#         if freq[i] == 1:
#             print(i)
#             break
#
#
# string = 'efefwwef'
# FirstNonRepeat(string)


# int n = 7, i,j=0;
# int arr[7] = {1, 2, 3, 4, 5, 6, 7};
# int temp[100];
# while(n>1){
# j = 2*j+1;
# n/=2;
# }
# cout<<arr[j];

# n = 15
# arr = []
# j = 0
# for i in range(1, n + 1):
#     arr.append(i)
# print(arr)
# while n > 1:
#     j = 2 * j + 1
#     n //= 2
# print(arr[j])

# st = 'coding is awesome'
# arr = list(st.split())
# arr = arr[::-1]
# stt = []
# for item in arr:
#     stt.append(item)
# print(' '.join(stt))

# # inp = [3521, 2452, 1352]
# inp = list(map(int, input().split()))
# min_th = 100
# max_hu = -1
# min_te = 100
# max_on = -1
# for num in inp:
#     th = num // 1000
#     hu = (num % 1000)//100
#     te = (num % 100)//10
#     on = num % 10
#     if th < min_th:
#         min_th = th
#     if hu > max_hu:
#         max_hu = hu
#     if te < min_te:
#         min_te = te
#     if on > max_on:
#         max_on = on
# print(min_th*1000 + max_hu*100 + min_te*10 + max_on)

# def isPalindrome(strn):
#     if strn == strn[::-1]:
#         return True
#     return False
#
#
# def convert_to_palindrome(strng):
#     if isPalindrome(strng):
#         return 0
#     length = len(strng)
#     res = 0
#     i = 0
#     while length > 0:
#         tempstr = strng[i:]
#         if isPalindrome(tempstr):
#             res = i
#             break
#         i = i + 1
#         length -= 1
#     return strng[res - 1::-1]
#
#
# # string = 'abba'
# string = 'racecarr'
# print(convert_to_palindrome(string))
