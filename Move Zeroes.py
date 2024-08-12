nums = [0,0,1]



k = 0

for i in range(len(nums)):
    if nums[i] != 0:
        tmp = nums[k]
        nums[k] = nums[i]
        nums[i] = tmp
        k += 1    



print((nums))