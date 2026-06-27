def productExceptSelf(nums):
    res = []

    for i in range(len(nums)):
        new_arr = nums.copy()
        new_arr[i] = 1
        res.append(new_arr)

    def product(arr):
        val = 1
        for num in arr:
            val *= num
        return val

    for i in range(len(res)):
        res[i] = product(res[i])

    return res
