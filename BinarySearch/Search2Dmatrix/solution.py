def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    left = 0
    right = len(matrix) * len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        res = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
        if res == target:
            return True
        elif res > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10

print(searchMatrix(matrix, target))
