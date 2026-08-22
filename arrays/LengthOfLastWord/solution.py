def lengthOfLastWord(s: str) -> int:
    count = 0
    for i in range(len(s) - 1, -1, -1):
        word = s[i]
        if word == " " and count == 0:
            continue
        if word == " " and count > 0:
            break
        count += 1
    return count


s = "   fly me   to   the moon  "

print(lengthOfLastWord(s))
