def isPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if isPalindrome(s, (left + 1), right) or isPalindrome(s, left, (right - 1)):
                return True
            return False

        left += 1
        right -= 1
    return True


s = "abbda"

print(validPalindrome(s))
