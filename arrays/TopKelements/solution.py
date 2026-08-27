from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash_map = {}
    for n in nums:
        if n not in hash_map:
            hash_map[n] = 1
        else:
            hash_map[n] += 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for n, c in hash_map.items():
        buckets[c].append(n)

    res = []
    for n in buckets[::-1]:
        for num in n:
            res.append(num)
            if len(res) == k:
                return res

    return res


def pythonictTopKFrequent(nums: list[int], k: int) -> list[int]:
    hash_map = defaultdict(int)
    for n in nums:
        hash_map[n] += 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for n, c in hash_map.items():
        buckets[c].append(n)

    res = []
    for n in buckets[::-1]:
        for num in n:
            res.append(num)
            if len(res) == k:
                return res

    return res


print(topKFrequent([1, 2, 2, 3, 3, 3], k=2))
print(pythonictTopKFrequent([1, 2, 2, 3, 3, 3], k=2))
