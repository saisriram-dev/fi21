def maxArea(heights):
    areas = []

    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            area = min(heights[i], heights[j]) * (j - i)
            areas.append(area)

    return max(areas)
