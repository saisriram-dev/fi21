def threeSum(nums):
    result = set()

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            first = nums[i]
            second = nums[j]
            pair_sum = first + second

            remaining = [nums[k] for k in range(len(nums)) if k not in (i, j)]

            if -(pair_sum) in remaining:
                result.add(tuple(sorted([first, second, -pair_sum])))
    return [list(x) for x in result]
