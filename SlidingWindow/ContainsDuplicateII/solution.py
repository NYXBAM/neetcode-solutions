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
