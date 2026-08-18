def majority_element(nums):
    res = {}
    for n in nums:
        if n in res:
            res[n] += 1
        else:
            res[n] = 1
        if res[n] > len(nums) // 2:
            return n
    return res


# Fast solution time O(n)
# Space o(1)
def fast_majority(nums):
    count = 0
    candidate = nums[0]
    for n in nums:
        if count == 0:
            candidate = n
        if n == candidate:
            count += 1
        else:
            count -= 1
    return candidate


nums = [5, 5, 1, 1, 1, 5, 5]

print(fast_majority(nums))
