def sortArray(nums: list[int]) -> list[int]:
    def quick(low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        nums[mid], nums[high] = nums[high], nums[mid]
        pivot = nums[high]
        j = low
        for n in range(low, high):
            if nums[n] < pivot:
                nums[j], nums[n] = nums[n], nums[j]
                j += 1
        nums[j], nums[high] = nums[high], nums[j]
        quick(low, j - 1)
        quick(j + 1, high)

    quick(0, len(nums) - 1)
    return nums
