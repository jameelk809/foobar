"""
def form_triangle(num1, num2, num3):
    success = "Triangle can be formed"
    failure = "Triangle can't be formed"
    if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num2 + num1:
        return success
    else:
        return failure


num1 = 4
num2 = 3
num3 = 1
form_triangle(num1, num2, num3)
"""

"""
def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # Start writing your code here
    # Populate the variables: five_needed and one_needed

    five_needed = rupees_to_make // 5
    one_needed = rupees_to_make - five_needed * 5

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    if no_of_one >= five_needed and no_of_one >= one_needed:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105, 20, 5)
"""

"""
def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    delivery_charge = 0
    if (food_type == 'N' or food_type == 'V') and quantity_ordered > 0 and distance_in_kms > 0:
        if food_type == 'V':
            bill_amount = 120 * quantity_ordered
        if food_type == 'N':
            bill_amount = 150 * quantity_ordered
        if distance_in_kms <= 3:
            pass
        elif distance_in_kms <= 6:
            delivery_charge = (distance_in_kms - 3) * 3
            bill_amount = bill_amount + delivery_charge
        elif distance_in_kms > 6:
            delivery_charge = (distance_in_kms - 6) * 6 + 3 * 3
            bill_amount = bill_amount + delivery_charge
        return bill_amount


bill = calculate_bill_amount("N", 2, 0)
print(bill)


def calculate_loan(account_number, salary, account_balance,
                   loan_type, loan_amount_expected, customer_emi_expected):
    bank_emi_expected = 0
    eligible_loan_amount = 0
    if 1000 <= account_number <= 1999:
        if account_balance >= 100000:
            if loan_type == 'Business' and salary > 75000:
                eligible_loan_amount = 7500000
                bank_emi_expected = 84
                if customer_emi_expected <= bank_emi_expected and loan_amount_expected <= eligible_loan_amount:
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:", customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif loan_type == 'House' and salary > 50000:
                eligible_loan_amount = 6000000
                bank_emi_expected = 60
                if customer_emi_expected <= bank_emi_expected and loan_amount_expected <= eligible_loan_amount:
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:", customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif loan_type == 'Car' and salary > 25000:
                eligible_loan_amount = 500000
                bank_emi_expected = 36
                if customer_emi_expected <= bank_emi_expected and loan_amount_expected <= eligible_loan_amount:
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:", customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")


calculate_loan(1001, 50000, 250000, "House", 300000, 30)
"""


#   famous chinese puzzle
"""
def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0
    ans = False
    for i in range(heads + 1):
        j = heads - i
        if (2 * i) + (4 * j) == legs:
            chicken_count = i
            rabbit_count = j
            ans = True
            break
    if ans:
        print(chicken_count, rabbit_count)
    else:
        print(error_msg)


heads = 90
legs = 260
solve(heads, legs)

rabbit = legs//2 - heads
chick = heads - rabbit
"""
"""
def find_max(num1, num2):
    l1 = []
    max_num = -1
    if num1 < num2:
        for i in range(num1, num2 + 1):
            if 10 <= i <= 99 and i % 5 == 0 and i % 3 == 0:
                l1.append(i)
                l1.sort()
                max_num = l1[-1]
    return max_num


find_max(10, 15)
"""

"""
def get_count(num_list):
    count = 0
    l = []
    for i in num_list:
        if i not in l:
            l.append(i)
        else:
            count += 1
    return count


num_list = [0, 1, 5, 100, -20, -20, 6, 0, 0]
print(get_count(num_list))
"""

"""
def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    source = source[0:3]
    destination = destination[0:3]
    ticket_num = 101+no_of_passengers
    if no_of_passengers > 5:
        no_of_passengers = 5

    for i in range(no_of_passengers):
        ticket_number_list.append(airline+':'+source+':'+destination+':'+str(ticket_num-5))
        ticket_num += 1
    return ticket_number_list


print(generate_ticket("AI", "Bangalore", "London", 5))


boarding_call = "Good Evening, this is the final call to AI passengers for the 
flight AI 466 which is planned to take off at 8.40A.M. " 
if boarding_call.startswith("Good Evening"): 
    print(boarding_call.replace("Good Evening", "Good Morning")) 
if (boarding_call.find("AI")) >= 0: 
    print("Welcome to Air India.") 
if boarding_call.endswith("A.M."): 
    print("Passengers are requested to have their breakfast.")

a = boarding_call.split()
for i in a:
    if i.isdigit():
        print("Flight Number is specified to the passengers.")

print("Total number of times flight service name is specified in the boarding call:", boarding_call.count("AI"))
message = "Thank you all..Have a nice journey!"
print(message.upper())
print(message.lower())


count = 0
i = 1
for baggage_weight in 29, 30, 31, 32, 28:
    if baggage_weight >= 1 or baggage_weight <= 30:
        print("Passenger", i, ": Proceed for baggage check.")
    else:
        count += 1
        print("Passenger", i, ": Maximum baggage weight allowed is 30kg.")
    i += 1
print("No. of passengers who cleared baggage check:", count)
"""

# PF-Tryout
"""This program is expected to display all the even numbers
between 1 and n (both inclusive)"""
"""
i = 1
n = 10
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1
"""

"""
def find_leap_years(given_year):
    list_of_leap_years = []
    isleap = False
    while not isleap:
        if (given_year % 400 == 0) or (given_year % 100 != 0) and (given_year % 4 == 0):
            isleap = True
            for i in range(1, 16):
                list_of_leap_years.append(given_year)
                given_year += 4
        else:
            given_year += 1
    return list_of_leap_years


list_of_leap_years = find_leap_years(1000)
print(list_of_leap_years)
"""

"""
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
price_list = [1760, 2119, 1599, 3920, 3999]
reqd_gems = ["Ivory", "Emerald", "Garnet"]
reqd_quantity = [3, 10, 12]

gems_list = ['Amber', 'Aquamarine', 'Opal', 'Topaz']
price_list = [4392, 1342, 8734, 6421]
reqd_quantity = [2, 1, 3]
reqd_gems = ['Amber', 'Opal', 'Topaz']


def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = 0
    total_quantity = sum(reqd_quantity)
    if total_quantity > 0:
        if set(reqd_gems).issubset(set(gems_list)):
            for gems in reqd_gems:
                price = price_list[gems_list.index(gems)]*reqd_quantity[reqd_gems.index(gems)]
                bill_amount += price
            if bill_amount > 30000:
                disc = 0.05*bill_amount
                bill_amount += disc
        else:
            bill_amount = -1
    return bill_amount


bill_amount = calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
"""

"""
def create_largest_number(number_list):
    largest_number = ""
    number_list.sort(reverse=True)
    for numbers in number_list:
        largest_number += str(numbers)
    return int(largest_number)


number_list=[98, 10, 22]
largest_number = create_largest_number(number_list)
print(largest_number)


def check_palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        return True
    else:
        return False


status = check_palindrome("malayalam")
if status:
    print("word is palindrome")
else:
    print("word is not palindrome")
"""

"""
def encode(message):
    output = ''
    previous = message[0]
    i = 1
    count = 1
    while len(message) > i:
        if previous == message[i]:
            count += 1
        else:
            output += str(count) + previous
            count = 1
            previous = message[i]

        if i == len(message) - 1:
            output += str(count) + previous
        i += 1
    if len(message) == 1:
        output += str(count) + previous
    return output


encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
"""

"""
def translate(bilingual_dict, english_words_list):
    swedish_words_list = []
    for words in english_words_list:
        meanings = bilingual_dict.get(words)
        swedish_words_list.append(meanings)
    return swedish_words_list


bilingual_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
english_words_list = ["merry", "christmas"]
print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)

swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:", swedish_words_list)
"""

"""
def find_common_characters(msg1, msg2):
    common_characters = ""
    msg1 = set(msg1)
    msg2 = set(msg2)
    for letters in msg1:
        if letters in msg2:
            if letters == " ":
                continue
            common_characters += letters
    if len(common_characters) == 0:
        return -1
    return common_characters


msg1 = "moto"
msg2 = "moto"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
"""

"""
def encrypt_sentence(sentence):
    encrypted_sentence = []
    l = sentence.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for words in l:
        if (l.index(words)+1) % 2 == 0:
            c = []
            v = []
            for letters in words:
                if letters in vowels:
                    v.append(letters)
                else:
                    c.append(letters)
            c.extend(v)
            words = ""
            for ele in c:
                words += ele
        else:
            words = words[::-1]
        encrypted_sentence.append(words)
    list = ' '.join(encrypted_sentence)
    return list


sentence = "the sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
"""

"""
def find_correct(word_dict):
    ans = [0, 0, 0]
    wrong_count = 0
    for key, value in word_dict.items():
        if key == value:
            ans[0] += 1
        elif len(key) != len(value):
            ans[2] += 1
        else:
            for i in range(len(key)):
                if key[i] != value[i]:
                    wrong_count += 1
            if wrong_count <= 2:
                ans[1] += 1
            else:
                ans[2] += 1
            wrong_count = 0

    return ans


word_dict = {'MIND': 'MUND', 'CHECK': 'CHEK', 'RADIO': 'RADICAL', 'ALWAYS': 'ALLISWELL', 'VENDOR': 'VENDING'}
    # {"THEIR": "THEIR",
    #          "BUSINESS": "BISINESS",
    #          "WINDOWS": "WINDMILL",
    #          "WERE": "WEAR",
    #          "SAMPLE": "SAMPLE"}
answer = find_correct(word_dict)
print(answer)
"""

"""
def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    speciality = ""
    max_val = 0
    dict_count = {'P': 0, 'O': 0, 'E': 0}
    for items in patient_medical_speciality_list:
        if items == 'P':
            dict_count['P'] += 1
        elif items == 'O':
            dict_count['O'] += 1
        elif items == 'E':
            dict_count['E'] += 1
    print(dict_count)
    for key, value in dict_count.items():
        if value > max_val:
            max_val = value
            max_key = key
    speciality = medical_speciality.get(max_key)
    return speciality


patient_medical_speciality_list = [101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'P']
    # [301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)
"""

"""
def sms_encoding(data):
    code = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    data = data.split()
    length = len(data)
    print(len(data))
    for word in data:
        index_of_word = data.index(word)+1
        if word in vowels:
            pass
        else:
            for letter in word:
                if letter in vowels:
                    word = word.replace(letter, "")
        code += word
        if index_of_word != length:
            code += " "
    return code


data = "I love Python"
print(sms_encoding(data))
"""

"""
def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    data_lower = []
    data = data.split()
    for words in data:
        words = words.lower()
        data_lower.append(words)

    for words in data_lower:
        count = data_lower.count(words)
        if count > frequency:
            frequency = count
            word = words

    print(word, frequency)


data = "Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
"""

"""
name1 = "Roger"
name2 = "Robert"


def swap(name1, name2):
    temp = name1
    name1 = name2
    name2 = temp


print("Before swapping: name1 = "+ name1 + " name2 = " + name2)
swap(name1, name2)
print("After swapping: name1 = "+ name1 + " name2 = " + name2)
"""

"""
import math

temp = ['Mysore', 'Bangalore', 'Pune', 'Chennai']
temp.sort()
count1 = len(temp[0])
count2 = len(temp[-1])
print(math.ceil(count1/count2))
"""

"""
for var1 in range(1, 6):
    for var2 in range(1, 6):
        if var1%var2 != 0:
            pass
        elif var2 < var1:
            continue
        else:
            print(var1*var2)
"""

"""
num1 = 11//10
num2 = 11%10
num3 = 20
num4 = 40
num5 = 5

if num3>num4:
    if num3 > num5:
        print(num5*num4/num3)
    else:
        print(num3/num2)
else:
    if num1 == num2:
        print(num4/num3)
    else:
        print(num4/num5)
"""

"""
var1 = 0
var2 = 10
while var1 <= 10 and var2 >= 1:
    print(var1, var2)
    var2 = var2 - 1
    var1 = var1 + 1
    if var1 == var2:
        break
"""

"""
temp = "Hello? how are you?"
if temp.isdigit():
    temp += "fine"
else:
    for var1 in range(len(temp)):
        if temp[var1] == '?':
            final_val = temp[:var1]
            break
if final_val.endswith('u'):
    final_val.replace('you', 'u')
else:
    final_val=final_val.upper()
print(final_val)
"""

"""
var1=5
var2=5
var3=1
var4=1
var5=0
print((var1+var2)>(var3/var4) and var5<=(var1-var3*var2))
print(not ((var3>=var4) and (var3==var4)))
print((var4>=var2) and (var1>=var2))
"""

"""
list1 = [1,2,1,3,3,1,2,1,2,1]
tuple1 = ("A","B","C","D")
tuple1 += ("E",)
list2 = []
for var1 in range(5, len(list1)):
    list2.append(list1[var1-5]+list1[var1])

for var1 in range(0, len(list2)):
    print(tuple1[var1], list2[var1])

def func(sample, res, key, val):
    if key in sample:
        res = True
        sample.update({key: val})
    res = False


res = None
sample = {"XS": 1, "X": 0, "XL": 3, "XXL": 4}
func(sample, res, "X", 2)
print(sample["X"], res)
"""

"""
my_str = "All3 that4 glitters8 is2 not3 gold4"
my_list = []

for char in my_str:
    if char.isdigit():
        my_list.append(int((char)))
        my_str.replace(char, "")
print(my_str, my_list)
"""

"""
code = "jack and jill went up the hill"
for temp in code.split():
    if temp.endswith("ill"):
        print("Count : ", code.count("ill"))
        break
code = code.replace("j", "m")
for temp in code.split():
    if len(temp)%2 != 0:
        temp_str = str(temp)
        code = code.replace(temp_str, temp_str.upper())
print(code)
"""

"""
def check_loss(game_history, game_points, total):
    if game_history[1] == 0:
        game_points[1] -= 1
    else:
        loss_points = game_history[1] * 2
        game_points[1] -= loss_points

    total = game_points[0] + game_points[1] + game_points[2]


game_history = [4, 0, 2]
game_points = [12, -4, 2]
total = 0
check_loss(game_history, game_points, total)
game_history = [5, 2, 2]
check_loss(game_history, game_points, total)
print(total, game_points)
"""

"""
result = 0


def find_sum(num1, num2):
    if (num1 != num2):
        result = num1 + num2
    else:
        result = 2 * (num1 + num2)


find_sum(3, 4)
print(result)
find_sum(5, 5)
print(result)
"""

"""
def find_avg(list_num):
    result_sum=0
    for num in list_num:
        result_sum+=num
    result_avg=result_sum/len(list_num)
find_avg([5,8,5])
print(result_avg)
"""

"""
def func(word, char="A"):
    if (char == "A"):
        return len(word[1:])
    elif (char == "B"):
        return len(word[2:])
    else:
        return len(word)


print(func("Apple", "A"), end=" ")
print(func("Apple", "B"), end=" ")
print(func("Apple"), end=" ")
print(func("Apple", "C"), end=" ")
"""

"""
def func(sample, res, key,val):
    index =- 1
    if(key in sample):
        res = True
        index = sample.index(key)
        values[index] = val
    else:
        res = False
    return index

res = None
sample = ["A","B","C","D"]
values = [1,1,3,4,5]
index = func(sample,res,"B",2)
print(values[index], res)
"""

"""
import math


def factorial(number):
    return math.factorial(number)


def find_strong_numbers(num_list):
    strong_num_list = []
    sum_of_fact = 0
    for number in num_list:
        x = number
        if number == 0:
            sum_of_fact = 1
        else:
            while number != 0:
                rem = (number % 10)
                fact = factorial(rem)
                sum_of_fact += fact
                number = number//10
            if x == sum_of_fact:
                strong_num_list.append(x)
            sum_of_fact = 0
    return strong_num_list


num_list = [145, 375, 100, 2, 10, 40585, 0]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)
"""

"""
def grade(marks):
    if 80 <= marks <= 100:
        gr = 'A'
    elif 73 <= marks <= 79:
        gr = 'B'
    elif 65 <= marks <= 72:
        gr = 'C'
    elif 0 <= marks <= 64:
        gr = 'D'
    else:
        gr = 'Z'
    return gr


print(grade(88))
"""

"""
def find_pairs_of_numbers(num_list, n):
    count = 0
    for num in num_list:
        for test_ele in num_list:
            if test_ele + num == n and test_ele != num:
                print(num, test_ele)
                count += 1
                num_list.remove(num)
    return count


num_list = [10, 20, 30, 40, 50]
n = 100
print(find_pairs_of_numbers(num_list, n))
"""

# This verification is based on string match.
"""
def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func is None:
        return sum(list_of_num)
    else:
        return sum(filter_func)


def even(data):
    even_list = []
    for numbers in data:
        if numbers % 2 == 0:
            even_list.append(numbers)
    return even_list


def odd(data):
    odd_list = []
    for numbers in data:
        if numbers % 2 != 0:
            odd_list.append(numbers)
    return odd_list


sample_data = range(1, 11)

print(sum_of_numbers(sample_data, filter_func=even()))
print(sum_of_numbers(sample_data, even(sample_data)))
# print(sum_of_numbers(sample_data, odd(sample_data)))
"""

# import math

"""_______________FROM   GITHUB________________"""

# def sum_of_numbers(list_of_num, filter_func=None):
#     if filter_func == None:
#         return sum(list_of_num)
#     else:
#         return sum(filter_func)
#
#
# def even(data):
#     e = []
#     for num in data:
#         if num % 2 != 0:
#             e.append(num)
#     return e
#
#
# def odd(data):
#     o = []
#     for num in data:
#         if num % 2 != 0:
#             o.append(num)
#     return o
#
#
# sample_data = range(1, 11)
#
# print(sum_of_numbers(sample_data, even(sample_data)))

# lex_auth_01269441810970214471

# def check_double(number):
#     flag = True
#     double_num = str(2 * number)
#     number = str(number)
#     if len(double_num) == len(number):
#         for digits in number:
#             if digits not in double_num:
#                 flag = False
#                 break
#     else:
#         flag = False
#     return flag
#
#
# print(check_double(14))
# lex_auth_012693816779112448160

# def calculate(distance, no_of_passengers):
#     profit = -1
#     fuel_price = 70
#     mileage = 10
#     ticket_price = 80
#     collection = no_of_passengers * ticket_price
#     investment = (distance/mileage)*fuel_price
#     if collection > investment:
#         profit = collection-investment
#     return profit
#
#
# distance = 20
# no_of_passengers = 50
# print(calculate(distance, no_of_passengers))
# lex_auth_01269438947391897654

# # Global variable
# list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)
#
#
# def find_more_than_average():
#     count = 0
#     avg = sum(list_of_marks)/len(list_of_marks)
#     for marks in list_of_marks:
#         if marks > avg:
#             count += 1
#     percent_avg = count/len(list_of_marks)*100
#     return percent_avg
#
#
# def sort_marks():
#     sorted_marks = list(list_of_marks)
#     sorted_marks.sort()
#     return sorted_marks
#
#
# def generate_frequency():
#     frequency = []
#     for i in range(1, 26):
#         frequency.append(list_of_marks.count(i))
#     return frequency
#
#
# print(find_more_than_average())
# print(generate_frequency())
# print(sort_marks())


# calculating airport expenditure
# def calculate_expenditure(list_of_expenditure):
#     total = 0
#     try:
#         for expenditure in list_of_expenditure:
#             total += expenditure
#         print(total)
#     except:
#         print("Some error occurred")
#     print("Returning back from function.")
#
#
# list_of_values = [100, 200, 300, "400", 500]
# calculate_expenditure(list_of_values)


# def calculate_expenditure(list_of_expenditure):
#     total = 0
#     try:
#         for expenditure in list_of_expenditure:
#             total += expenditure
#         print("Total:", total)
#         avg = total / num_values
#         print("Average:", avg)
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")
#     except:
#         print("Some error occurred")
#
#
# list_of_values = [100, 200, 300, "400", 500]
# num_values = 0
# calculate_expenditure(list_of_values)


# def calculate_expenditure(list_of_expenditure):
#     total = 0
#     try:
#         for expenditure in list_of_expenditure:
#             total += expenditure
#         print("Total:", total)
#         avg = total / num_values
#         print("Average:", avg)
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")
#     except:
#         print("Some error occurred")
#
#
# list_of_values = [100, 200, 300, "400", 500]
# num_values = 0
# calculate_expenditure(list_of_values)

# def calculate_sum(list_of_expenditure):
#     total = 0
#     try:
#         for expenditure in list_of_expenditure:
#             total += expenditure
#         print("Total:", total)
#         avg = total / no_values
#         print("Average:", avg)
#     # except NameError:
#     #     print("Name error occurred")
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")
#
#
# try:
#     list_of_values = [100, 200, 300, 400, 500]
#     num_values = len(list_of_values)
#     calculate_sum(list_of_values)
# except NameError:
#     print("Name error occurred")
# except:
#     print("Some error occurred")
# balance = 1000
# amount = 300


# def take_card():
#     print("Take the card out of ATM")
#
#
# try:
#     if balance >= int(amount):
#         print("Withdraw")
#     else:
#         print("Invalid amount")
#
# except TypeError:
#     print("Type Error Occurred")
# except ValueError:
#     print("Value Error Occurred")
# except:
#     print("Some error Occurred")
# finally:
#     take_card()


# def divide(num1, num2):
#     try:
#         num3 = num1 / num2
#         print(num3)
#     except:
#         print("Inside function")
#
#
# try:
#     divide(100, 0)
# except:
#     print("Outside function")


# num1=100
# num2=0
# try:
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Zero Division Error Occurred")

# def division(value_1, value_2):
#     try:
#         return int(value_1) / value_2
#     except TypeError:
#         print("Type error")
#     except ValueError:
#         print("Value error")
#     finally:
#         print("Finally")
#     print("Done")
#
#
# division('A', 10)
# lex_auth_01269437504257228837

# def find_average(mark_list):
#     try:
#         total = 0
#         for i in range(0, len(mark_list)+1):
#             total += mark_list[i]
#         marks_avg = total / len(mark_list)
#         return marks_avg
#     except NameError as n:
#         print(NameError, n)
#     except TypeError as e:
#         print(TypeError, e)
#     except ValueError as v:
#         print(v)
#     except ZeroDivisionError as z:
#         print(ZeroDivisionError, z)
#     except IndexError as i:
#         print(IndexError, i)


# mark1 = "A"
# mark1 = int("A")
# m_list = [mark1, 2, 3, 4]
# m_list = []
# print("Average marks:", find_average(m_list))
# def human_tower(no_of_people):
#     if no_of_people == 1:
#         return 1 * 50
#     else:
#         return no_of_people * 50 + human_tower(no_of_people - 2)
#
#
# print("Total weight of human tower: ", human_tower(35))

#
# import turtle
#
# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# my_win.setup(1000, 1000)
#
#
# def draw_spiral(my_turtle, line_len):
#     if line_len <= 0:  # works till length is greater than 0
#         return
#     else:
#         my_turtle.forward(line_len)
#         my_turtle.right(45)
#         draw_spiral(my_turtle, line_len - 5)  # recursive call
#
#
# draw_spiral(my_turtle, 360)
# destination = "south"

# def tower_of_hanoi(n, source, destination, temp):
#     if n == 1:
#         disk = source.pop(0)  # Removes the element in specified position
#         destination.insert(0, disk)  # Inserts the given element in specified position
#         return
#     tower_of_hanoi(n - 1, source, temp, destination)
#     disk = source.pop(0)
#     destination.insert(0, disk)
#     tower_of_hanoi(n - 1, temp, destination, source)
#     return
#
#
# source = ["blue", "green", "orange"]
# destination = []
# temp = []
# tower_of_hanoi(3, source, destination, temp)
# print("Source:", source)
# print("Destination:", destination)


# def fun(number):
#     if number < 2:
#         return 1
#     elif number / 2 == 2:
#         return fun(number - 1)
#     else:
#         return (number - 1) * fun(number - 1)
#
#
# print(fun(7))

# lex_auth_01269437527007232044

# def human_pyramid(no_of_people):
#     # returns the tower weight for a given no. of pople at base
#     if no_of_people <= 1:
#         return 1 * 50
#     else:
#         return no_of_people * 50 + human_pyramid(no_of_people - 2)
#
#
# def find_maximum_people(max_weight):
#     i = 1
#     while i < (max_weight // 50):
#         weight = human_pyramid(i)
#         if weight > max_weight:
#             return i - 1
#             # when the weight exceed this means older value was in the limit
#         i = i + 2
#
#
# max_people = find_maximum_people(max_weight=1000)
# print(max_people)

# Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not.
# The function should return true, if it is a palindrome. Else it should return false.

# def is_palindrome(word):
#     word = word.lower()
#     if len(word) < 1:
#         return True
#     else:
#         if word[0] == word[len(word)-1]:
#             return is_palindrome(word[1:len(word)-1])
#         else:
#             return False
#
#
# result = is_palindrome("mam dad")
# if result:
#     print("The given word is a Palindrome")
# else:
#     print("The given word is not a Palindrome")

# def find_factors(num):
#     factors = []
#     for i in range(2, (num + 1)):
#         if num % i == 0:
#             factors.append(i)
#     return factors
#
#
# def is_prime(num, i):
#     if i == 1:
#         return True
#     elif num % i == 0:
#         return False
#     else:
#         return is_prime(num, i - 1)
#
#
# def find_largest_prime_factor(list_of_factors):
#     list_of_prime_factors = []
#     for numbers in list_of_factors:
#         if is_prime(numbers, numbers//2):
#             list_of_prime_factors.append(numbers)
#     return max(list_of_prime_factors)
#
#
# def find_f(num):
#     factors = find_factors(num)
#     return find_largest_prime_factor(factors)
#
#
# def find_g(num):
#     s_f_n = 0
#     for i in range(num, num + 9):
#         s_f_n += find_f(i)
#     return s_f_n
#
#
# print(find_g(10))

# import turtle
#
# wn = turtle.Screen()
# wn.setup(500, 500)
# turtle = turtle.Turtle()
# turtle.speed("fastest")
#
# step = 100
#
#
# def draw_square(length, angle):
#     for i in range(0, step):
#         for b in range(0, 4):
#             turtle.forward(length + i)
#             turtle.right(angle + b)
#
#
# draw_square(100, 90)

# def find_smallest_number(num):
#     j = 1
#     while True:
#         count = 0
#         for i in range(1, j+1):
#             if j % i == 0:
#                 count += 1
#         if count == num:
#             break
#         j += 1
#     return j
#
#
# num = 16
# print("The number of divisors :", num)
# result = find_smallest_number(num)
# print("The smallest number having", num, " divisors:", result)


# lex_auth_01269442545042227276

# def find_ten_substring(num_str):
#     substring_list = []
#     index = -1
#     for _ in num_str:
#         s = 0
#         temp = ""
#         index += 1
#         for i in range(index, len(num_str)):
#             s += int(num_str[i])
#             temp += num_str[i]
#             if s == 10:
#                 substring_list.append(int(temp))
#                 break
#
#     return substring_list
#
#
# num_str = "2825302"
# print("The number is:", num_str)
# result_list = find_ten_substring(num_str)
# print(result_list)


# def find_duplicates(list_of_numbers):
#     duplicates = []
#     index = -1
#     for digit in list_of_numbers:
#         index += 1
#         for i in range(index+1, len(list_of_numbers)):
#             if digit == list_of_numbers[i]:
#                 if digit not in duplicates:
#                     duplicates.append(digit)
#     return duplicates
#
#
# list_of_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# list_of_duplicates = find_duplicates(list_of_numbers)
# print(list_of_duplicates)


# def check_anagram(data1, data2):
#     data1 = data1.lower()
#     data2 = data2.lower()
#     flag = True
#     for letter1 in data1:
#         for letter2 in data2:
#             if letter1 not in data2:
#                 if data1.index(letter1) == data2.index(letter2):
#                     flag = False
#     return flag
#
#
# print(check_anagram("Schoolmaster", "Theclassroom"))


# def remove_duplicates(value):
#     return_value = ""
#     for letters in value:
#         if letters not in return_value:
#             return_value += letters
#     return return_value
#
#
# print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))


# def check_perfect_number(number):
#     flag = True
#     s = 0
#     for i in range(1, number):
#         if number % i == 0:
#             s += i
#     if s != number or number == 0:
#         flag = False
#     return flag
#
#
# def check_perfectno_from_list(no_list):
#     perfect_list = []
#     for items in no_list:
#         if check_perfect_number(items):
#             perfect_list.append(items)
#     return perfect_list
#
#
# perfectno_list = check_perfectno_from_list([87, 76, 567, 99, 0, 789])
# print(perfectno_list)


# # Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
# # Note: flight_no has the following format - "airline_name followed by three digit number
#
# # Global variable ticket_list = ["AI567:MUM:LON:014", "AI077:MUM:LON:056", "BA896:MUM:LON:067",
# "SI267:MUM:SIN:145", "AI077:MUM:CAN:060", "SI267:BLR:MUM:148", "AI567:CHE:SIN:015", "AI077:MUM:SIN:050",
# "AI077:MUM:LON:051", "SI267:MUM:SIN:146"]
#
#
# def find_passengers_flight(airline_name="AI"):
#     # This function finds and returns the number of passengers travelling in the specified airline.
#     count = 0
#     for i in ticket_list:
#         string_list = i.split(":")
#         if string_list[0].startswith(airline_name):
#             count += 1
#     return count
#
#
# def find_passengers_destination(destination):
#     # Write the logic to find and return the number of passengers traveling to the specified destination
#     count = 0
#     for tickets in ticket_list:
#         string_list = tickets.split(":")
#         if string_list[2] == destination:
#             count += 1
#     return count
#
#
# def find_passengers_per_flight():
#     """Write the logic to find and return a list having number of passengers traveling per flight based on the
#     details in the ticket_list In the list, details should be provided in the format: [flight_no:no_of_passengers,
#     flight_no:no_of_passengers, etc.]. """
#     pass
#
#
# def sort_passenger_list():
#     # Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of
#     # number of passengers
#     pass
#
#
# print(find_passengers_flight("AI"))
# print(find_passengers_destination("LON"))
# print(sort_passenger_list())


# def nearest_palindrome(number):
#     number += 1
#     while True:
#         if is_palindrome(number):
#             break
#         else:
#             number += 1
#     return number
#
#
# def is_palindrome(word):
#     word = str(word)
#     if len(word) < 1:
#         return True
#     else:
#         if word[0] == word[len(word) - 1]:
#             return is_palindrome(word[1:len(word) - 1])
#         else:
#             return False
#
#
# number = 99
# print(nearest_palindrome(number))


# def check_prime(number):
#     flag = True
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 flag = False
#                 break
#     return flag
#
#
# def rotations(num):
#     """-------------------copied-------------------------"""
#     rotation_list = []
#     digit = len(str(num))
#     powTen = pow(10, digit - 1)
#     rotation_list.append(int(num))
#     for i in range(digit - 1):
#         firstDigit = num // powTen
#         left = (num * 10 + firstDigit - (firstDigit * powTen * 10))
#         rotation_list.append(left)
#         num = left
#     return rotation_list
#
#
# def get_circular_prime_count(limit):
#     count = 0
#     flag = True
#     for number in range(limit-1, 1, -1):
#         list_count = 0
#         rotation_list = rotations(number)
#         for i in rotation_list:
#             if check_prime(i) and len(str(i)) == len(str(number)):
#                 list_count += 1
#         if list_count == len(str(i)):
#             count += 1
#     return count
#
#
# print(get_circular_prime_count(1000))


# def validate_name(name):
#     flag = False
#     if 0 < len(name) <= 15 and name.isalpha():
#         flag = True
#     return flag
#
#
# def validate_phone_no(phno):
#     flag = False
#     c = phno.count(phno[0])
#     if len(phno) == 10 and phno.isdigit() and c != 10:
#         flag = True
#     return flag
#
#
# # Start writing your code here
#
# def validate_email_id(email_id):
#     flag = False
#     domains = ['gmail.com', 'hotmail.com', 'yahoo.com']
#     if \
#             email_id.endswith('.com') and \
#             email_id.count('.com') == 1 and \
#             email_id.count('@') == 1:
#         email_id = email_id.split('@')
#         if email_id[1] in domains:
#             flag = True
#     return flag
#
#
# def validate_all(name, phone_no, email_id):
#     flag1 = flag2 = flag3 = True
#     if not validate_name(name):
#         print("Invalid Name")
#         flag1 = False
#     if not validate_email_id(email_id):
#         print("Invalid email id")
#         flag2 = False
#     if not validate_phone_no(phone_no):
#         print("Invalid phone number")
#         flag3 = False
#     if flag1 and flag2 and flag3:
#         print("All the details are valid")
#
#
# validate_all("Tina", "9994599998", "tina@yahoo.com")


# def validate_credit_card_number(card_number):
#     flag = False
#     l1 = []
#     card_number = str(card_number)
#     for i in range(0, len(card_number), 2):
#         l1.append(str(2 * int(card_number[i])))
#     l1.reverse()
#     for digit in l1:
#         s = 0
#         if int(digit) > 9:
#             s = str(int(digit[0]) + int(digit[1]))
#             l1[l1.index(digit)] = s
#     print(l1)
#     for i in range(0, len(l1)):
#         l1[i] = int(l1[i])
#     print(l1)
#     s1 = sum(l1)
#     for i in range(1, len(card_number), 2):
#         s1 += int(card_number[i])
#     if s1 % 10 == 0:
#         flag = True
#     return flag
#
#
# card_number = 5239512608615007
# result = validate_credit_card_number(card_number)
# if result:
#     print("credit card number is valid")
# else:
#     print("credit card number is invalid")

# for var1, var2 in (1, 2), (3, 4):
#     print(var1 + var2, end=" ")

# num_list = [32.5, 44.2, 66.6, 78.4, 99.2]
# for num in range(0, len(num_list)):
#     num_list[num] = math.ceil(num_list[num])
# num_list.reverse()

# list = ["ABC", "DEF", "GHI", 100]
# str = ""
# for item in list:
#     str += str(item)
# print(str)

# def remove_odd(list1):
#     for index in range(len(list1)):
#         if list1[index] % 2 == 0:
#             list1.remove(list1[index])
#
#
# list1 = [1, 2, 3, 4, 5]
# remove_odd(list1)
# print(list1)


"""
list1 = [10, 20, 30, 40, 50, 60]
for num in len(list1):
    print(num, end=" ")

def average(list1):
    sum, count = 0, 0
    for index in range(0, len(list1)-1):
        sum += list1[index]
        count += 1
    return sum/count
print(average([1,2,3,4,5]))
"""

"""
result = 0
list1 = [10, 20, 30]
list2 = [1, 2]
for num in range(len(list1)):
    for num in range(len(list2)):
        result += list1[num] + list2[num]
print(result)
"""

"""
def move(list1, list2):
    for num in list1:
        list2.append(num)
        list1.remove(num)

list1 = [1, 2, 3, 4, 5]
list2 = [10]
move(list1, list2)
print((list1, list2))
"""

"""
elements = [2, 5, 6, 0]
try:
    div = elements[4] / elements[3]
except ZeroDivisionError:
    print("Infinity")
except IndexError:
    print("Index Error")
except Exception:
    print("0")
finally:
    print("In finally block")
"""

"""
try:
    list1 = [8, 4, 2, 0]
    i = list1[0:-1]
    value = len(list1[:-1])
    result = list1[0]/list1[value]
    print(result)
except IndexError:
    print("Index")
except ZeroDivisionError:
    print(ZeroDivisionError)
except:
    print("all")
"""

"""
total = 0
try:
    try:
        num_list = [1, 2, 0, 0]
        for num in range(len(num_list)):
            total += (num_list[num] - num_list[num - 1]) * 4 // (num_list[num] + num_list[num + 1])
    except ZeroDivisionError:
        print("ZD", end=" ")
    except:
        print("OTHER", end=" ")
    finally:
        print("FI", end=" ")
    print(total)
except IndexError:
    print("IN")
"""

"""
try:
    try:
        int(var1)
    except TypeError:
        print("TE1", end=" ")
    except NameError:
        print("NE1", end=" ")
    except ValueError:
        print("VE1", end=" ")
    var1 = 'A'
    'Z'/0
except TypeError:
    print("TE2", end= " ")
except ZeroDivisionError:
    print("ZD2")
"""

"""
try:
    try:
        list1 = [0, 1, 2, 4]
        var1, var2, var3 = list1
        var1/var2
    except ValueError:
        print("VE")
except ZeroDivisionError:
    print("ZD")
except:
    print("CA")
"""

# print(str.__doc__)


"""
try:
    list1 = ["ABC", "PQR", "XYZ", "GHIJKL"]
    str = ""
    for value in list1:
        str += value
    value = len(str) / len(str) % 3
except TypeError:
    print("TE")
except ValueError:
    print("VE")
except ZeroDivisionError:
    print("ZE")
except:
    print("CA")
"""

"""
def func1():
    try:
        var1 = 1/0
        return 1
    except ZeroDivisionError:
        var1 = 1/0
        return 2
    finally:
        return 3


print(func1())
"""

"""
list1 = [10, 20, 0, 40, 0]
def test():
    try:
        var1 = 3
        if list1[var1]/list1[var1+1] > 1:
            value = var1 + 1
    except ZeroDivisionError:
        print("1")
    except IndexError:
        print("2")
    finally:
        print("4")
    print("5")
test()
"""

"""
def fun(var1):
    if var1 < 1:
        return 0
    elif var1 % 2 == 0:
        return fun(var1-1)
    else:
        return var1 + fun(var1 - 2)
print(fun(10))
"""

"""
def calculate(var1, var2):
    while var1 != var2:
        if var1 > var2:
            return calculate(var1-var2, var2)
        else:
            return calculate(var1, var2-var1)
    return var1
print(calculate(10,55))
print(calculate(60, 30))
print(calculate(27, 47))
print(calculate(45, 20))
"""

"""
def func(var1, var2):
    try:
        var3 = int(var1)
        var2 = var3 + "A"
        print(var2)
    except TypeError:
        print("T")
    finally:
        print("TF")
try:
    func("R", 13)
except ValueError:
    print("V")
finally:
    print("OF")
"""

"""
def func1(arg1, *arg2):
    for num in arg2:
        if arg1>=num:
            return num
return 0


def func2(args, arg4=10):
    if(arg3<=arg4):
        return arg3
    return arg4


def func3(arg5, arg6):
    if(arg5!=arg6):
        return False
    return True


res2=func2(1)
res1=func1(res2,1,1,2,5,7,8)
print(func3(arg6=10, agr5=res2))
"""

"""
def func(var1, var2, var3):
    if var1 > var2:         # 1
        return "1"          # 2
    elif var2 > var3:       # 3
        if var1 > var3:     # 4
            return "2"      # 5
        else:               # 6
            return "3"      # 7
    else:                   # 8
        return "4"          # 9


print(func(3, 5, 1))
"""

"""
def func(my_lst, var1):
    new_lst=[]                      # Line1
for num in my_lst:                  # Line2
    if num%var1==0:                # Line3
        new_lst.append(num//var1)   # Line4
    else:                           # Line5
        new_lst.append(0)           # Line6
    return new_lst                  # Line7


try:
    tupl1 = ([1, 2], [3, 4])
    list1 = [(1, 2), (3, 4)]
    list2 = tupl1[0]
    list2[0] = 5
    list1[1] = (6, 7)
    print(tupl1, list1)
except TypeError:
    print("ERR")
"""

"""
def func1():
    try:
        dict1 = {"IN": "India", "US": "United States"}
        del dict1["IN"]
        value = 100 // (len(dict1) - 1)
        print(value)
    except ZeroDivisionError:
        print("ZD", end=" ")
        value = int(dict1[0])
    except KeyError:
        print("KE", end=" ")
    finally:
        print("FI", end=" ")
try:
    func1()
    print("TR")
except:
    print("CA")
"""

"""
var1, var2=10,40
def func1(var1):
    global var2
    var1, var2=20,50
    print(var1, end=" ")
    print(var2, end=" ")
func1(30)
print(var1, end=" ")
print(var2,end=" ")
"""

"""
def func1(var1=1, var2=2):
    print(var1, end=" ")
    print(var2, end=" ")
func1(100, None)
func1(var2=20, var1=10)
func1(var2=10)
"""

"""
# What is the output of the below code snippet?
def func1():
    try:
        1 / 0
        return 1
    except ZeroDivisionError:
        "ABC" + 1
        return 2
    finally:
        int('A')
        return 3


try:
    result = func1()
    print(result)
except:
    print(4)
"""

"""
count = 0
result = []
for number in range(100, 1000):
    if number % 25 == 0:
        arr = []
        for n in str(number):
            arr.append(int(n))
        if arr[0] % 3 == 0 and arr[2] % 5 == 0:
            count += 1
            result.append(number)
print(count)
print(result)
"""