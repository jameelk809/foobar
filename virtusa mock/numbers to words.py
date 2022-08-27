def convert_to_words(num):
    res = []
    l = len(num)

    if l == 0:
        return ''

    if l > 4:
        return

    single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens_power = ["hundred", "thousand"]

    if l == 1:
        return single_digits[ord(num[0]) - 48]

    x = 0
    while x < len(num):
        if l >= 3:
            if ord(num[x]) - 48 != 0:
                res.append(single_digits[ord(num[x]) - 48] + " ")
                res.append(tens_power[l - 3] + " ")
            l -= 1
        else:
            if ord(num[x]) - 48 == 1:
                sum = (ord(num[x]) - 48 + ord(num[x + 1]) - 48)
                res.append(two_digits[sum])
                break
            elif ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0:
                res.append("twenty")
                break
            else:
                i = ord(num[x]) - 48
                if i > 0:
                    res.append(tens_multiple[i] + " ")
                else:
                    res.append("" + "")
                x += 1
                if ord(num[x]) - 48 != 0:
                    res.append(single_digits[ord(num[x]) - 48])
        x += 1
    print(res)
    return "".join(res)


print(convert_to_words(str(987)))
