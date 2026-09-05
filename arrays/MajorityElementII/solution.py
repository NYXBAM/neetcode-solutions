def majorityElement(nums: list[int]) -> list[int]:
    count1 = 0
    count2 = 0
    candidate1 = None
    candidate2 = None
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = n
            count1 = 1
        elif count2 == 0:
            candidate2 = n
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    result = []
    count1 = 0
    count2 = 0
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
    if candidate1 is not None and count1 > len(nums) // 3:
        result.append(candidate1)
    if candidate2 is not None and count2 > len(nums) // 3:
        result.append(candidate2)
    return result


nums = [5, 2, 3, 2, 2, 2, 2, 5, 5, 5]


print(majorityElement(nums))

from collections import Counter


def slowMajorityElement(nums):
    count = Counter(nums)
    return [n for n, count in count.items() if count > len(nums) // 3]


print(slowMajorityElement(nums))
