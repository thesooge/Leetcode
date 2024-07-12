
nums = [1,2,1,3,2,5]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            nums[j] = ""
            nums[i] = ""

nums = list(set(nums))

for i in nums: 
    if i == "": 
        nums.remove(i)
print(nums)