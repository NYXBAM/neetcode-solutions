def longestConsecutive(nums: list[int]) -> int:
    hashset = set(nums)
    max_len = 0
    for n in hashset:
        if (n - 1) not in hashset:
            current_num = n
            current_streak = 1
            while current_num + 1 in hashset:
                current_streak += 1
                current_num += 1
            max_len = max(max_len, current_streak)

    return max_len


nums = [2, 20, 4, 10, 3, 4, 5]
# must return 4

print(longestConsecutive(nums))
