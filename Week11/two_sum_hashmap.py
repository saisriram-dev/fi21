# Two sum problem using hashmap

# nums = [2, 7, 11, 15]
# target = 9
# complement = target - num


# Code:
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


"""
1st loop:
    num = 2
    complement = 7
    seen = {2: 0}

2nd loop:
    num = 7
    complement = 2
    seen = {2: 0, 7: 1}
    complement in seen -> True
    return [0, 1]
"""
