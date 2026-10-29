def characterReplacement(s: str, k: int) -> int:
    left = 0
    result = {}
    max_len = 0
    for right in range(len(s)):
        if s[right] not in result:
            result[s[right]] = 1
        else:
            result[s[right]] += 1
        max_freq = max(result.values())
        while (right - left + 1) - max_freq > k:
            result[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len


s = "AAABABB"
k = 1
print(characterReplacement(s, k))
