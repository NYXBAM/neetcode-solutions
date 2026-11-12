def firstMissingPositive(nums: list[int]) -> int:
    for i in range(len(nums)):
        while (
            nums[i] != i + 1
            and nums[i] <= len(nums)
            and nums[i] > 0
            and nums[nums[i] - 1] != nums[i]
        ):
            x = nums[i]
            nums[i], nums[x - 1] = nums[x - 1], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


print(firstMissingPositive([1, 2, 4, 5, 6, 3, 1]))  # 7
