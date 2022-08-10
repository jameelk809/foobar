def check_palindrome(str_list):
    flag = -1
    palindrome_list = []
    for item in str_list:
        item = item.lower()
        for i in range(len(item)):
            flag = 0
            i1 = item[i]
            i2 = item[len(item)-i-1]
            if i1 == i2:
                flag = 1
                continue
            else:
                break
        if flag:
            palindrome_list.append(item)

    # for item in str_list:
    #     j = item.lower()
    #     if j == j[::-1]:
    #         palindrome_list.append(item)

    return palindrome_list


lis = ['Hello', 'malayalam', 'Radar']
pal_lst = check_palindrome(lis)
if len(pal_lst) != 0:
    print(pal_lst)
else:
    print("No palindrome")
