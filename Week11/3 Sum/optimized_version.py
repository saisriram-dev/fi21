def threeSum(nums):
    nums.sort()
    triplets = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return triplets
