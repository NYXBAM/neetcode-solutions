def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j - 1] == nums[j]:
                continue
            left = j + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                    left += 1
    return result


nums = [3, 2, 3, -3, 1, 0]
target = 3

print(fourSum(nums, target))
