# Hills and valleys

# Hill -> nums[i - 1] < nums[i] > nums[i + 1] Here hill is the index of the hill element.
# Valley -> nums[i - 1] > nums[i] < nums[i + 1] Here valley is the index of the valley element.

def count_hill_valley(nums):
    hill = 0
    valley = 0

    # Remove consecutive duplicates only
    cleaned = [nums[0]]

    for x in nums[1:]:
        if x != cleaned[-1]:
            cleaned.append(x)

    for i in range(1, len(cleaned)-1):
        if cleaned[i] > cleaned[i-1] and cleaned[i] > cleaned[i+1]:
            hill += 1

        elif cleaned[i] < cleaned[i-1] and cleaned[i] < cleaned[i+1]:
            valley += 1

    return hill, valley
