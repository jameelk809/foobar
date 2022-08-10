def count_words(inp_string):
    d = {}
    temp = []
    list_words = inp_string.split()
    for word in list_words:
        count = list_words.count(word)
        d[word] = count
    return d


def max_occurance_word(strr):
    d = count_words(strr)
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


strr = 'are the contents of the site are only for general information the use'
print(count_words(strr))
print(max_occurance_word(strr))


