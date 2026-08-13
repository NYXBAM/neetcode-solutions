from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Complexity O(N*K log K)"""
    seen = {}
    for word in strs:
        srt = tuple(sorted(word))
        if srt in seen:
            seen[srt].append(word)
        else:
            seen[srt] = [word]
    return list(seen.values())


def fast_group_anagrams(strs: list[str]) -> list[list[str]]:
    """Complexity O(N*K)"""
    res = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for w in word:
            count[ord(w) - ord("a")] += 1
        res[tuple(count)].append(word)
    return list(res.values())
