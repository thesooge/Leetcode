nums = [0,1,2,2,3,0,4,2]
val = 2
k = len(nums)
for i in range(len(nums)):
    if nums[i] == val:
        k -= 1
        nums[i] = "_"

for item in nums[:]:
    print(item)    
    if item == "_":
        nums.remove(item)
print(nums)
print(k)        