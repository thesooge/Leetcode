result = []

subset = []

nums = [1,2,3]

def inj(i):
    if i == len(nums):
        result.append(subset[:])
        return
    subset.append(nums[i])
    for z in range(len(nums)):
        inj(z)
   
print(result)
print(subset)