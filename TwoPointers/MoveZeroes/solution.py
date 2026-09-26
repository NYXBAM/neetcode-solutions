def moveZeroes(nums: list[int]) -> None:
    write = 0
    scan = 0
    while scan < len(nums):
        if nums[scan] != 0:
            nums[write], nums[scan] = nums[scan], nums[write]
            write += 1
        scan += 1
