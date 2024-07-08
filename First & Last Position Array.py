nums = [1]

target = 1

target_li = []

counter = 0

for i in range(len(nums)):
    if nums[i] == target:
        target_li.append(nums.index(nums[i]))
        break
for j in range(len(nums)-1 , -1, -1):
    counter += 1
    if nums[j] == target:
        target_li.append(len(nums) - counter)    
        break

if target_li == []:
    target_li.append(-1)
    target_li.append(-1)



print(target_li)        