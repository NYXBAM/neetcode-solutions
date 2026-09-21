def numRescueBoats(people: list[int], limit: int) -> int:
    left = 0
    right = len(people) - 1
    boats = 0
    people.sort()
    while left < right:
        if people[left] + people[right] <= limit:
            boats += 1
            left += 1
            right -= 1
        else:
            boats += 1
            right -= 1
    if left == right:
        boats += 1
    return boats


people = [5, 1, 4, 2]
limit = 6
print(numRescueBoats(people, limit))
