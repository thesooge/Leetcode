nums = [1,3,5,6]
target = 2

if target in nums:
    print(nums.index(target))
else: 
    for i in range(len(nums)):
        if nums[i] > target : 
            print(nums.index(nums[i]))
            break 
        elif i == len(nums) - 1:
            print(nums.index(nums[i]) + 1)
            break

