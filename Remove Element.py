nums = [0,1,2,2,3,0,4,2]
val = 2
k = 0
length = len(nums)
for i in range(0, length):
    if nums[i] != val:
        k += 1
    else :
        nums[i] = "_"
