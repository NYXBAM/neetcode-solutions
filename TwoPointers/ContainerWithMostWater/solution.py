def maxArea(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    maxArea = 0
    area = 0
    while left < right:
        if heights[left] < heights[right]:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(area, maxArea)
            left += 1
        else:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(area, maxArea)
            right -= 1

    return maxArea


height = [1, 7, 2, 5, 4, 7, 3, 6]


print(maxArea(height))
