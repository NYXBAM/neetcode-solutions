def minSubArrayLen(target: int, nums: list[int]) -> int:
    window = 0
    left = 0
    minimum = len(nums) + 1
    for right in range(len(nums)):
        window += nums[right]
        while window >= target:
            minimum = min(minimum, right - left + 1)
            window -= nums[left]
            left += 1

    return 0 if minimum > len(nums) else minimum


target = 10
nums = [2, 1, 5, 1, 5, 3]  # must be 3

print(minSubArrayLen(target, nums))
