def mostWordsFound(sentences):
    res = -1
    for sent in sentences:
        len_sent = len(sent.split())
        if len_sent > res:
            res = len_sent
    return res


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))
