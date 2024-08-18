nums = [1,2,3,4,5]

first = float('inf')
second = float('inf')

for i in range(len(nums)):
    if nums[i] <= first:
        first = nums[i]
    elif nums[i] > first and nums[i] <= second:
        second = nums[i]
    else:
        print(True)        
 