def maxArea(heights):
    i = 0
    j = len(heights) - 1
    max_area = 0

    while i < j:
        new_area = (j - i) * min(heights[i], heights[j])
        max_area = max(max_area, new_area)

        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
