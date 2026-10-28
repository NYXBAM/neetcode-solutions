def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    result = set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in result:
            result.remove(s[left])
            left += 1
        result.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


s = "zxyzxyz"


print(lengthOfLongestSubstring(s))
