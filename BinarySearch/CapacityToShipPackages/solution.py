def shipWithinDays(weights: list[int], days: int) -> int:
    left = max(weights)
    right = sum(weights)
    result = sum(weights)
    while left <= right:
        mid = (left + right) // 2
        day_weight = 0
        day_use = 1
        for w in weights:
            if day_weight + w <= mid:
                day_weight += w
            else:
                day_use += 1
                day_weight = w
        if day_use <= days:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


weights = [2, 4, 6, 1, 3, 10]
days = 4
print(shipWithinDays(weights, days))
