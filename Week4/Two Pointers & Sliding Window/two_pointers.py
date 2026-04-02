# Two-pointer technique
"""This function takes a sorted array of integers and returns a new array containing the squares
of the original integers, also sorted in non-decreasing order."""


def sort_square(nums):
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    result.reverse()

    return result
