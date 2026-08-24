def scoreOfString(s: str) -> int:
    score = 0
    for w in range(len(s) - 1):
        a = abs(ord(s[w]) - ord(s[w + 1]))
        score += a
    return score


s = "code"

print(scoreOfString(s))
