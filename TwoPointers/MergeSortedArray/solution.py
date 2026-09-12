def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


nums1 = [10, 20, 20, 40, 0, 0]
m = 4
nums2 = [1, 2]
n = 2


print(merge(nums1, m, nums2, n))
