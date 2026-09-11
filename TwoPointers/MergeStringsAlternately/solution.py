def mergeAlternately(word1: str, word2: str) -> str:
    res = []
    i = min(len(word1), len(word2))
    for n in range(i):
        res.append(word1[n])
        res.append(word2[n])

    if len(word1) > len(word2):
        res.append(word1[i:])
    else:
        res.append(word2[i:])

    return "".join(res)


word1 = "ab"
word2 = "abbxxc"


# word1 = "abc"
# word2 = "xyz"
print(mergeAlternately(word1, word2))
