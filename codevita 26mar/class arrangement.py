input_string = input()
len_input_string = len(input_string)

no_of_boys = no_of_girls = output = 0

for item in range(len_input_string):
    if input_string[item] == 'B':
        no_of_boys = no_of_boys + 1
    elif input_string[item] == 'G':
        no_of_girls = no_of_girls + 1

if no_of_boys > no_of_girls + 1 or no_of_girls > no_of_boys + 1:
    output = (-1)

if len_input_string % 2:
    temp_num = (len_input_string + 1) // 2
    even_no_of_boys = even_no_of_girls = 0
    for item in range(len_input_string):
        if item % 2 == 0:
            if input_string[item] == 'B':
                even_no_of_boys = even_no_of_boys + 1
            else:
                even_no_of_girls = even_no_of_girls + 1
    if no_of_boys > no_of_girls:
        output = temp_num - even_no_of_boys
    elif no_of_girls > no_of_boys:
        output = temp_num - even_no_of_girls

else:
    odd_no_of_boys = even_no_of_boys = 0
    for item in range(len_input_string):
        if input_string[item] == 'B':
            if item % 2:
                odd_no_of_boys = odd_no_of_boys + 1
            else:
                even_no_of_boys = even_no_of_boys + 1
    output = min(len_input_string // 2 - odd_no_of_boys, len_input_string // 2 - even_no_of_boys)
print(output)
