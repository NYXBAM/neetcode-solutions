def removeDuplicates(nums: list[int]) -> int:
    write = 0
    read = 1
    while read < len(nums):
        if nums[read] == nums[write]:
            nums[write] = nums[read]
            read += 1
        else:
            nums[write + 1] = nums[read]
            read += 1
            write += 1
    return write + 1


nums = [2, 10, 10, 30, 30, 30]

print(removeDuplicates(nums))
