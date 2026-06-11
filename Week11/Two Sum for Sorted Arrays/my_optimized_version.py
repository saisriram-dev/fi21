def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1

    while i < j:
        curr_sum = numbers[i] + numbers[j]

        if curr_sum < target:
            i += 1
        elif curr_sum > target:
            j -= 1
        else:
            return [i + 1, j + 1]
