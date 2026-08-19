def replaceElements(arr: list[int]) -> list[int]:
    max_right = arr[-1]
    arr[-1] = -1
    temp = 0
    for n in range(len(arr) - 2, -1, -1):
        temp = arr[n]
        arr[n] = max_right
        if temp > max_right:
            max_right = temp
    return arr


arr = [2, 4, 5, 3, 1, 2]

print(replaceElements(arr))
