def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    left = 0
    right = len(nums) - 1
    while right > left:
        nums[left], nums[right] = nums[right], nums[left]
        right -= 1
        left += 1
    right = k - 1
    left = 0
    while right > left:
        nums[left], nums[right] = nums[right], nums[left]
        right -= 1
        left += 1
    left = k
    right = len(nums) - 1
    while right > left:
        nums[left], nums[right] = nums[right], nums[left]
        right -= 1
        left += 1


nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4


print(rotate(nums, k))
print(nums)
