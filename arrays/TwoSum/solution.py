# This solution has complexity O(n^2)
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        i = 0
        for n in range(len(nums)):
            for nr in range(i + 1, len(nums)):
                if nums[n] + nums[nr] == target:
                    return [n, nr]

    # faster solution with O(1)

    def twoSumOptimized(nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, num in enumerate(nums):
            b = target - num
            if b in seen:
                return [seen[b], index]
            seen[num] = index
