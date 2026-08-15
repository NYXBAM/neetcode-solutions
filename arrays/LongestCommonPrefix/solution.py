def longestCommonPrefix(strs: list[str]) -> str:
    prefix = strs[0]
    if not strs:
        return ""
    for w in strs:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
