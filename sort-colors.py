nums = [2,0,2,1,1,0]

for j in range(len(nums)):
    for i in range(0, -len(nums), -1):
        if nums[i] < nums[i - 1]:
            a = nums[i - 1]
            nums.pop(i-1)
            nums.append(a)
            


print(nums)        