nums = [3,-2,12]

min_dist = abs(nums[0])
num = nums[0]
for i in range(1, len(nums)):
    if abs(nums[i]) < min_dist:
        min_dist = abs(nums[i])
        num = nums[i]  

if num < 0:
    if (num * -1) in nums:
        num = num * -1

print(num)