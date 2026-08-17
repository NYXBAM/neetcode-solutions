nums = [3, 2, 2, 3]
val = 3


def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for n in nums:
        if n != val:
            nums[k] = n
            k += 1
    return k


# Second solution with 2 pointers
def rm_elem(nums: list[int], val: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1
    return left


print(rm_elem(nums, val))
