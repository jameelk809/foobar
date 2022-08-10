def check_palindrome(listOfString):
    return_list = []
    for item in listOfString:
        l_item = item.lower()
        rev = l_item[::-1]
        if l_item == rev:
            return_list.append(item)
    return return_list


# lis = ['Hello', 'Malayalam', 'Radar']
# print(check_palindrome(lis))

if __name__ == '__main__':
    count = int(input('Enter no of elements: '))
    lis = []
    for i in range(count):
        lis.append(input('Enter element: '))
    output = check_palindrome(lis)
    if len(output) != 0:
        for item in output:
            print(item)
    else:
        print('No palindrome found')
