def find_Novowels(str_list):
    output = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for item in str_list:
        flag = 0
        for vowel in vowels:
            if vowel in item:
                flag = 1
        if not flag:
            output.append(item)

    return output


lis = ['almost', 'vtyw', 'sound', 'prtwy']
new_list = find_Novowels(lis)
if len(new_list) != 0:
    print(new_list)
else:
    print("No string found")
