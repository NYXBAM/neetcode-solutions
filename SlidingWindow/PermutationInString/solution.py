from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    target = Counter(s1)
    window = Counter(s2[: len(s1)])
    if window == target:
        return True
    for right in range(len(s1), len(s2)):
        window[s2[right]] += 1
        left = right - len(s1)
        window[s2[left]] -= 1
        if window[s2[left]] == 0:
            del window[s2[left]]
        if window == target:
            return True
    return False


s1 = "abc"
s2 = "lecabee"

print(checkInclusion(s1, s2))
