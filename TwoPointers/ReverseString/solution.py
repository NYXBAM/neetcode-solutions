def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["r", "a", "c", "e", "c", "a", "r"]

print(reverseString(s))
