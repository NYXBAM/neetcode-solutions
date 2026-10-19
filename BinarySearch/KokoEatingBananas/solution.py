def minEatingSpeed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)
    res = max(piles)
    while left <= right:
        total = 0
        mid = (left + right) // 2
        for p in piles:
            total += p // mid
            if p % mid != 0:
                total += 1

        if total <= h:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


piles = [1, 4, 3, 2]
h = 9

print(minEatingSpeed(piles, h))
