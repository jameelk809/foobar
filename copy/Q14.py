str1 = 'Hello World'
str2 = 'Outstanding'
lis = [str1, str2]
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count_list = []
for item in lis:
    count = 0
    for letter in item:
        if letter in vowels:
            count += 1
    count_list.append(count)
if count_list[0] > count_list[1]:
    print(lis[0])
    print(count_list[0])
elif count_list[1] > count_list[0]:
    print(lis[1])
    print(count_list[1])
else:
    print('Both string have same no. of vowels')
