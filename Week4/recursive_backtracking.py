# Recursive Bactracking

# To find sub-sets of a set, we can use recursive backtracking.
# The idea is to explore all possible combinations of elements in the set, and for each combination,
# we can either include or exclude the current element.


def subsets(nums):
    n = len(nums)
    res, sol = [], []

    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return

        # Don't pick nums[i]
        backtrack(i + 1)

        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()

    backtrack(0)
    return res
