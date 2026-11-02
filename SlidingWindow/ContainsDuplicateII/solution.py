def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()
    for n in range(len(nums)):
        if nums[n] in window:
            return True
        else:
            window.add(nums[n])
        if len(window) > k:
            window.remove(nums[n - k])
    return False


nums = [1, 2, 3, 1]
k = 3

print(containsNearbyDuplicate(nums, k))


# Similar problem solution
# For training purpose
def nearby_duplicate(nums, k, target) -> bool:
    window = set()
    for n in range(len(nums)):
        if (target - nums[n]) in window:
            return True
        else:
            window.add(nums[n])
        if len(window) > k:
            window.remove(nums[n - k])
    return False


nums = [1, 2, 3, 4, 5]
k = 2
target = 7

print(nearby_duplicate(nums, k, target))
