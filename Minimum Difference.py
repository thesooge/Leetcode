nums = [6,6,0,1,1,4,6]



def minDifference(nums):
    nums = sorted(nums, reverse=True)
    if len(nums) <= 4: 
        return 0
    right = len(nums) - 4
    left = 3
    right_max = max(nums) - nums[right]
    left_min = nums[left] - min(nums)
    print(left_min)
    print(right_max)
    condition = False
    if right_max < left_min:
        condition = True
        nums = sorted(nums, reverse=False)
    print(nums)
    i = 0
    while i != 3:
        if condition == True:
            nums[i] = max(nums)
            i += 1
        else:
            nums[i] = min(nums)
            i += 1
    return (max(nums)-min(nums))

print(minDifference(nums))            