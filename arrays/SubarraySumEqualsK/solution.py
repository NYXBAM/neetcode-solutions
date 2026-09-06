def subarraySum(nums: list[int], k: int) -> int:
    prefix = 0
    hashmap = {0: 1}
    counts = 0
    for n in range(len(nums)):
        prefix = nums[n] + prefix
        if prefix - k in hashmap:
            counts += hashmap[prefix - k]
        if prefix in hashmap:
            hashmap[prefix] += 1
        else:
            hashmap[prefix] = 1
    return counts


arr = [2, -1, 1, 2]
k = 2


print(subarraySum(arr, k))
